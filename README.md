# Yt-dlp python GUI

GUI для yt-dlp на Python + DearPyGUI.

## Сборка

```bash
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt

pyinstaller --clean -n "yt-dlp-python-gui" -w -y -F -i="files\icon.ico" --add-data="files\CascadiaCode-Regular.otf:files" --add-data="files\icon.ico:files" .\main.py
```
