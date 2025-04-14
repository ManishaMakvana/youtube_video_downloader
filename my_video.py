import os
import subprocess

# Path to your link file
text_file = "C:/Users/Manisha/Desktop/youtube/songs.txt"

# Folder to save videos
folder_name = os.path.splitext(os.path.basename(text_file))[0]
download_folder = os.path.join(os.getcwd(), folder_name)
os.makedirs(download_folder, exist_ok=True)

# Read YouTube URLs
with open(text_file, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip().startswith("http")]

print(f"📁 Downloading to: {download_folder}")
print(f"🔗 Found {len(urls)} videos\n")

# Download each video with merged format
for i, url in enumerate(urls, 1):
    print(f"{i}. Downloading: {url}")
    try:
        subprocess.run([
            "yt-dlp",
            "--ffmpeg-location", "C:/ffmpeg/bin",  # 👈 Point directly to your ffmpeg folder
            "-f", "bestvideo+bestaudio",
            "--merge-output-format", "mp4",
            "-o", os.path.join(download_folder, "%(title)s.%(ext)s"),
            url
        ], check=True)
        print("   ✅ Downloaded\n")
    except subprocess.CalledProcessError as e:
        print("   ❌ Download failed:", e)
