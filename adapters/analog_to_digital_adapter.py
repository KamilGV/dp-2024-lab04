from datetime import datetime
from interfaces import BaseDigitalClock, BaseAnalogClock
from consts import DayNightDivision


class AnalogToDigitalAdapter(BaseDigitalClock):
    """
    Адаптер для работы с AnalogClock через DigitalClock
    """

    def __init__(self, analog_clock: BaseAnalogClock):
        """
        Устанавливает аналоговую дату для адаптера

        :param analog_clock: Аналоговая дата

        """
        self.analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату

        :param date: дата в формате datetime
        """
        day_night_division = self._get_day_night_division(hour=date.hour)
        hour_angle = self._value_to_angle(
            max_val=12,
            cur_val=(
                date.hour
                if day_night_division is DayNightDivision.AM
                else date.hour - 12
            ),
        )
        minute_angle = self._value_to_angle(max_val=60, cur_val=date.minute)
        second_angle = self._value_to_angle(max_val=60, cur_val=date.second)
        self.analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=hour_angle,
            minute_angle=minute_angle,
            second_angle=second_angle,
            day_night_division=day_night_division,
        )

    def get_date_time(self) -> datetime:
        """
        Возвращает текущую дату в формате datetime
        """
        hour_dif = self._get_diff_day_night_division(
            day_night_division=self.analog_clock.day_night_division
        )
        hour_value = (
            self._angle_to_value(max_val=12, cur_ang=self.analog_clock.get_hour_angle())
            + hour_dif
        )
        minute_value = self._angle_to_value(
            max_val=60, cur_ang=self.analog_clock.get_minute_angle()
        )
        second_value = self._angle_to_value(
            max_val=60, cur_ang=self.analog_clock.get_second_angle()
        )
        return datetime(
            year=self.analog_clock.get_year(),
            month=self.analog_clock.get_month(),
            day=self.analog_clock.get_day(),
            hour=hour_value,
            minute=minute_value,
            second=second_value,
        )

    def _get_diff_day_night_division(self, day_night_division: DayNightDivision):
        """
        Возвращает разницу во времени

        :param day_night_division: Дневное/Ночное время суток
        """
        if day_night_division is DayNightDivision.AM:
            return 0
        else:
            return 12

    def _get_day_night_division(self, hour: int):
        """
        Возвращает время дневное/ночное время суток

        :param hour: Часы
        """
        if hour < 12:
            return DayNightDivision.AM
        else:
            return DayNightDivision.PM

    def _angle_to_value(self, max_val: int, cur_ang: float) -> int:
        """
        Конвертирует угол в значение

        :param max_val: Максимальное значение
        : param cur_ang: Угол
        """
        return round((cur_ang / 360) * max_val)

    def _value_to_angle(self, max_val: int, cur_val: int) -> float:
        """
        Конвертирует значение в угол

        :param max_val: Максимальное значение
        : param cur_ang: Текущее значения
        """
        return 360 * cur_val / max_val
