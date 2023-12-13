import pytest
from dir_check import dir_check
from pathlib import Path


# Check when the folder exists, by creating temporary folder, and removing it after the test.
def test_dir_check_exists():
    tempFolder = "folder_Tester"
    Path(tempFolder).mkdir(exist_ok=True)

    assert dir_check(tempFolder) is True

    Path(tempFolder).rmdir()


# Checks if folder does not exist, by creating a temporary folder variable.
def test_dir_check_not_exists():
    # Make sure fake directory does not exist
    tempFolder = "folder_Tester"
    if Path(tempFolder).exists():
        Path(tempFolder).rmdir()

    assert dir_check(tempFolder) is False
