set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat

set pg1=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins
set pg2=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\PySide6

set shi=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\shiboken6

call conda activate ymg

pip install -r requirements.txt

pyinstaller --name="Girl bing-go" ^
--add-data="%pg1%; PySide6" ^
--add-data="%pg2%\*.dll; PySide6" ^
--add-data="%pg2%\*.pyd; PySide6" ^
--add-data="%pg2%\pyside6.*.dll; PySide6" ^
--add-data="%shi%\*.dll; shiboken6" ^
--add-data="%shi%\shiboken6.*.dll; shiboken6" ^
--add-data=".\girl\*.jpg; girl" ^
--add-data=".\nice\*.jpg; nice" ^
--onefile ^
--windowed ^
ymg_pyside_mini_project1.py 
pause
