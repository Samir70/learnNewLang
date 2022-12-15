import tkinter as tk
from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer
from player.mp3_loader import Mp3Loader

class GUI:
    def __init__(self, subprocess, file_sys, tag_reader):
        self.music_library = MusicLibrary()
        self.music_player = MusicPlayer(subprocess)
        self.mp3_loader = Mp3Loader(["data", "mp3s"], tag_reader, file_sys)

    def run(self):
        self.mp3_loader.get_files()
        for track in self.mp3_loader.file_data:
            # print("Found a track:")
            # print(track["title"])
            # print(track["artist"])
            # print(track["file"])
            # print("")
            self.music_library.add(Track(track["title"], track["artist"], track["file"]))
        print(f"added {len(self.mp3_loader.file_data)} tracks")
        self._showGUI()
    
    def _showGUI(self):
        print("in the show gui method")
        window = tk.Tk()
        headings = tk.Frame()
        headings.rowconfigure(0, minsize=50, weight=1)
        headings.columnconfigure([0, 1, 2], minsize=50, weight=1)
        lbl_artists = tk.Label(window, text="Artists")
        lbl_artists.grid(row=0, column=1)
        headings.pack()
        window.mainloop()


    def _add_track(self, title, artist, file):
        self.music_library.add(Track(title, artist, file))

    def _list_tracks(self, tracks):
        for idx, track in enumerate(tracks):
            self.console.print(
                f"{idx + 1}. {track}"
            )

    def _search_tracks(self):
        self.console.print("Search by:")
        self.console.print("  t: title")
        self.console.print("  a: artist")
        self.console.print("  f: file")
        self.console.print("  *: anything")
        choice = self.console.input("What do you want to search by? ")
        search_term = self.console.input("What do you want to search for? ").lower()
        attribute_name = {
            "t": "title",
            "a": "artist",
            "f": "file",
            "*": "all"
        }[choice]
        found = self.music_library.search(attribute_name, search_term)
        self._list_tracks(found)
        return found
        # if choice == "t":
        #     # DONE: Find tracks by title
        #     found = self.music_library.search(
        #         lambda track: search_term in track.title.lower())
        #     self._list_tracks(found)
        # elif choice == "a":
        #     # DONE: Find tracks by artist
        #     found = self.music_library.search(
        #         lambda track: search_term in track.artist.lower())
        #     self._list_tracks(found)
        # elif choice == "f":
        #     # DONE: Find tracks by file
        #     found = self.music_library.search(
        #         lambda track: search_term in track.file.lower())
        #     self._list_tracks(found)
        # elif choice == "*":
        #     # DONE: Find tracks by any field
        #     found = self.music_library.search(
        #         lambda track: search_term in track.title.lower() or search_term in track.artist.lower() or search_term in track.file.lower()
        #     )
        #     self._list_tracks(found)
        # else:
        #     self.console.print("No such field!")

    def _play_track(self):
        tracks = self._search_tracks()
        # tracks = self.music_library.all()
        track_id = int(self.console.input("Which do you want to play? ")) - 1
        if track_id >= 0 and track_id < len(tracks):
            track = tracks[track_id]
            t_str = f"{track}".split(" @")[0]
            self.console.print(f"Playing {t_str}...")
            self.music_player.play(track.file)
            self.console.print("Done.")
        else:
            self.console.print("No such track.")

    def _remove_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to delete? ")) - 1
        if self.music_library.remove(track_id):
            self.console.print("Deleted successfully.")
        else:
            self.console.print("No such track.")


