# Yt-dlp python GUI

![screenshot](readme_images/screenshot.png)

GUI для yt-dlp на Python + PySide6.

## Внимание!

1. Ни в коем случае не используйте данное приложение в корыстных целях. Автор не несёт никакой ответственности за ваши действия!
2. Для скачивания видео ТРЕБУЕТСЯ FFmpeg. Его можно установить через [Scoop](https://scoop.sh), с помощью [моего полурабочего установщика](https://github.com/SeryiBaran/ffmpeg_installer) или по инструкциям в интернете.

## Скачать (Windows)

- [Стандартный интерфейс](https://github.com/SeryiBaran/yt-dlp-python-gui/releases/latest/download/yt-dlp-python-gui.exe)
- [Большой интерфейс](https://github.com/SeryiBaran/yt-dlp-python-gui/releases/latest/download/yt-dlp-python-gui__big_ui.exe)

## Сборка (PowerShell)

```powershell
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt

pyside6-uic .\ui\main.ui -o .\ui_main.py && pyside6-uic .\ui\about.ui -o .\ui_about.py
$versions = Get-Content .\versions.json -Raw | ConvertFrom-Json

pyinstaller --clean -n "yt-dlp-python-gui__$($versions.app)__$($versions.yt_dlp)" -w -y -F -i="ui\icon.ico" --add-data="ui\icon.ico:ui" --add-data="versions.json:." .\main.py
```

## Разработка

- Чтобы изменить версию, надо отредактировать её в `versions.json`

## Linux

Нужно поправить алгоритм поиска папки загрузки `download_directory`. Остальное всё кроссплатформенное.
