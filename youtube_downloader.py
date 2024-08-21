while True:
    import yt_dlp
    import os
    
    
    def short_to_url(link):
        if "youtube.com/shorts/" in link:
            # Video ID'yi al
            video_id = link.split("/")[-1]
            # Uzun URL'yi oluştur
            long_url = f"https://www.youtube.com/watch?v={video_id}"
            return long_url
        return link
    
    
    # YouTube video URL'sini girin
    url = input("YouTube video URL'sini girin: ").strip()
    
    # URL türünü kontrol et ve gerekirse kısa URL'yi uzun URL'ye çevir
    url = short_to_url(url)
    
    try:
        # Masaüstü klasörünün yolunu al
        desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    
        # Video indirme işlemi
        ydl_opts = {
            'format': 'best',  # En iyi kalitede indirme
            'outtmpl': os.path.join(desktop_folder, '%(title)s.%(ext)s'),  # Dosya ismi formatı
        }
    
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Video indiriliyor...")
            ydl.download([url])
            print("İndirme tamamlandı!")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    print("\n\n")
