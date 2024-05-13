import os
import pytube

def find_desktop_path():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop

def download_video(url, quality):
    try:
        youtube = pytube.YouTube(url)
        streams = youtube.streams.filter(file_extension="mp4", res=quality).all()
        
        if len(streams) > 0:
            video = streams[0]
            desktop_path = find_desktop_path()
            
            video.download(output_path=desktop_path)
            
            video_file_name = os.path.basename(video.title)
            print(f"Video başarıyla indirildi ve masaüstünde kaydedildi. İndirilen dosya adı: {video_file_name}")
        else:
            print("Belirtilen kalitede video bulunamadı.")
    except Exception as e:
        print("Video indirme işlemi başarısız oldu:", str(e))

if __name__ == "__main__":
    video_url = input("İndirilecek video URL'sini girin: ")
    video_quality = input("İndirme kalitesini seçin (örneğin, 720p veya 1080p): ").strip()
    
    download_video(video_url, video_quality)
