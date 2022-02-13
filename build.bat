pyinstaller src/ExporterInterface.py ^
--distpath dist ^
--workpath build ^
 --specpath spec ^
 --onefile ^
 --noconsole ^
 --add-data "../assets;assets"^
 --splash "../assets/logo_bg.png" ^
 --icon "../assets/logo.ico" ^
 --hidden-import=pyi_splash