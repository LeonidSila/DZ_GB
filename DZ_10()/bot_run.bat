@echo off

call %~dp0dz_10\venv\Scripts\activate

cd %~0dz_10

set TOKEN=5926331406:AAHL_rm5IYx08nHarDQL3_VXTxSIuktAEn0

python gb_telegram_bot.py

pause