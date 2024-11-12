from datetime import datetime
from interfaces import BaseDigitalClock, BaseAnalogClock
from consts import DayNightDivision
from tools import TimeConverter


class AnalogToDigitalAdapter(BaseDigitalClock):
    """
    Адаптер для работы с AnalogClock через DigitalClock
    """

    def __init__(self, analog_clock: BaseAnalogClock):
        """
        Устанавливает аналоговую дату для адаптера

        :param analog_clock: Аналоговая дата

        """
        self._analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату

        :param date: дата в формате datetime
        """
        day_night_division = TimeConverter.get_day_night_division(hour=date.hour)
        hour_angle = TimeConverter.value_to_angle(
            max_val=12,
            cur_val=(
                date.hour
                if day_night_division is DayNightDivision.AM
                else date.hour - 12
            ),
        )
        minute_angle = TimeConverter.value_to_angle(max_val=60, cur_val=date.minute)
        second_angle = TimeConverter.value_to_angle(max_val=60, cur_val=date.second)
        self._analog_clock.set_date_time(
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
        hour_dif = TimeConverter.get_diff_day_night_division(
            day_night_division=self._analog_clock.day_night_division
        )
        hour_value = (
            TimeConverter.angle_to_value(
                max_val=12, cur_ang=self._analog_clock.get_hour_angle()
            )
            + hour_dif
        )
        minute_value = TimeConverter.angle_to_value(
            max_val=60, cur_ang=self._analog_clock.get_minute_angle()
        )
        second_value = TimeConverter.angle_to_value(
            max_val=60, cur_ang=self._analog_clock.get_second_angle()
        )
        return datetime(
            year=self._analog_clock.get_year(),
            month=self._analog_clock.get_month(),
            day=self._analog_clock.get_day(),
            hour=hour_value,
            minute=minute_value,
            second=second_value,
        )
