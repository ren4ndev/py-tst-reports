import pandas as pd


class SheetsConverter:
    def __init__(self, *args, **kwargs) -> None:
        self.sheets_directory = kwargs.get('sheets_directory')
        self.extracted_data = kwargs.get('extracted_data')
        self.duplicates = kwargs.get('duplicates')

    def _export_daily_sheets(self):
        """
            Para cada pdf extraído, cria uma planilha com
            os números de processos para o respectivo dia
        """
        columns = ['Processo Nº']
        for (sheet_date, data) in self.extracted_data:
            filename = 'TST {}.xlsx'.format(sheet_date)
            df = pd.DataFrame(list(data), columns=columns)
            df.to_excel(r'{}\{}'.format(
                    self.sheets_directory,
                    filename,
                )
            )

    def _export_duplicate_sheet(self):
        result_series = pd.concat(
            {key: pd.Series(values) for key, values in self.duplicates.items()}
        )
        result_series.to_excel(r'{}\{}'.format(
                self.sheets_directory,
                'duplicates.xlsx',
            )
        )

    def execute(self):
        self._export_daily_sheets()
        self._export_duplicate_sheet()
