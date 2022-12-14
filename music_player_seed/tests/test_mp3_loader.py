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

    
