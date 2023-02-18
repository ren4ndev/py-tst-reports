from modules.dates.dates import Dates
from modules.scraper.notebook_scraper import NotebookScraper
from modules.process_extraction.process_extraction import ProcessExtraction
from modules.sheets_converter.sheets_converter import SheetsConverter
import os
import shutil


class MainScript:
    def __init__(self) -> None:
        self.pdf_path = r'{}\pdf'.format(os.getcwd())
        self.sheets_path = r'{}\sheets'.format(os.getcwd())

    def _make_sheets_directory(self):
        os.mkdir(self.sheets_path)

    def _clear_temporary_files(self):
        shutil.rmtree(self.pdf_path)

    def execute(self):
        dates_of_the_week = Dates.get_days_of_the_week()

        scraper = NotebookScraper(
            pdf_directory=self.pdf_path,
            start_date=dates_of_the_week[0],
            end_date=dates_of_the_week[-1]
        )
        scraper.execute()
        extracted_data = ProcessExtraction(
            pdf_directory=self.pdf_path
        ).execute()
        self._make_sheets_directory()
        SheetsConverter(
            sheets_directory=self.sheets_path,
            extracted_data=extracted_data
        ).execute()
        self._clear_temporary_files()


if __name__ == '__main__':
    MainScript().execute()
