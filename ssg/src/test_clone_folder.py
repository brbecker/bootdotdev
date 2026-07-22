import unittest
from pathlib import Path
import tempfile

try:
    from .clone_folder import copy_directory, clone_folder
except Exception:
    from clone_folder import copy_directory, clone_folder


class TestCloneFolder(unittest.TestCase):
    def setUp(self) -> None:
        self._td = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self._td.name)

    def tearDown(self) -> None:
        self._td.cleanup()

    def _write_file(self, p: Path, content: str = "data") -> None:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)

    def test_copy_directory_copies_files_and_dirs(self):
        src = self.tmp_path / "src"
        src.mkdir()
        self._write_file(src / "file1.txt", "hello")
        self._write_file(src / "sub" / "file2.txt", "world")

        tgt = self.tmp_path / "target"
        copy_directory(str(src), str(tgt))

        self.assertTrue((tgt / "file1.txt").exists())
        self.assertTrue((tgt / "sub" / "file2.txt").exists())
        self.assertEqual((tgt / "file1.txt").read_text(), "hello")
        self.assertEqual((tgt / "sub" / "file2.txt").read_text(), "world")

    def test_clone_folder_clears_target_before_copy(self):
        src = self.tmp_path / "src"
        src.mkdir()
        self._write_file(src / "a.txt", "A")

        tgt = self.tmp_path / "target"
        tgt.mkdir()
        self._write_file(tgt / "old.txt", "OLD")

        clone_folder(str(src), str(tgt))

        self.assertFalse((tgt / "old.txt").exists())
        self.assertTrue((tgt / "a.txt").exists())
        self.assertEqual((tgt / "a.txt").read_text(), "A")


if __name__ == "__main__":
    unittest.main()
