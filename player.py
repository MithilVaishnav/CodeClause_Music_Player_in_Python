import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")

        self.current_track = ""
        self.paused = False

        # Create buttons
        self.btn_previous = tk.Button(self.window, text="Previous", command=self.play_previous)
        self.btn_previous.pack(side=tk.LEFT)

        self.btn_play = tk.Button(self.window, text="Play", command=self.play)
        self.btn_play.pack(side=tk.LEFT)

        self.btn_pause = tk.Button(self.window, text="Pause", command=self.pause)
        self.btn_pause.pack(side=tk.LEFT)

        self.btn_stop = tk.Button(self.window, text="Stop", command=self.stop)
        self.btn_stop.pack(side=tk.LEFT)

        self.btn_next = tk.Button(self.window, text="Next", command=self.play_next)
        self.btn_next.pack(side=tk.LEFT)

        self.btn_browse = tk.Button(self.window, text="Browse", command=self.browse_file)
        self.btn_browse.pack(side=tk.LEFT)

        self.window.mainloop()

    def play_previous(self):
        # Implement logic to play the previous track
        print("Playing previous track")

    def play(self):
        if self.current_track:
            if self.paused:
                mixer.music.unpause()
                self.paused = False
                print("Resumed playback")
            else:
                mixer.music.load(self.current_track)
                mixer.music.play()
                print("Playing track:", self.current_track)
        else:
            print("No track selected")

    def pause(self):
        if self.current_track:
            if not self.paused:
                mixer.music.pause()
                self.paused = True
                print("Paused playback")
            else:
                print("Playback already paused")
        else:
            print("No track selected")

    def stop(self):
        if self.current_track:
            mixer.music.stop()
            self.current_track = ""
            self.paused = False
            print("Stopped playback")
        else:
            print("No track selected")

    def play_next(self):
        # Implement logic to play the next track
        print("Playing next track")

    def browse_file(self):
        filetypes = (("Audio files", "*.mp3;*.wav"), ("All files", "*.*"))
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.current_track = filepath
            print("Selected track:", self.current_track)

if __name__ == "__main__":
    mixer.init()
    player = MusicPlayer()
    mixer.quit()
