from pytube import YouTube 
url = input("Digite o link do vídeo que deseja baixar: ")
video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download()
print("Download concluído!")