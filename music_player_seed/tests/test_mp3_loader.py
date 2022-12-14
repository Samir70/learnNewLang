import unittest
from unittest.mock import Mock, MagicMock
from player.mp3_loader import Mp3Loader

class TestMp3Loader(unittest.TestCase):
    def test_constructs(self):
        file_sys = Mock()
        file_sys.join = MagicMock(return_value = "dummy/path")
        mLoad = Mp3Loader(["dummy", "path"], None, file_sys)
        # file_sys.join.assert_called_with("dummy", "path")
        self.assertEqual(mLoad.path, "dummy/path")

    def test_finds_files_in_folder(self):
        file_sys = Mock()
        file_sys.getcwd = MagicMock(return_value = "/Users/project/mLib")
        file_sys.join = MagicMock(return_value = "/Users/project/mLib/dummy/path")
        file_sys.is_file.side_effect = [True, False, True, True] 
        file_sys.listdir = MagicMock(return_value = ["file1.mp3", "subdir/", "file2.mp3", "file3.txt"])
        mLoad = Mp3Loader("dummy/path", None, file_sys)
        mLoad.get_files()
        file_sys.getcwd.assert_called
        file_sys.join.assert_called
        file_sys.is_file.assert_called
        file_sys.listdir.assert_called_with("/Users/project/mLib/dummy/path")
        self.assertEqual(mLoad.files, ["file1.mp3", "file2.mp3"])

