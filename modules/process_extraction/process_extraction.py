import fitz
from pathlib import Path
import json
import re


class ProcessExtraction:
    def __init__(self, *args, **kwargs) -> None:
        self.pdf_directory = kwargs.get('pdf_directory')

    def _extract(self, path):
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
        notebooks_dict = dict()
        for path in Path(self.pdf_directory).iterdir():
            print(re.split(r'[_.]', path.parts[-1]))
            pdf_filename = re.split(r'[_.]', path.parts[-1])
            sheet_filename = 'TST {}/{}/{}.xlsx'.format(
                pdf_filename[-4],
                pdf_filename[-3],
                pdf_filename[-2]
            )
            print(sheet_filename)

            value = self._extract(path)
            notebooks_dict.update({sheet_filename: value})

        with open('result.json', 'w') as file:
            json.dump(notebooks_dict, file)
