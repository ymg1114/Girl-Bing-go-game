set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat %root%

call conda activate ymg

pyinstaller --name="Girl bing-go" ^
-p="C:\Users\skdid\anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins/platforms" ^
--add-data="C:\Users\skdid\anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins/platforms" ^
--add-data="C:\Users\skdid\Downloads\PySide6 공부용 예제\ymg_pyside_examples\girl; C:\Users\skdid\Downloads\PySide6 공부용 예제\ymg_pyside_examples\girl" ^
--add-data="C:\Users\skdid\Downloads\PySide6 공부용 예제\ymg_pyside_examples\nice; C:\Users\skdid\Downloads\PySide6 공부용 예제\ymg_pyside_examples\nice" ^
--onefile ^
ymg_pyside_mini_project1.py 
