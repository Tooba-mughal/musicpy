import tkinter as tk
from tkinter import filedialog
import pygame
class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Music Player")
        self.geometry("300x200")

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        # Load button
        load_button = tk.Button(self, text="Load Music", command=self.load_music)
        load_button.pack(pady=20)

        # Play button
        play_button = tk.Button(self, text="Play", command=self.play_music)
        play_button.pack(pady=10)

        # Stop button
        stop_button = tk.Button(self, text="Stop", command=self.stop_music)
        stop_button.pack(pady=10)

    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])

    def play_music(self):
        if hasattr(self, 'music_file'):
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()