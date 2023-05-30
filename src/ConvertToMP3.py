import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import *
from tkinter.ttk import Progressbar

class Converter:
    def __init__(self, window):
        self.window = window
        self.window.title("Conversor de Vídeo para MP3")
        self.window.geometry("400x200")

        self.label = tk.Label(window, text="Selecione o arquivo de vídeo:")
        self.label.pack(pady=10)

        self.button = tk.Button(window, text="Selecionar Arquivo", command=self.verify_resources)
        self.button.pack(pady=10)

        self.progress_bar = Progressbar(window, orient="horizontal", length=200, mode="indeterminate")

    def convert_to_mp3(self, filename):
        video = VideoFileClip(filename)
        mp3_filename = filename[:-4] + "mp3"
        video.audio.write_audiofile(mp3_filename, codec="mp3", bitrate="192k")
        video.close()
        return mp3_filename

    def show_progress(self):
        self.progress_bar.pack(pady=10)
        self.progress_bar.start()

    def hide_progress(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()

    def verify_resources(self):
        input_file = filedialog.askopenfilename(title="Selecione o arquivo de vídeo", filetypes=[("Arquivos de Vídeo", "*.mp4;*.3gpp")])
        if input_file:
            self.show_progress()
            self.window.update()  # Atualiza a janela para exibir a barra de progresso

            mp3_filename = self.convert_to_mp3(input_file)

            self.hide_progress()
            messagebox.showinfo("Conversão Concluída", f"O vídeo foi convertido para MP3 com sucesso!\nArquivo MP3 salvo como: {mp3_filename}")

# Cria a janela principal
window = tk.Tk()
converter = Converter(window)

# Inicia o loop principal da janela
window.mainloop()
