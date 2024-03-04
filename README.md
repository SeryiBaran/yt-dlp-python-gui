# Yt-dlp python GUI

![screenshot](readme_images/screenshot.png)

GUI для yt-dlp на Python + PySide6.

## Внимание!

Ни в коем случае не используйте данное приложение в корыстных целях. Автор не несёт никакой ответственности за ваши действия!

TL;DR: я не я, корова не моя :)

## Скачать (Windows)

- [Стандартный интерфейс](https://github.com/SeryiBaran/yt-dlp-python-gui/releases/latest/download/yt-dlp-python-gui.exe)
- [Большой интерфейс](https://github.com/SeryiBaran/yt-dlp-python-gui/releases/latest/download/yt-dlp-python-gui__big_ui.exe)

## 1080 и FFmpeg

Для скачивания некоторых видео в 1080 нужен FFmpeg. Его можно установить через [Scoop](https://scoop.sh), с помощью [моего установщика](https://github.com/SeryiBaran/ffmpeg_installer) или по инструкциям в интернете.

## Сборка (PowerShell)

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt

pyside6-uic .\ui\main.ui -o .\ui_main.py && pyside6-uic .\ui\main__big_ui.ui -o .\ui_main__big_ui.py && pyside6-uic .\ui\about.ui -o .\ui_about.py

$ytdlppygui_version = Get-Content .\version.txt -Raw | ForEach-Object { $_.TrimEnd() }

# pyinstaller --clean -n "yt-dlp-python-gui__$($ytdlppygui_version)__big_ui" -w -y -F -i="ui\icon.ico" --add-data="ui\icon.ico:ui" .\main.py
pyinstaller --clean -n "yt-dlp-python-gui__$($ytdlppygui_version)" -w -y -F -i="ui\icon.ico" --add-data="ui\icon.ico:ui" .\main.py
```

## Если нужен большой шрифт

Измените код в main.py:

```diff

- BIG_UI = False  # Change to `True` if need big 14px ui
- from ui_main import Ui_MainWindow  # Standard compact 9px ui
+ BIG_UI = True  # Change to `True` if need big 14px ui
+ from ui_main__big_ui import Ui_MainWindow  # Big 14px ui
```

## Разработка

- Чтобы изменить версию, надо отредактировать её в `main.py` и `version.txt`

## Linux

Нужно поправить алгоритм поиска папки загрузки. Остальное всё кроссплатформенное.
