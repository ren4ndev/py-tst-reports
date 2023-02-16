from datetime import date, timedelta


class Dates:
    def __init__():
        pass

    @classmethod
    def get_days_of_the_week(self):
        today = date.today()
        start_of_the_week = today - timedelta(days=today.weekday())

        days_of_the_week = []
        for dates_to_add in range(7):
            new_date = start_of_the_week + timedelta(days=dates_to_add)
            days_of_the_week.append(new_date.strftime('%d/%m/%y'))

        return days_of_the_week
