import os
import sys
import shutil
from pathlib import Path
import yt_dlp
import questionary
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn

console = Console()

BANNER = r"""
________                __   ___________   ___.           
\______ \ _____ _______|  | _\__    ___/_ _\_ |__   ____  
 |    |  \\__  \\_  __ \  |/ / |    | |  |  \ __ \_/ __ \ 
 |    `   \/ __ \|  | \/    <  |    | |  |  / \_\ \  ___/ 
/_______  (____  /__|  |__|_ \ |____| |____/|___  /\___  >
        \/     \/           \/                  \/     \/ 
"""

AUTHOR = "[bold green]Author:[/bold green] ZXTXZEC\n[bold cyan]GitHub:[/bold cyan] https://github.com/zxtxzec"
DISCLAIMER = (
    "[bold yellow]Disclaimer:[/bold yellow] This tool is for personal and educational use only.\n"
    "You are responsible for how you use it. Do not download copyrighted content without permission.\n"
)

def print_banner():
    console.print(f"[bold cyan]{BANNER}[/bold cyan]")
    console.print(Panel.fit(
        "[bold magenta]DarkTube - Midnight CLI Downloader[/bold magenta]\n"
        "[white]Advanced CLI experience with full functionality, no GUI required[/white]",
        title="Welcome to DarkTube", padding=(1, 2))
    )
    console.print(AUTHOR)
    console.print(DISCLAIMER)
    console.rule()

def get_download_path():
    path = Path.home() / "Downloads" / "DarkTube"
    path.mkdir(parents=True, exist_ok=True)
    return path

def choose_format():
    return questionary.select(
        "Choose download format:",
        choices=["Audio (MP3)", "Audio (Original)", "Video (Best Quality)"]
    ).ask()

def ask_embed_thumbnail():
    return questionary.confirm("Embed thumbnail/cover if available?").ask()

def ask_rename():
    return questionary.confirm("Prompt to rename files after download?").ask()

def get_links():
    links = questionary.text("Paste one or more YouTube URLs (space-separated):").ask()
    if not links:
        return []
    return links.strip().split()

def rename_files(download_dir):
    console.print("\n[bold yellow]Rename downloaded files (optional):[/bold yellow]")
    for filename in os.listdir(download_dir):
        full_path = os.path.join(download_dir, filename)
        new_name = questionary.text(f"Rename '{filename}' (leave blank to skip):").ask()
        if new_name:
            new_path = os.path.join(download_dir, new_name)
            shutil.move(full_path, new_path)
            console.print(f"[green]Renamed to:[/green] {new_name}")

def build_options(mode, embed_thumb, output_path):
    postprocessors = []
    if mode == "Audio (MP3)":
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0'
        })
    if embed_thumb:
        postprocessors.append({'key': 'EmbedThumbnail'})

    return {
        'format': 'bestaudio/best' if 'Audio' in mode else 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': postprocessors,
        'merge_output_format': 'mp4' if 'Video' in mode else None,
        'progress_hooks': [progress_hook],
        'quiet': True,
    }

def progress_hook(d):
    if d['status'] == 'downloading':
        console.log(f"[cyan]Downloading:[/cyan] {d.get('filename', '')} | Speed: {d.get('speed', 'N/A')} | ETA: {d.get('eta', 'N/A')}s")
    elif d['status'] == 'finished':
        console.log(f"[green]Finished:[/green] {d['filename']}")

def download_videos(links, ydl_opts):
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), TimeElapsedColumn(), transient=True) as progress:
        task = progress.add_task("Starting download...", total=None)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(links)
        except Exception as e:
            console.print(f"[bold red]Error during download:[/bold red] {e}")
        finally:
            progress.update(task, description="Download complete")
            progress.stop()

def open_folder(path):
    if sys.platform.startswith("linux"):
        os.system(f"xdg-open {path}")
    elif sys.platform == "darwin":
        os.system(f"open {path}")
    elif sys.platform == "win32":
        os.startfile(path)

def main_menu():
    return questionary.select(
        "Choose an action:",
        choices=[
            "📅 Start Download",
            "🗆 View Download Folder",
            "❌ Quit"
        ]
    ).ask()

def main():
    print_banner()
    while True:
        choice = main_menu()

        if choice == "❌ Quit":
            console.print("\n[bold magenta]Thanks for using DarkTube. See you next time![/bold magenta]")
            break

        elif choice == "🗆 View Download Folder":
            path = get_download_path()
            console.print(f"Opening: {path}")
            open_folder(path)

        elif choice == "📅 Start Download":
            links = get_links()
            if not links:
                console.print("[red]No links provided. Returning to main menu.[/red]\n")
                continue

            format_choice = choose_format()
            embed_thumb = ask_embed_thumbnail()
            rename_after = ask_rename()
            path = get_download_path()

            opts = build_options(format_choice, embed_thumb, str(path))
            download_videos(links, opts)

            console.print(Panel.fit(f"[green]Download complete! Files saved to:[/green] {path}"))
            if rename_after:
                rename_files(path)

            console.rule("[bold blue]End of Operation[/bold blue]")

if __name__ == "__main__":
    main()
