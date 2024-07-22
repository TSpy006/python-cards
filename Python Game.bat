@echo off




for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"

echo %ESC%[32;40m
python main.py
echo %ESC%[0m


pause
