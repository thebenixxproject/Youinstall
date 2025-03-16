import yt_dlp

def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Failed to download video from URL: {url}")

if __name__ == "__main__":
    video_url = input("Enter the URL of the video you want to download: ")
    output_path = "C:\\Users\\Admin\\Desktop\\code\\Python\\youinstall\\downloads"
    download_video(video_url, output_path)