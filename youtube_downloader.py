while True:  # Kütüphane eklemeleri için bir döngü oluşturuyoruz.
    import subprocess  # Kütüphane kurulumlarında yardımcı olması için subprocess kütüphanesini içe aktarıyoruz.
    import pip  # Kütüphane kurulumlarında yardımcı olması için pip kütüphanesini içe aktarıyoruz.

    try:  # Kütüphanelerin sorunsuz olarak içe aktarıldığından emin olmak için kullanıyoruz.
        import time  # Gecikme için time kütüphanesini içe aktarıyoruz.
        import pytube # Youtube kütüphanesini içe aktarıyoruz..
        import os
        break  # Kütüphanelerin sorunsuz eklenmesi durumunda döngüyü durduruyoruz.

    except:  # İçe aktarırken hata olması durumunda alttaki kodları çalıştırıyoruz(bu kısım .py dosyası ile açanlar için).
        try:  # python.exe' nin dosya yolunu yazarken hata olması durumunda çökmeyi önlemek için try kullanıyoruz.
            python_exe_path = input("python.exe'nin dosya yolunu girin: ")  # kullanıcıdan python.exe' nin yolunu
            # istiyoruz.
            subprocess.run([python_exe_path, "-m", "pip", "install", "time"])  # python.exe ile kütüphaneyi kuruyoruz.
            subprocess.run([python_exe_path, "-m", "pip", "install", "pytube"])  # python.exe ile kütüphaneyi
            # kuruyoruz.
            subprocess.run([python_exe_path, "-m", "pip", "install", "os"])
            break  # Kütüphaneler başarılı bir şekilde içe aktarılınca döngüyü sonlandırıyoruz.

        except FileNotFoundError:  # python.exe' nin dosya yolu yanlış yazılırsa alttaki kod çalışır.
            print("\nDosya yolunu kontrol edin\n:")  # Hata mesajı veriyoruz.

        except Exception as e:  # Oluşan hataları e değişkenine atar ve isteğe bağlı işlem ve düzenleme yapmamıza
            # olanak tanır.
            print(f"\nBir hata oluştu: {e}\n")  # Hata mesajı ve hata türünü kullanıcıya veriyoruz. ##

github_link="https://github.com/mehmetrehakogukkaya/youtube_downloader"
version = "1.0"  # Versiyon bilgisi belirtiyoruz.

print(f"Github link: {github_link}\n\nv{version}\n\n")  # github ve
# versiyon bilgisi yazrıdıyoruz.

time.sleep(2)  # Daha stabil bir kullanım için gecikme ekliyoruz(2sn)

print("Kütüphane kurulumları Tamamlandı...\n\n---------------------------------------------------------") #Kullanıcıya
                            # kütüphane işlemlerinin bittiğini ve programın kullanılabilir olduğunu bildiriyoruz.

time.sleep(2)  # Daha stabil bir kullanım için gecikme ekliyoruz(2sn)


while True:

    video_link = input("\n\nLütfen YouTube video bağlantısını girin: ")


    try:
        # YouTube video bağlantısını kullanarak bir YouTube nesnesi oluşturun
        yt = pytube.YouTube(video_link)

        # En yüksek çözünürlüğe sahip video akışını seçin
        stream = yt.streams.get_highest_resolution()

        # İndirme dizini (varsayılan olarak İndirilenler klasörü)
        default_download_path = os.path.expanduser("~/Downloads")

        # Video başlığı ve boyutunu alın
        video_title = yt.title
        video_size = round(stream.filesize / (1024 * 1024),2)  # Boyutu MB cinsinden hesapla

        # Kullanıcıya bilgi verin
        print(f"Şimdi indiriliyor: {video_title} ({video_size} MB)")

        # Videoyu indirin
        stream.download(output_path=default_download_path)

        # İndirme tamamlandı mesajı
        print(f"İndirme tamamlandı! Dosya kaydedildi: {os.path.join(default_download_path, video_title)}.mp4")
    except Exception as e:
        # Hata durumunda kullanıcıya hata mesajını gösterin
        print(f"Hata oluştu: {e}")

