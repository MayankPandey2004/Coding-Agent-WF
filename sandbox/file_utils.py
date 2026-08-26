from pathlib import Path

def get_total_txt_size(directory: str | Path) -> int:
    """Return the total size in bytes of all *.txt files under *directory* recursively.

    Parameters
    ----------
    directory: str or Path
        The root directory to search.

    Returns
    -------
    int
        Sum of file sizes in bytes.
    """
    root = Path(directory)
    total = 0
    for txt_file in root.rglob('*.txt'):
        if txt_file.is_file():
            total += txt_file.stat().st_size
    return total
