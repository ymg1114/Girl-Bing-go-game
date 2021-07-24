set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat %root%

set pg1=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\PySide6\plugins
set pg2=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\PySide6

set shi=C:\Users\skdid\Anaconda3\envs\ymg\Lib\site-packages\shiboken6

call conda activate ymg

pyinstaller --name="Girl bing-go" ^

--add-data "%pg1%; PySide6\plugins" ^
--add-data "%pg2%\*.dll; PySide6" ^
--add-data "%shi%\*.dll; shiboken6" ^

--add-data ".\girl; girl" ^
--add-data ".\nice; nice" ^
--onefile ^
ymg_pyside_mini_project1.py 
pause
