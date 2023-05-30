
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import pytube
from tkinter.ttk import Progressbar
from threading import Thread

# Função para fazer o download do vídeo do YouTube
def download_video():
    url = url_entry.get()
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    save_path = filedialog.askdirectory(title="Selecione a pasta de salvamento")
    if save_path:
        download_button.config(state="disabled")
        status_label.config(text="Baixando vídeo...")
        
        progress_bar['value'] = 0
        progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        
        def download():
            video.download(output_path=save_path)
            messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!")
            status_label.config(text="")
            download_button.config(state="normal")
            progress_bar.grid_forget()
        
        Thread(target=download).start()


# Cria a janela principal
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("400x150")

# Cria os widgets
url_label = tk.Label(window, text="URL do vídeo:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

url_entry = tk.Entry(window)
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

download_button = tk.Button(window, text="Baixar Vídeo", command=download_video)
download_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

status_label = tk.Label(window, text="", font=("Arial", 12))
status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

progress_bar = Progressbar(window, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
progress_bar.grid_forget()

footer_label = tk.Label(window, text="Criado por Kenny Vargas", font=("Arial", 8))
footer_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Inicia o loop principal da janela
window.mainloop()
