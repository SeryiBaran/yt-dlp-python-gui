import os
import sys
from pathlib import Path
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import yt_dlp
from tkinter import Tk
from tkinter import filedialog
from win32com.shell import shell, shellcon

dpg.create_context()

logs_textarea = 0
download_button = 0

download_finished = True
logs_messages = []

def print_logs():
    dpg.set_value(logs_textarea, '\n'.join(logs_messages))

# Parameters for Cyrillic conversion
big_let_start = 0x00C0  # Capital "А" in Cyrillic.
big_let_end = 0x00DF  # Capital "Я" in Cyrillic.
small_let_end = 0x00FF  # Little "я" in Cyrillic
remap_big_let = 0x0410  # Initial number for the reassigned Cyrillic alphabet

alph_len = big_let_end - big_let_start + 1  # adds a shift from large letters to small ones
alph_shift = remap_big_let - big_let_start  # adds a transition from reassignment to non-reassignment

# Path to the font file 
font_file = 'CascadiaCode-Regular.otf'
if getattr(sys, 'frozen', False):
    font_path = os.path.join(sys._MEIPASS, 'files', font_file)
else:
    font_path = os.path.join('files', font_file)

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, 'files', 'icon.ico')
else:
    icon_path = os.path.join('files', 'icon.ico')

def fix_font():
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

    dpg.add_font_range(0x0391, 0x03C9)  #Greek character range
    dpg.add_font_range(0x2070, 0x209F)  #Range of upper and lower numerical indices

    # Fixing keyboard input on Windows
    if sys.platform == 'win32':
        biglet = remap_big_let  # Initial number for the reassigned Cyrillic alphabet
        for i1 in range(big_let_start, big_let_end + 1):  # Cyclic switching of large letters
            dpg.add_char_remap(i1, biglet)  # Reassigning the big letter
            dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Reassign a small letter
            biglet += 1  # choose the next letter

        #The letters "Ёё" must be added separately, since they are located elsewhere in the table
        dpg.add_char_remap(0x00A8, 0x0401)
        dpg.add_char_remap(0x00B8, 0x0451)

with dpg.font_registry():
    with dpg.font(font_path, size=24) as font:
        fix_font()
        # Set font
        dpg.bind_font(font)
    with dpg.font(font_path, size=42) as fontbig:
        fix_font()

def decode_string(instr : str):
    if sys.platform == 'win32':
        outstr = []
        for i in range(0, len(instr)):
            char_byte = ord(instr[i])
            if char_byte in range(big_let_start, small_let_end + 1):
                char = chr(ord(instr[i]) + alph_shift)
                outstr.append(char)
            # Checking for "Ё"
            elif char_byte == 0x00A8:
                char = chr(0x0401)
                outstr.append(char)
                # Checking for "ё"
            elif char_byte == 0x00B8:
                char = chr(0x0451)
                outstr.append(char)
            else:
                outstr.append(instr[i])

        return ''.join(outstr)

    else:
        return instr
class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        logs_messages.append(msg)
        print_logs()
        pass

    def warning(self, msg):
        logs_messages.append(msg)
        print_logs()
        pass

    def error(self, msg):
        logs_messages.append(msg)
        print_logs()
        print(msg)


# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
def my_hook(d):
    if d['status'] == 'finished':
        global download_finished
        download_finished = True
        dpg.enable_item(download_button)
        dpg.set_item_label(download_button, "Скачать")

video_sizes = (360, 720, 1080)
video_size = 360
url = ""
download_folder = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Downloads)
noplaylist = True

