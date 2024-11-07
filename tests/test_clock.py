import random
from datetime import datetime, timedelta

from adapters import AnalogToDigitalAdapter
from clocks import AnalogClock

import pytest


@pytest.mark.repeat(10)
def test_convert():
    """
    Проверка конвертации случайных дат из digital в analog, и обратно.
    """
    # Получаем случайную дату
    start_date = datetime(1800, 1, 1)

    random_sec = random.randint(0, 10000000)
    random_date = start_date + timedelta(seconds=random_sec)
    # random_date = datetime(1800, 4, 7, 23, 7, 3)

    # Создаём адаптер
    adapter = AnalogToDigitalAdapter(AnalogClock())

    adapter.set_date_time(random_date)
    return_date = adapter.get_date_time()

    assert return_date == random_date
