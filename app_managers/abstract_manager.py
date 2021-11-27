import os
import subprocess
from abc import abstractmethod, ABC
from configparser import NoOptionError, NoSectionError, ConfigParser
from datetime import date

import pandas as pd

from constants import CONFIG_EXAMPLE, SECTION, CONFIG_FILE_NAME
from utils import wait_input_from_user, input_white_list_of_values, resolve_path


class AppManager(ABC):
    def __init__(self, config_field):
        self.config_field = config_field
        self.date_from = None
        self.date_to = None
        self.hour = None
        self.minute = None
        self.app_path = None

    def operate(self):
        self.get_app_path()
        self.get_period()
        self.get_hour()
        self.get_minute()
        self.get_input_parameters()
        self.start_app_for_each_day_in_period()

    def get_app_path(self):
        try:
            self.get_path_from_config()
        except NoOptionError as error:
            print("Нет корректных настроек для пути файлов в файле конфигурации", CONFIG_EXAMPLE)
            wait_input_from_user()
            raise error
        except NoSectionError as error:
            print("Нет конфигурационного файла в текущей директории или он описан неверно", CONFIG_EXAMPLE)
            wait_input_from_user()
            raise error

    def get_path_from_config(self):
        config = ConfigParser()
        config.read(resolve_path(CONFIG_FILE_NAME))
        self.app_path = resolve_path(config.get(SECTION, self.config_field))
        if not os.path.isfile(self.app_path):
            print(f"Не обнаружено исполняемого файла {self.app_path}. Проверьте файл конфигурации", CONFIG_EXAMPLE)
            wait_input_from_user()
            raise ValueError("Проверьте файл конфигурации")

    def get_period(self):
        self.date_from = self.ger_date_from_user("начало периода")
        self.date_to = self.ger_date_from_user("конец периода")

        time_delta = self.date_to - self.date_from
        if time_delta.days <= 0:
            print(f"Некорректный ввод периода времени. "
                  f"Конец периода {self.date_to} раньше или равен началу {self.date_from}.\n")
            self.get_period()

    def ger_date_from_user(self, period):
        user_input = input(f"Введите {period} в формате год, месяц, день [2020 01 01]:").split(" ")
        try:
            year, month, day = user_input
            date_from_user = date(year=int(year), month=int(month), day=int(day))
            return date_from_user
        except (TypeError, ValueError):
            print("Ошибка в преобразовании даты. Введите дату в корректном формате.\n")
            return self.ger_date_from_user(period)

    def get_minute(self):
        self.minute = input_white_list_of_values("Выберите минуту [0]...[59]:\n", list(map(str, range(60))))

    def get_hour(self):
        self.hour = input_white_list_of_values("Выберите час [0]...[23]:\n", list(map(str, range(24))))

    @abstractmethod
    def get_input_parameters(self):
        pass

    def start_app_for_each_day_in_period(self):
        date_range = pd.date_range(self.date_from, self.date_to)
        for day_date in date_range:
            date_string = f"{day_date.year} {day_date.month} {day_date.day} {self.hour} {self.minute}"
            input_string = "\n".join([date_string, *self.app_args])
            subprocess.run(self.app_path, encoding="utf8", input=input_string)
        input("Процессы отработали успешно. Для выхода нажмите Enter.")

    @property
    @abstractmethod
    def app_args(self):
        pass
