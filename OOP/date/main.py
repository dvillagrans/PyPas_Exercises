# TODO
class Date:
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    WEEKDAYS = ['DOMINGO', 'LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO']
    MONTHS = ['', 'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 
              'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']

    def __init__(self, day: int, month: int, year: int):
        self.year = 1900 if year < 1900 or year > 2050 else year
        self.month = 1 if month < 1 or month > 12 else month
        max_days = self.get_days_in_month(self.month, self.year)
        self.day = 1 if day < 1 or day > max_days else day

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def get_days_in_month(month: int, year: int) -> int:
        if month == 2 and Date.is_leap_year(year):
            return 29
        return Date.DAYS_IN_MONTH[month]

    def get_delta_days(self) -> int:
        total_days = 0
        # Calcular días de años completos
        for year in range(1900, self.year):
            total_days += 366 if self.is_leap_year(year) else 365
        
        # Añadir días de meses completos del año actual
        for month in range(1, self.month):
            total_days += self.get_days_in_month(month, self.year)
        
        # Añadir días del mes actual
        return total_days + self.day - 1

    @property
    def weekday(self) -> int:
        # 1-1-1900 fue lunes (1)
        return (self.get_delta_days() + 1) % 7

    @property
    def is_weekend(self) -> bool:
        return self.weekday in [0, 6]  # Domingo (0) o Sábado (6)

    @property
    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

    def __str__(self) -> str:
        return f"{self.WEEKDAYS[self.weekday]} {self.day} DE {self.MONTHS[self.month]} DE {self.year}"

    def __add__(self, days_to_add: int) -> 'Date':
        total_days = self.get_delta_days() + days_to_add
        year = 1900
        while True:
            days_in_year = 366 if self.is_leap_year(year) else 365
            if total_days < days_in_year:
                break
            total_days -= days_in_year
            year += 1

        month = 1
        while total_days >= self.get_days_in_month(month, year):
            total_days -= self.get_days_in_month(month, year)
            month += 1

        return Date(total_days + 1, month, year)

    def __sub__(self, other: 'Date|int') -> 'Date|int':
        if isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()
        elif isinstance(other, int):
            return self + (-other)
        raise TypeError("Operando no soportado")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return (self.day == other.day and 
                self.month == other.month and 
                self.year == other.year)

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.get_delta_days() > other.get_delta_days()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.get_delta_days() < other.get_delta_days()