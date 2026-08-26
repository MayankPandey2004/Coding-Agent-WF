import os
from pathlib import Path
import pytest

from file_utils import get_total_txt_size

def create_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    return path

def test_get_total_txt_size(tmp_path: Path):
    # Create .txt files with known sizes
    file1 = create_file(tmp_path / 'a.txt', 'hello')  # 5 bytes
    file2 = create_file(tmp_path / 'subdir' / 'b.txt', 'world!')  # 6 bytes
    # Create a non-txt file
    create_file(tmp_path / 'c.md', 'markdown')
    # Create an empty txt file
    create_file(tmp_path / 'empty.txt', '')

    expected_size = (
        file1.stat().st_size +
        file2.stat().st_size +
        (tmp_path / 'empty.txt').stat().st_size
    )

    assert get_total_txt_size(tmp_path) == expected_size
