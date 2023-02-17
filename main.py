from modules.dates.dates import Dates
from modules.scraper.notebook_scraper import NotebookScraper
from modules.process_extraction.process_extraction import ProcessExtraction
import os


class MainScript:
    def __init__(self) -> None:
        self.pdf_path = r'{}\pdf'.format(os.getcwd())

    def execute(self):
        dates_of_the_week = Dates.get_days_of_the_week()

        scraper = NotebookScraper(
            pdf_directory=self.pdf_path,
            start_date=dates_of_the_week[0],
            end_date=dates_of_the_week[-1]
        )
        scraper.execute()
        ProcessExtraction(
            pdf_directory=self.pdf_path
        ).execute()


if __name__ == '__main__':
    MainScript().execute()
