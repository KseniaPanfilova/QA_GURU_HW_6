import pytest
import os
from zipfile import ZipFile
import shutil

TMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
ARCHIVE = os.path.join(TMP_DIR, 'archive.zip')
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
files = ['file_example_XLSX_1000.xlsx', 'industry.csv', 'Тест план. Интернет-магазин скрыто.pdf']


@pytest.fixture(scope="function", autouse=True)
def create_archive():
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    with ZipFile(ARCHIVE, 'w') as zf:
        for file in files:
            add_file = os.path.join(FILES_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(TMP_DIR)