with dpg.window(label="Example Window") as main_window:
    def download_folder_select_callback():
        Tk().withdraw()
        new_download_folder = filedialog.askdirectory()
        if new_download_folder:
            download_folder = new_download_folder
            dpg.set_value(download_folder_label, download_folder)

    def submit_callback():
        new_url = decode_string(dpg.get_value(url_input))
        noplaylist = not dpg.get_value(check)
        video_size = dpg.get_value(video_size_select_combo)
        print(f'new_url = {new_url}, noplaylist = {noplaylist}')
        print(f'download_folder = {download_folder}')
        if not new_url:
            logs_messages.append("ВВЕДИТЕ АДРЕС ВИДЕО/ПЛЕЙЛИСТА!")
            print_logs()
        elif not download_folder:
            logs_messages.append("ВЫБЕРИТЕ ПАПКУ ДЛЯ ЗАГРУЗКИ!")
            print_logs()
        else:
            global url
            url = new_url
            ydl_opts = {
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
                'compat_opts': 'filename',
                'format_sort': [f'res:{video_size}'],
                'noplaylist': noplaylist,
                'paths': {'home': download_folder}
            }
            dpg.disable_item(download_button)
            dpg.set_item_label(download_button, "Идет скачивание...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)

    header = dpg.add_text("Скачивание видео с YouTube")
    sub_header = dpg.add_text("(Графический интерфейс для yt-dlp)")

    dpg.add_separator()

    dpg.add_text("Укажите адрес видео/плейлиста:")
    url_input = dpg.add_input_text(width=-1)

    dpg.add_separator()

    dpg.add_text("Укажите папку для скачивания:")
    with dpg.group(horizontal=True):
        download_folder_btn = dpg.add_button(label="Выбрать папку", callback=download_folder_select_callback)
        download_folder_label = dpg.add_text(download_folder, wrap=0)

    dpg.add_separator()

    check = dpg.add_checkbox(label="Скачать плейлист")

    dpg.add_separator()

    dpg.add_text("Качество видео:")
    video_size_select_combo = dpg.add_combo(video_sizes, default_value=video_size, width=200)

    dpg.add_separator()

    download_button = dpg.add_button(label="Скачать", callback=submit_callback)

    dpg.add_separator()

    dpg.add_text("Вывод:")
    logs_textarea = dpg.add_input_text(multiline=True, default_value="", height=300, width=-1, tab_input=True, readonly=True)

    dpg.bind_item_font(header, fontbig)

# light theme from DearPyGui_Ext
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Text                   , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TextDisabled           , (0.60 * 255, 0.60 * 255, 0.60 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg               , (0.94 * 255, 0.94 * 255, 0.94 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg                , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg                , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.98 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_Border                 , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.30 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow           , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg                , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg                , (0.96 * 255, 0.96 * 255, 0.96 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive          , (0.82 * 255, 0.82 * 255, 0.82 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed       , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.51 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg              , (0.86 * 255, 0.86 * 255, 0.86 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg            , (0.98 * 255, 0.98 * 255, 0.98 * 255, 0.53 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab          , (0.69 * 255, 0.69 * 255, 0.69 * 255, 0.80 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered   , (0.49 * 255, 0.49 * 255, 0.49 * 255, 0.80 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive    , (0.49 * 255, 0.49 * 255, 0.49 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark              , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab             , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.78 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive       , (0.46 * 255, 0.54 * 255, 0.80 * 255, 0.60 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button                 , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.40 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (0.06 * 255, 0.53 * 255, 0.98 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_Header                 , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.31 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered          , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive           , (0.26 * 255, 0.59 * 255, 0.98 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_Separator              , (0.39 * 255, 0.39 * 255, 0.39 * 255, 0.62 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered       , (0.14 * 255, 0.44 * 255, 0.80 * 255, 0.78 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive        , (0.14 * 255, 0.44 * 255, 0.80 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip             , (0.35 * 255, 0.35 * 255, 0.35 * 255, 0.17 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered      , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.67 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive       , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.95 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_Tab                    , (0.76 * 255, 0.80 * 255, 0.84 * 255, 0.93 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered             , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TabActive              , (0.60 * 255, 0.73 * 255, 0.88 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused           , (0.92 * 255, 0.93 * 255, 0.94 * 255, 0.99 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive     , (0.74 * 255, 0.82 * 255, 0.91 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_DockingPreview         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.22 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg         , (0.20 * 255, 0.20 * 255, 0.20 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_PlotLines              , (0.39 * 255, 0.39 * 255, 0.39 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered       , (1.00 * 255, 0.43 * 255, 0.35 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram          , (0.90 * 255, 0.70 * 255, 0.00 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered   , (1.00 * 255, 0.45 * 255, 0.00 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg          , (0.78 * 255, 0.87 * 255, 0.98 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong      , (0.57 * 255, 0.57 * 255, 0.64 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight       , (0.68 * 255, 0.68 * 255, 0.74 * 255, 1.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableRowBg             , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt          , (0.30 * 255, 0.30 * 255, 0.30 * 255, 0.09 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.35 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget         , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.95 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_NavHighlight           , (0.26 * 255, 0.59 * 255, 0.98 * 255, 0.80 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight  , (0.70 * 255, 0.70 * 255, 0.70 * 255, 0.70 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg      , (0.20 * 255, 0.20 * 255, 0.20 * 255, 0.20 * 255))
        dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg       , (0.20 * 255, 0.20 * 255, 0.20 * 255, 0.35 * 255))
        dpg.add_theme_color(dpg.mvPlotCol_FrameBg       , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_PlotBg        , (0.42 * 255, 0.57 * 255, 1.00 * 255, 0.13 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_PlotBorder    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_LegendBg      , (1.00 * 255, 1.00 * 255, 1.00 * 255, 0.98 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_LegendBorder  , (0.82 * 255, 0.82 * 255, 0.82 * 255, 0.80 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_LegendText    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_TitleText     , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_InlayText     , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_XAxis         , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid     , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxis         , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid     , (1.00 * 255, 1.00 * 255, 1.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxis2        , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid2    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxis3        , (0.00 * 255, 0.00 * 255, 0.00 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid3    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_Selection     , (0.82 * 255, 0.64 * 255, 0.03 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_Query         , (0.00 * 255, 0.84 * 255, 0.37 * 255, 1.00 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvPlotCol_Crosshairs    , (0.00 * 255, 0.00 * 255, 0.00 * 255, 0.50 * 255), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (240, 240, 240, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (100, 100, 100, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (248, 248, 248, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, (209, 209, 209, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_Link, (66, 150, 250, 100), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (66, 150, 250, 242), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_Pin, (66, 150, 250, 160), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_PinHovered, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (90, 170, 250, 30), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (90, 170, 250, 150), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_GridBackground, (225, 225, 225, 255), category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_GridLine, (180, 180, 180, 100), category=dpg.mvThemeCat_Nodes)

        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 12, 8, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 14, 8, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

dpg.create_viewport(title=f"Yt-dlp python GUI", width=800, height=800, small_icon=icon_path, large_icon=icon_path)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window(main_window, True)
dpg.start_dearpygui()
dpg.destroy_context()
