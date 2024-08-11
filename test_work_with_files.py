import os
from zipfile import ZipFile
import csv
from pypdf import PdfReader
from openpyxl import load_workbook

TMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tmp')
ARCHIVE = os.path.join(TMP_DIR, 'archive.zip')
FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
files = ['file_example_XLSX_1000.xlsx', 'industry.csv', 'Тест план. Интернет-магазин скрыто.pdf']


def test_archive():

    # test csv
    with ZipFile(ARCHIVE) as zf:
        with zf.open('industry.csv') as csv_file:
            content = csv_file.read().decode()
            csvreader = list(csv.reader(content.splitlines()))
            first_row = csvreader[1]

            assert first_row[0] == 'Accounting/Finance'

    # test pdf
    with ZipFile(ARCHIVE) as zf:
        with zf.open('Тест план. Интернет-магазин скрыто.pdf') as pdf_file:
            content = PdfReader(pdf_file)
            page = content.pages[1]
            text = page.extract_text()

            assert 'История изменений' in text

    # test xlsx
    with ZipFile(ARCHIVE) as zf:
        with zf.open('file_example_XLSX_1000.xlsx') as xlsx_file:
            workbook = load_workbook(xlsx_file)
            sheet = workbook.active
            cell_content = sheet.cell(row=3, column=3).value

            assert cell_content == 'Hashimoto'
