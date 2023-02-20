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
        return processes

    def execute(self):
        """
            Executa processo de extração dos números
            de processos de cada arquivo pdf no
            diretório de arquivos pdf baixados
        """
        extracted_data = []
        for path in Path(self.pdf_directory).iterdir():
            print(re.split(r'[_.]', path.parts[-1]))
            pdf_filename = re.split(r'[_.]', path.parts[-1])
            sheet_filename = 'TST {}-{}-{}.xlsx'.format(
                pdf_filename[-4],
                pdf_filename[-3],
                pdf_filename[-2]
            )
            processes = self._extract(path)
            extracted_data.append((sheet_filename, processes))
        return extracted_data
