# CliHelper
Проект помогает запускать исполняемые файлы в цикле с предустановленными параметрами.

## Запуск с помошью интерпретатора Python
Также есть возможность запустить файл с помощью Python.
Необходим Python версии 3.x
Предварительно необходимо создать и активировать виртуальное окружение.
[Подробнее по ссылке](https://docs.python.org/3/tutorial/venv.html)
```bash
python -m venv venv
venv\Scripts\activate.bat
```
установить зависимости
```bash
pip install -r path/to/requirements.txt
```
Далее запуск
```bash
python -m main.py
```

## Создание исполняемого файла из исходников

Для этого используется pyinstaller.
Также необходимо создать виртуальное окружение и установить зависимости.
Далее необходимо выполнить команду:
```bash
pyi-makespec --name plkar_helper main.py
```
Запуск создания exe файла
```bash
pyinstaller --clean plkar_helper.spec
```

