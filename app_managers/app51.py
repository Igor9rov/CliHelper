from app_managers.abstract_manager import AppManager
from constants import PATH_51
from utils import input_white_list_of_values


class App51Manager(AppManager):
    def __init__(self):
        super().__init__(config_field=PATH_51)
        self.map = None
        self.scale = None
        self.condition = None
        self.with_circle = None
        self.with_tide = None

    @property
    def app_args(self):
        return [self.map, self.scale, self.condition, self.with_circle, self.with_tide]

    def get_input_parameters(self):
        self.map = input_white_list_of_values("Выберите карту \n[1]-геогр., \n[2]-админ., \n[3]-вместе:\n",
                                              ["1", "2", "3"])
        self.scale = input_white_list_of_values("Выберите масштаб \n[1], \n[2]:\n", ["1", "2"])
        self.condition = input_white_list_of_values("Осадки,температура,сток рек [0],[1],[2],[3])?\n",
                                                    ["0", "1", "2", "3"])
        self.with_circle = input_white_list_of_values("С крутом? \n[0]-С кругом,\n[1]-Без круга:\n", ["0", "1"])
        self.with_tide = input_white_list_of_values("С приливом? \n[0]-С приливом,\n[1]-Без прилива:\n", ["0", "1"])
