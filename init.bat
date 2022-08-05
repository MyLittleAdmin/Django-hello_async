curl -L --ssl-no-revoke -o winpython.7z --url https://sourceforge.net/projects/winpython/files/WinPython_3.8/3.8.9.0/Winpython64-3.8.9.0dot.exe/download
winpython.7z -y -gm2
del winpython.7z
timeout 10
ren WPy64-3890 WinPython
WinPython\python-3.8.9.amd64\python.exe -m venv .\venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
call db_migration.bat