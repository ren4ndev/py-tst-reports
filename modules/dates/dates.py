from datetime import date, timedelta


class Dates:
    def __init__():
        pass

    @classmethod
    def get_days_of_the_week(cls):
        """
            Método responsável por retornar dias da
            semana corrente.
            Obs.: pode ser refatorado para utilizar pandas
        """
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        return (week_start.strftime('%d/%m/%Y'), week_end.strftime('%d/%m/%Y'))
