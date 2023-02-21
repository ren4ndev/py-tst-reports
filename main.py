from modules.dates.dates import Dates
from modules.scraper.notebook_scraper import NotebookScraper
from modules.process_extraction.process_extraction import ProcessExtraction
from modules.sheets_converter.sheets_converter import SheetsConverter
import os
import io
import sys
import shutil


class MainScript:
    def __init__(self) -> None:
        self.pdf_path = r'{}\pdf'.format(os.getcwd())
        self.sheets_path = r'{}\sheets'.format(os.getcwd())

    def _make_sheets_directory(self):
        '''Cria diretório para armazenar planilhas'''
        os.mkdir(self.sheets_path)

    def _clear_temporary_files(self):
        """
            Remove diretório de arquivos temporários
            com dados a serem extraídos
        """
        shutil.rmtree(self.pdf_path)

    def execute(self):
        """
            Responsável por executar todos os métodos do script
            de acordo com os requisitos do projeto
        """
        buffer = io.StringIO()
        sys.stdout = buffer
        sys.stderr = buffer

        (week_start, week_end) = Dates.get_days_of_the_week()
        print(week_start)
        print(week_end)

        scraper = NotebookScraper(
            pdf_directory=self.pdf_path,
            start_date='13/02/2023',
            end_date='19/02/2023'
        )
        scraper.execute()
        (extracted_data, duplicates) = ProcessExtraction(
            pdf_directory=self.pdf_path
        ).execute()
        self._make_sheets_directory()
        SheetsConverter(
            sheets_directory=self.sheets_path,
            extracted_data=extracted_data,
            duplicates=duplicates
        ).execute()
        self._clear_temporary_files()


if __name__ == '__main__':
    MainScript().execute()
