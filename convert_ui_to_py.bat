set root=C:\Users\skdid\anaconda3

call %root%\Scripts\activate.bat %root%

call conda activate ymg

call pyside6-uic bingo_ui.ui -o bingo_ui.py