# Yt-dlp python GUI

![screenshot](readme_images/screenshot.png)

GUI для yt-dlp на Python + PySide6.

## Внимание!

Ни в коем случае не используйте данное приложение в корыстных целях. Автор не несёт никакой ответственности за ваши действия!

TL;DR: я не я, корова не моя :)

## Сборка

```bash
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt

pyinstaller --clean -n "yt-dlp-python-gui" -w -y -F -i="ui\icon.ico" --add-data="ui\icon.ico:ui" .\main.py
```

### Если нужен большой шрифт

Измените код в main.py:

```diff
- from ui_standart_size_main import Ui_MainWindow # Standard compact 9px ui
+ from ui_main import Ui_MainWindow # Big ui
```

```diff
- BIG_UI = False # Change to `False` if need standard compact 9px ui
+ BIG_UI = True # Change to `False` if need standard compact 9px ui
```

## Linux

Нужно поправить алгоритм поиска папки загрузки. Остальное всё кроссплатформенное.
