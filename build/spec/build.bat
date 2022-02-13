pyinstaller src/ExporterInterface.py ^
--distpath build/dist ^
--workpath build/build ^
 --specpath build/spec ^
 --noconsole --onefile ^
 --add-data "assets/logo.png;assets/logo.ico" 
@REM  --splash "assets/logo.png" 
@REM  --icon "assets/logo.ico" ^