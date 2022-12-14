import unittest
from unittest.mock import Mock, MagicMock
from player.mp3_loader import Mp3Loader


class TestMp3Loader(unittest.TestCase):
    def test_constructs(self):
        file_sys = Mock()
        file_sys.join = MagicMock(return_value="dummy/path")
        mLoad = Mp3Loader(["dummy", "path"], None, file_sys)
        file_sys.join.assert_called_with("dummy", "path")
        self.assertEqual(mLoad.path, "dummy/path")

    def test_finds_files_in_folder(self):
        file_sys = Mock()
        file_sys.getcwd = MagicMock(return_value="/Users/project/mLib")
        file_sys.join = MagicMock(return_value="/Users/project/mLib/dummy/path")
        file_sys.is_file.side_effect = [True, True, False]
        file_sys.listdir = MagicMock(
            return_value=["file1.mp3", "subdir/", "file2.mp3", ".mp3"])
        mLoad = Mp3Loader(["dummy", "path"], None, file_sys)
        mLoad.get_files()
        file_sys.getcwd.assert_called
        file_sys.join.assert_called
        file_sys.is_file.assert_called
        file_sys.listdir.assert_called_with("/Users/project/mLib/dummy/path")
        self.assertEqual(mLoad.file_names, ["file1.mp3", "file2.mp3"])

    def test_gets_file_data(self):
        file_sys = Mock()
        file_sys.listdir = MagicMock(
            return_value=["file1.mp3", "subdir/", "file2.mp3", ".mp3"])
        file_sys.is_file.side_effect = [True, True, False]
        file_sys.join.side_effect = [
            "used in __init__/",
            "should be from getcwd/",
            "to access first file/",
            "dummy/path/file1.mp3",
            "to access second file/",
            "dummy/path/file2.mp3"
        ]
        fake_eyed3 = Mock()
        fake_eyed3.load.side_effect = [
            {"tag": {"title": "title1", "artist": "artist1"}},
            {"tag": {"title": "title2", "artist": "artist2"}},
        ]
        mLoad = Mp3Loader(["dummy", "path"], fake_eyed3, file_sys)
        mLoad.get_files()
        fake_eyed3.load.assert_called
        self.assertEqual(mLoad.file_data, [
            {"title": "title1", "artist": "artist1", "file": "dummy/path/file1.mp3"},
            {"title": "title2", "artist": "artist2", "file": "dummy/path/file2.mp3"}
        ])
