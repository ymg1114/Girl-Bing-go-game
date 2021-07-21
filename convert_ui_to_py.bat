set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat %root%

call conda activate ymg

call pyside6-uic ymg_ui2.ui -o ymg_ui2.py