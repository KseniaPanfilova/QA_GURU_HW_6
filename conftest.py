import pytest
from zipfile import ZipFile
import shutil
from constants import *


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
