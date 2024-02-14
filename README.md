# mkvtomp4
**MKV to MP4 Converter**

This easy-to-use Python script provides a simple graphical interface for converting MKV video files to the more widely compatible MP4 format. Whether you have a few files or need to convert in bulk, this tool makes the process quick and painless.

**Features**

* Super simple GUI: No complicated options – just select your MKV file and click "Convert"!
* Automatic ffmpeg handling: The script checks if you have ffmpeg installed (needed for conversion) and offers guidance if you don't.
* Convenient Output: Converted MP4 files are saved neatly in a 'convert' folder within the script's directory.
* Progress Updates: See the conversion status right in the application window.

**Prerequisites**

* Python 3.x: Download the latest version from https://www.python.org/
* tkinter: Usually included with Python. If not, install with `pip install tkinter`
* ffmpeg: Get it from https://ffmpeg.org/ or your system's package manager.

**Installation**

1. Download or copy the script code. (You can name it something like `mkv_to_mp4_converter.py`)
2. Make sure you have ffmpeg installed.

**How to Use**

1. Run the script:
   * If you're comfortable with the command line, use `python mkv_to_mp4_converter.py`
   * Otherwise, most code editors or Python environments let you run Python scripts directly.
2. Click the "Select MKV and Convert" button.
3. Choose the MKV file you want to convert.
4. Watch the progress in the application window.
5. Click "Open Output Folder" (appears when done) to access your converted MP4 file.

**Troubleshooting**

* No "Open Output Folder" button: Make sure your conversion was successful; any errors will be displayed in the window.
* Issues with ffmpeg: Please refer to the ffmpeg documentation for installation and usage.

**License**

This script is provided "as is", without warranty of any kind. Feel free to use and modify it as needed. Please adhere to the licenses of any included libraries (tkinter is part of the Python standard library; ffmpeg has its own license).