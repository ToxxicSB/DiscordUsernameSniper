@ECHO OFF
REM BFCPEOPTIONSTART
REM BFCPEEXE=
REM BFCPEICON=
REM BFCPEICONINDEX=-1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=0
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT=TOXXIC UsernameSniper Settings
REM BFCPEVERDESC=Configure TOXXIC UsernameSniper
REM BFCPEVERCOMPANY=Toxxic
REM BFCPEVERCOPYRIGHT=Copyright Info
REM BFCPEOPTIONEND

CHCP 65001 > NUL
TITLE TOXXIC UsernameSniper Settings


START ./data/config.json
EXIT