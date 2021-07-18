import re

class Data:
    @classmethod
    def find_date(cls, date):
        if len(date) == 10:
            if date[2] == '-' and date[5] == '-':
                day = int(date[0] + date[1])
                month = int(date[3] + date[4])
                year = int(date[6] + date[7] + date[8] + date[9])
                print(f'Day {day}, Month {month}, Year {year}')
            else:
                raise ValueError('ValueError: Wrong format!')
        else:
            raise ValueError('ValueError: Wrong format!')

    @staticmethod
    def valid_date(date):
        RE_DATE = re.compile(r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(\d{4})')
        assert RE_DATE.match(date), f'wrong date {date}'

Data.find_date('31-01-1990')
Data.valid_date('31-01-1990')
