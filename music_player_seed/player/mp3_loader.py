class Mp3Loader:
    def __init__(self, path, tag_reader, file_sys) -> None:
        self.file_names = []
        self.file_data = []
        self.path = file_sys.join(*path)
        self.file_sys = file_sys
        self.tag_reader = tag_reader

    def get_files(self):
        full_path = self.file_sys.join(self.file_sys.getcwd(), self.path)
        # print("getting files from: ", full_path)
        # for f in self.file_sys.listdir(full_path):
        #     print("file?", f, self.file_sys.is_file(self.file_sys.join(full_path, f)))
        self.file_names = [f for f in self.file_sys.listdir(full_path) if (
            f.endswith(".mp3") and self.file_sys.is_file(self.file_sys.join(full_path, f)))]
        if self.tag_reader == None:
            return
        for f in self.file_names:
            audio = self.tag_reader.load(self.file_sys.join(full_path, f))
            self.file_data.append({
                "title": audio.tag.title,
                "artist": audio.tag.artist,
                "file": self.file_sys.join(self.path, f)
            })
