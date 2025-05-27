from unittest.mock import patch
from src.downloads import download_file
import gdown
import os 


def test_download_success(monkeypatch):
    def mock_download(url, output, quiet, use_cookies):
        with open(output, 'w') as f:
            f.write('test data')
        return True
    
    monkeypatch.setattr(gdown, 'download', mock_download)
    test_files = {"test1": "dummy_url"}
    assert download_file(test_files, "test_dir") is True
    os.remove("test_dir/test1.csv")
    os.rmdir("test_dir")
    
    
def test_download_failure(monkeypatch):
    def mock_download(url, output, quiet, use_cookies):
        raise Exception("Download error")
    
    monkeypatch.setattr(gdown, 'download', mock_download)
    test_files = {"test1": "dummy_url"}
    assert download_file(test_files) is False
    
    
def test_directory_creation():
    test_dir = "temp_test_dir"
    if os.path.exists(test_dir):
        os.rmdir(test_dir)
    
    test_files = {"test1": "dummy_url"}
    download_file(test_files, test_dir)
    assert os.path.exists(test_dir)
    os.rmdir(test_dir)
    
    
def test_empty_file_list():
    assert download_file({}) is True  # или False, в зависимости от ожидаемого поведения

def test_invalid_urls():
    test_files = {"test1": "invalid_url"}
    assert download_file(test_files) is False