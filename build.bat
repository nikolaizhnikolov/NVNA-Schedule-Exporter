pyinstaller src/ExporterInterface.py ^
--distpath dist ^
--workpath build ^
 --specpath spec ^
 --noconsole --onefile ^
 --add-data "../assets/logo_bg.png;../assets/logo.ico" ^
 --splash "../assets/logo_bg.png" ^
 --icon "../assets/logo.ico" 