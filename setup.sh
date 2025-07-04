#!/bin/bash

# DarkTube CLI Setup Script
# Author: cxb3rf1lth / zxtxzec
# GitHub: https://github.com/cxb3rf1lth/darktube-cli

set -e

echo -e "\n[1/6] 🔧 Checking Python version..."
PYTHON_OK=$(python3 -c "import sys; print(sys.version_info >= (3, 8))")
if [ "$PYTHON_OK" != "True" ]; then
  echo "❌ Python 3.8 or newer is required. Exiting."
  exit 1
fi

echo -e "\n[2/6] 🧪 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo -e "\n[3/6] 📦 Installing dependencies..."
pip install --upgrade pip
pip install yt-dlp rich questionary

echo -e "\n[4/6] 🔍 Checking for ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
  echo "⚠️ ffmpeg not found! Please install it via your package manager before continuing."
  echo "Example for Arch Linux: sudo pacman -S ffmpeg"
  echo "Example for Debian/Ubuntu: sudo apt install ffmpeg"
  exit 1
else
  echo "✅ ffmpeg found."
fi

echo -e "\n[5/6] 🧱 Verifying required files..."
if [ ! -f "darktube.py" ]; then
  echo "❌ darktube.py not found. Please make sure this script is in the same directory."
  exit 1
fi

echo -e "\n[6/6] ✅ Setup complete!"
echo -e "To run the CLI tool:\n"
echo -e "  source venv/bin/activate && python darktube.py\n"
