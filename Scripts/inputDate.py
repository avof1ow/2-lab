import datetime

import pandas as pd


def main(year: int, month: int, day: int) -> tuple[str, int]:
    """_summary_
        Принимаются день, месяц и год
        возвращается курс по заданной дате
    Args:
        year (int): год нужного курса
        month (int): месяц нужного курса
        day (int): день нужного курса

    Returns:
        tuple[str, int]: возвращает кортеж с датой и курсом рубля
    """
    df = pd.read_csv("CSV/dollar_course.csv", usecols=["rouble", "date"])
    date = datetime.date(year, month, day)
    rouble = df[df["date"] == str(date)]["rouble"].values[0]
    return (str(date), rouble)


if __name__ == "__main__":
    print(main(2022, 12, 27))
