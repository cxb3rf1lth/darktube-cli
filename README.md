# 🎿 DarkTube CLI Downloader
This easy to use and run CLI app scrapes and downloads audio, video, and optionally thumbnails of YouTube videos from any video link at the best and highest possible quality. You can insert and download multiple links at a time as well as select the audio format and optionally change file name upon finishing the download. You can then directly access your downloads folder from the CLI to view your downloads.

```
________                __   ___________   ___.           
\______ \ _____ _______|  | _\__    ___/_ _\_ |__   ____  
 |    |  \\__  \\_  __ \  |/ / |    | |  |  \ __ \_/ __ \ 
 |    `   \/ __ \|  | \/    <  |    | |  |  / \_\ \  ___/ 
/_______  (____  /__|  |__|_ \ |____| |____/|___  /\___  >
        \/     \/           \/                  \/     \/ 
```

> A modern, intuitive, and high-quality **YouTube downloader** with zero GUI and maximum control.  
> ⚡ Built with `yt-dlp`, `rich`, `questionary`, and advanced CLI enhancements.

---

## ✨ Features

* 📅 Download audio (MP3, original) or full video in best quality
* ✅ Thumbnail embedding support
* ✏️ Rename files post-download
* 🗅️ Open download folder directly
* 🧱 Full CLI navigation with menu and feedback
* 🎨 Stylish and user-friendly interface via `rich`
* ♻️ Cross-platform support (Linux, macOS, Windows, Termux)

---

## 🖼️ Screenshot
![2025-07-03_22-13](https://github.com/user-attachments/assets/39f3240b-c4fa-4001-bff0-518d2ffc3505)
![2025-07-03_22-14_1](https://github.com/user-attachments/assets/ee3ac68d-8c5a-4366-8436-135690a0716a)
![2025-07-03_22-14_2](https://github.com/user-attachments/assets/eb465f3e-5e81-4be4-bbb1-2a02fce4ab82)

---

## ⚙️ Quick Install & Setup

### ✅ Requirements

* Python 3.8+
* ffmpeg installed and in PATH

### 🛠️ Setup Script (Linux/macOS/WSL)

```bash
# Clone the repo
git clone https://github.com/cxb3rf1lth/darktube-cli.git
cd darktube-cli

# Run setup
bash setup.sh
```

### 🛠️ Setup Script (Termux)

```bash
# Clone the repo
git clone https://github.com/cxb3rf1lth/darktube-cli.git
cd darktube-cli

# Give storage permission (if not done already)
termux-setup-storage

# Run Termux setup
bash setup_termux.sh
```

---

## ▶️ Run the CLI Tool

After setup:

```bash
python darktube.py
```

Or if you prefer the standalone `.pyz`:

```bash
python darktube.pyz
```

---

## 📂 Download Folder

All files are saved in:

```
~/Downloads/DarkTube/  # For Linux/macOS/WSL
~/storage/downloads/DarkTube/  # For Termux
```

---

## 📜 Disclaimer

This tool is intended **strictly for personal and educational use only**.  
You are solely responsible for how you use it.  
⚠️ Do not download copyrighted content without permission.

---

## 👤 Author

**ZedSec/cxb3rf1lth**  
🔗 GitHub: [github.com/cxb3rf1lth/zedseclabs/zxtxzec](https://github.com/cxb3rf1lth)

---

## 🧾 License

MIT License – Free to use, modify, and share with credit.

---

## ❤️ Support

If this helped you, consider giving the repo a ⭐ on GitHub!

