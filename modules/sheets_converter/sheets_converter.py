import pandas as pd


class SheetsConverter:
    def __init__(self, *args, **kwargs) -> None:
        self.sheets_directory = kwargs.get('sheets_directory')
        self.extracted_data = kwargs.get('extracted_data')

    def execute(self):
        """
            Para cada pdf extraído, cria uma planilha com
            os números de processos para o respectivo dia
        """
        columns = ['Processo Nº']
        for (filename, data) in self.extracted_data:
            print(filename)
            df = pd.DataFrame(list(data), columns=columns)
            df.to_excel(r'{}\{}'.format(
                    self.sheets_directory,
                    filename,
                )
            )
