import tkinter as tk
from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer
from player.mp3_loader import Mp3Loader

class GUI:
    def __init__(self, subprocess, file_sys, tag_reader):
        self.music_library = MusicLibrary()
        self.music_player = MusicPlayer(subprocess)
        self.mp3_loader = Mp3Loader(["data", "mp3s"], tag_reader, file_sys)
        self.labels = { "artists": {}, "titles": {}}
        self.selected_artist = ""
        self.selected_track = ""

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
        self.window = tk.Tk()
        play_btn = tk.Button(self.window, text="PLAY", command=self._play_track)
        play_btn.pack()
        stop_btn = tk.Button(self.window, text="STOP", command=self._stop_playback)
        stop_btn.pack()
        self.headings = tk.Frame()
        self.headings.pack()
        self.headings.rowconfigure(0, minsize=50, weight=1)
        self.headings.columnconfigure(0, minsize=50, weight=1)
        self.headings.columnconfigure(1, minsize=300, weight=3)
        lbl_artist = tk.Label(self.headings, text="Artists")
        lbl_artist.grid(row=0, column=0)
        lbl_title = tk.Label(self.headings, text="Track title")
        lbl_title.grid(row=0, column=1)

        tracks = self.music_library.all()
        artists = sorted([" All", *list(set([t.artist for t in tracks]))])
        r = 1
        for artist in artists:
            temp_lbl = tk.Label(self.headings, text=f"{artist}")
            temp_lbl.bind("<Button-1>", self._artist_clicked)
            temp_lbl.grid(row=r, column=0)
            self.labels["artists"][artist] = temp_lbl
            r += 1
        self._highlight("artists", " All", "#5555FF")
        self.selected_artist = " All"
        self._list_tracks(tracks)
        self.window.mainloop()

    def _artist_clicked(self, event):
        name = event.widget["text"]
        self._highlight("artists", self.selected_artist, "systemWindowBackgroundColor")
        self.selected_artist = name
        self.selected_track = ""
        self._highlight("artists", name, "#5555FF")
        if name == " All":
            tracks = self.music_library.all()
        else:
            tracks = [track for track in self.music_library.all() if track.artist == name]
        self._list_tracks(tracks)

    def _title_clicked(self, event):
        name = event.widget["text"]
        if self.selected_track != "":
            self._highlight("titles", self.selected_track, "systemWindowBackgroundColor")
        self._highlight("titles", name, "#5555FF")
        self.selected_track = name

    def _add_track(self, title, artist, file):
        self.music_library.add(Track(title, artist, file))

    def _highlight(self, type, name, colour):
        self.labels[type][name].configure(bg=colour)

    def _list_tracks(self, tracks):
        for title in self.labels["titles"]:
            self.labels["titles"][title].destroy()
        r = 0
        for track in tracks:
            r += 1
            title_lbl = tk.Label(self.headings, text=f"{track.title}")
            title_lbl.bind("<Button-1>", self._title_clicked)
            title_lbl.grid(row=r, column= 1)
            self.labels["titles"][track.title] = title_lbl

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
        if self.selected_track == "":
            track_name = list(self.labels["titles"].keys())[0]
        else:
            track_name = self.selected_track
        print(f"Trying to play{track_name}")
        tracks = self.music_library.search("title", track_name.lower())
        print(tracks)
        if tracks[0] == None:
            print(f"?????? didn't find a track to play {track_name}")
            return
        else:
            self.music_player.play(tracks[0].file)

    def _stop_playback(self):
        pass


