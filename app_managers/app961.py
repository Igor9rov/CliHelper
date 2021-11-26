from app_managers.abstract_manager import AppManager
from constants import PATH_961
from utils import input_white_list_of_values


class App961Manager(AppManager):
    def __init__(self):
        super().__init__(config_field=PATH_961)
        self.mode = None
        self.cutting = None
        self.number_of_days = None
        self.conditions = None

    def get_input_parameters(self):
        self.mode = input_white_list_of_values("Выберите режим\n[0]-весь мир.,\n[1]-сев. полушарие.:\n", ["0", "1"])
        msg = "Выберите вырезку\n[0]-нет,\n[1]-восточное полушарие,\n[2]-западное полушарие:\n"
        self.cutting = input_white_list_of_values(msg, ["0", "1", "2"])
        self.number_of_days = input_white_list_of_values("Выберите кол-во дней [1]...[30]:\n",
                                                         list(map(str, range(1, 31))))
        self.conditions = input_white_list_of_values("Осадки или температура?\n", ["0", "1", "2"])

    @property
    def app_args(self):
        return [self.mode, self.cutting, self.number_of_days, self.conditions]
