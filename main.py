from app_managers.abstract_manager import AppManager
from app_managers.app51 import App51Manager
from app_managers.app961 import App961Manager
from utils import input_white_list_of_values


def run():
    app = get_app_from_user()
    app.operate()


def get_app_from_user():
    msg = "Выберите программу \n[0]-plkar51.exe (Значение по умолчанию), \n[1]-plkar961.exe:\n"
    user_input = input_white_list_of_values(msg, ["", "1", "0"])
    app_manager: AppManager = {"": App51Manager(), "0": App51Manager(), "1": App961Manager()}.get(user_input)
    return app_manager


if __name__ == '__main__':
    run()
