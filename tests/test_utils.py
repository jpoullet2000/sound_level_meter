from slm.utils import str_to_datetime

def test_str_to_datetime():
    str_time = '20200816 164536'
    my_datetime = str_to_datetime(str_time)
    assert my_datetime.year == 2020
    assert my_datetime.day == 16
    assert my_datetime.hour == 16
    assert my_datetime.minute == 45
    assert my_datetime.second == 36