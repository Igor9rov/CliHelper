from utils import resolve_path

CONFIG_FILE_NAME = "config.ini"

SECTION = "PATHS"
PATH_51 = "PATH_51"
PATH_961 = "PATH_961"

CONFIG_EXAMPLE = rf"""
Пример содержимого файла {CONFIG_FILE_NAME}:

[{SECTION}]
# Здесь должны быть описаны абсолютные или относительные пути к программам plkar51.exe и plkar961.exe
{PATH_51} = cli_apps\plkar51.exe
{PATH_961} = cli_apps\plkar961.exe"
"""

ID_APP_51 = "51"
ID_APP_961 = "961"
ID_NOT_CORRECT = "-1"





