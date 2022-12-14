class Mp3Loader:
    def __init__(self, path, tag_reader, file_sys) -> None:
        self.files = []
        self.path = file_sys.join(*path)
        self.file_sys = file_sys

    def get_files(self):
        full_path = self.file_sys.join(self.file_sys.getcwd(), self.path)
        self.files = [f for f in self.file_sys.listdir(full_path) if f.endswith(".mp3")]