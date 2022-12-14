class Mp3Loader:
    def __init__(self, path, tag_reader, file_sys) -> None:
        self.files = []
        self.path = file_sys.join(*path)