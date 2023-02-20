import fitz
from pathlib import Path
import re


class ProcessExtraction:
    def __init__(self, *args, **kwargs) -> None:
        self.pdf_directory = kwargs.get('pdf_directory')

    def _extract(self, path):
        """
            Recebe um arquivo pdf e retorna todas
            ocorrências de números de processos no
            arquivo.
        """
        doc = fitz.open(path)
        processes = []
        for page in doc.pages():
            frame = page.search_for('Processo Nº')
            for line in frame:
                line.x1 = 600
                process = page.get_textbox(line)
                if 'Processo Nº' in process:
                    processes.append(process.split()[-1])
        return set(processes)

    def _extract_duplicates(self, extracted_data):
        seen = set()
        repeated = set()
        for (sheet_date, processes) in extracted_data:
            for item in processes:
                if item in seen:
                    repeated.add(item)
                else:
                    seen.add(item)

        duplicates_dict = dict()
        for (sheet_date, processes) in extracted_data:
            for item in processes:
                if item in repeated:
                    if item in duplicates_dict:
                        duplicates_dict[item].append(sheet_date)
                    else:
                        duplicates_dict[item] = [sheet_date]
        return duplicates_dict

    def _extract_data(self):
        """
            Executa processo de extração dos números
            de processos de cada arquivo pdf no
            diretório de arquivos pdf baixados
        """
        extracted_data = []
        for path in Path(self.pdf_directory).iterdir():
            print('Procurando ocorrências no arquivo {}'.format(
                path.parts[-1])
            )
            pdf_filename = re.split(r'[_.]', path.parts[-1])
            sheet_date = '{}-{}-{}'.format(
                pdf_filename[-4],
                pdf_filename[-3],
                pdf_filename[-2]
            )
            processes = self._extract(path)
            extracted_data.append((sheet_date, processes))
        return extracted_data

    def execute(self):
        extracted_data = self._extract_data()
        duplicates = self._extract_duplicates(extracted_data)

        return (extracted_data, duplicates)
