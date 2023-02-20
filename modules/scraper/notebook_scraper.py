from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os


class NotebookScraper():
    def __init__(self, *args, **kwargs):
        """
            Instancia driver para raspagem de dados
            definindo o path de onde os downloads devem ser armazenados,
            assim como a url onde a raspagem de dados deve ser feita.
        """
        self.download_path = kwargs.get('pdf_directory')
        options = Options()
        prefs = {'download.default_directory': self.download_path}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        self.url = 'https://dejt.jt.jus.br/dejt/f/n/diariocon'
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')

    def _filter_notebooks(self):
        """
            Realiza o filtro de acordo com as datas de início
            e fim da semana passadas para a classe
        """
        start_date_input = self.driver.find_element(
            By.ID, 'corpo:formulario:dataIni'
        )
        end_date_input = self.driver.find_element(
            By.ID, 'corpo:formulario:dataFim'
        )

        start_date_input.clear()
        self.driver.execute_script(
            f"arguments[0].value = '{self.start_date}';",
            start_date_input
        )
        start_date_input.click()

        end_date_input.clear()
        self.driver.execute_script(
            f"arguments[0].value = '{self.end_date}';",
            end_date_input
        )
        end_date_input.click()

        select_notebook_input = Select(
            self.driver.find_element(By.ID, 'corpo:formulario:tipoCaderno')
        )
        select_notebook_input.select_by_value('1')

        select_court_input = Select(
            self.driver.find_element(By.ID, 'corpo:formulario:tribunal')
        )
        select_court_input.select_by_value('0')

        search_button = self.driver.find_element(
            By.ID, 'corpo:formulario:botaoAcaoPesquisar'
        )
        search_button.click()

    def _download_notebooks(self):
        """
            Realiza o download dos cadernos em resultado
            do filtro realizado
        """
        download_buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            '.bt.af_commandButton'
        )
        for button in download_buttons:
            button.click()

        while len([
                f for f in os.listdir(self.download_path) if f.endswith('.pdf')
                ]) < len(download_buttons):
            sleep(1)

    def execute(self):
        """
            Chama os métodos de filtro e download
            da classe
        """
        self.driver.implicitly_wait(1)
        self.driver.get(self.url)
        self._filter_notebooks()
        self._download_notebooks()

        self.driver.close()
