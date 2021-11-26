import os
import sys


def wait_input_from_user():
    """
    Нужна для того, чтобы пользователь смог увидеть сообщение об ошибке
    """
    input("Для выхода нажмите Enter")


def input_white_list_of_values(msg, white_list):
    user_input = input(msg)
    if user_input not in white_list:
        print(f"Допустимый список значений: {white_list}. Повторите ввод ещё раз, пожалуйста.")
        return input_white_list_of_values(msg, white_list)
    return user_input


def resolve_path(path):
    """Нужна чтобы нормально работать с путями в приложении"""
    if getattr(sys, "frozen", False) and hasattr(sys, '_MEIPASS'):
        # If the 'frozen' flag is set, we are in bundled-app mode!
        resolved_path = os.path.join(os.path.dirname(sys.executable), path)
    else:
        # Normal development mode. Use os.getcwd() or __file__ as appropriate in your case...
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path
