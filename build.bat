set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat %root%

call conda activate ymg

pyinstaller --name="Girl bing-go" ^
-p="C:\Users\skdid\anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins/platforms" ^
--add-data="C:\Users\skdid\anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins/platforms" ^
--add-data="C:\Users\skdid\Documents\Girl-Bing-go-game\girl; C:\Users\skdid\Documents\Girl-Bing-go-game\girl" ^
--add-data="C:\Users\skdid\Documents\Girl-Bing-go-game\nice; C:\Users\skdid\Documents\Girl-Bing-go-game\nice" ^
--onefile ^
ymg_pyside_mini_project1.py 
pause

C:\Users\skdid\Documents\Girl-Bing-go-game
