from consts import DayNightDivision


class TimeConverter:
    MAX_DEGREES_VALUE = 360
    START_DAY_TIME = 0
    HALF_DAY_TIME = 12
    """
    Класс для конвертирования значений времени
    """

    @classmethod
    def angle_to_value(cls, max_val: int, cur_ang: float) -> int:
        """
        Конвертирует угол в значение

        :param max_val: Максимальное значение
        :param cur_ang: Угол
        """
        return round((cur_ang / cls.MAX_DEGREES_VALUE) * max_val)

    @classmethod
    def value_to_angle(cls, max_val: int, cur_val: int) -> float:
        """
        Конвертирует значение в угол

        :param max_val: Максимальное значение
        :param cur_val: Текущее значения
        """
        return cls.MAX_DEGREES_VALUE * cur_val / max_val

    @classmethod
    def get_diff_day_night_division(cls, day_night_division: DayNightDivision):
        """
        Возвращает время начала отсчета относительно старового положения стрелки

        :param day_night_division: Дневное/Ночное время суток
        """
        if day_night_division is DayNightDivision.AM:
            return cls.START_DAY_TIME
        else:
            return cls.HALF_DAY_TIME

    @classmethod
    def get_day_night_division(cls, hour: int):
        """
        Возвращает время дневное/ночное время суток

        :param hour: Часы
        """
        if hour < cls.HALF_DAY_TIME:
            return DayNightDivision.AM
        else:
            return DayNightDivision.PM
