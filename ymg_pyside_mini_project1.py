import sys
from PySide6.QtCore import (QLineF, QMimeData, QPoint, QPointF, Qt)
from PySide6.QtGui import ( QColor, QDrag, QImage, QPainter, QPixmap, QPen)
from PySide6.QtWidgets import (QApplication, QGraphicsRectItem, QGraphicsScene,
                               QGraphicsView, QGraphicsPixmapItem)
from PySide6.QtCore import Qt, Signal, QBasicTimer
from ymg_ui2 import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import random
import os
import copy
import numpy as np
import json

cur = os.getcwd()

if len(sys.argv) > 1:
    build = [k for k in sys.argv if 'build' in k][0]
    
    if json.loads(build[6:].lower()):
        _girl = os.path.join(os.path.dirname(__file__))
        _nice = os.path.join(os.path.dirname(__file__))
    else:
        _girl = os.path.join(os.path.dirname(__file__), 'girl')
        _nice = os.path.join(os.path.dirname(__file__), 'nice')

else:
    _girl = os.path.join(os.path.dirname(__file__), 'girl')
    _nice = os.path.join(os.path.dirname(__file__), 'nice')


BOARD_SIZE = 5
BOARD_SCALE = 100


class SingletonInstane:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance



GIRL_IDX_POOL = [i for i in range(5)] * 5 

class BOARD(SingletonInstane):
    config = np.array( [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] )
    score = 0
    
    

def Reset_bingo_Board():
    BOARD.instance().score = 0
    _GIRL_IDX_POOL = copy.deepcopy(GIRL_IDX_POOL)
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            idx = random.sample(_GIRL_IDX_POOL, 1)[0]
            _GIRL_IDX_POOL.remove(idx)
            girl = Girl(x, y, idx)
            image = QImage(_girl + f'\\girl_{idx}.jpg')
            # image = QImage(cur + f'\\girl\\girl_{idx}.jpg')
            girl.setPixmap( QPixmap.fromImage(image).scaled(BOARD_SCALE, BOARD_SCALE) )
            girl.setPos(x*BOARD_SCALE, y*BOARD_SCALE)
            Girl_bingo_Board(0, 0, 700, 800).instance().addItem(girl)
            
            BOARD.instance().config[y, x] = girl
    

class Girl(QGraphicsPixmapItem):
    
    def __init__(self, x, y, idx, *args, **kargs):
        super().__init__(*args, **kargs)
        self.setAcceptDrops(True) 
        self.setCursor(Qt.OpenHandCursor)
        self._start_drag_distance = QApplication.startDragDistance()
        self.ImageData = QImage(_girl + f'\\girl_{idx}.jpg')
        # self.ImageData = QImage(cur + f'\\girl\\girl_{idx}.jpg')
        self.pixmap = QPixmap.fromImage(self.ImageData).scaled(BOARD_SCALE, BOARD_SCALE)
        
        self.object_location = (y, x)
        self.idx = idx
        self.done = False
        
    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            event.ignore()
            return
        self.setCursor(Qt.ClosedHandCursor) 
        
    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)
        
    def mouseMoveEvent(self, event):
        start = QPointF(event.buttonDownScreenPos(Qt.LeftButton))
        if QLineF(event.screenPos(), start).length() < self._start_drag_distance:
            return

        drag = QDrag(event.widget()) 
        mime = QMimeData()         
        drag.setMimeData(mime)     
        drag.setHotSpot(QPoint(BOARD_SCALE/2, BOARD_SCALE/2)) 
        
        mime.setImageData(self.ImageData)
        mime.setText( str(self.idx) )
        drag.setPixmap( self.pixmap.scaled(BOARD_SCALE, BOARD_SCALE) ) 

        drag.exec()
        self.setCursor(Qt.OpenHandCursor)


    def dragEnterEvent(self, event):
        if event.mimeData().hasImage(): 
            event.setAccepted(True)
            self._drag_over = True
        else:
            event.setAccepted(False)
    
    def dragLeaveEvent(self, event):
        self._drag_over = False
        
    def dropEvent(self, event):
        self._drag_over = False
        if event.mimeData().hasColor():
            self.color = QColor(event.mimeData().colorData())
        elif event.mimeData().hasImage():
            self.ImageData = event.mimeData().imageData()
            self.pixmap = QPixmap(self.ImageData)
            self.setPixmap( self.pixmap.scaled(BOARD_SCALE, BOARD_SCALE) )
            
            self.idx = int( event.mimeData().text() )

            self.check_score()
        else:
            event.ignore()
    
    
    def get_girl_y_index(self, y_low):    
        return np.array( [v.idx for v in BOARD.instance().config[ y_low, : ]] )
        
    def get_girl_x_index(self, x_low): 
        return np.array( [v.idx for v in BOARD.instance().config[ :, x_low ]] )
    
    
    def oh_bingo_x(self, x_low):
        image = QImage(_nice + f'\\bingo.jpg')
        # image = QImage(cur + f'\\nice\\bingo.jpg')
        for v in BOARD.instance().config[ :, x_low ]:
            v.setPixmap( QPixmap.fromImage(image).scaled(BOARD_SCALE, BOARD_SCALE) )
            v.setAcceptDrops(False) 
            v.done = True
            
    def oh_bingo_y(self, y_low):
        image = QImage(_nice + f'\\bingo.jpg')
        # image = QImage(cur + f'\\nice\\bingo.jpg')
        for v in BOARD.instance().config[ y_low, : ]:
            v.setPixmap( QPixmap.fromImage(image).scaled(BOARD_SCALE, BOARD_SCALE) )
            v.setAcceptDrops(False) 
            v.done = True
    
    def check_score(self):
        BOARD.instance().score = 0

        for y_low in range(BOARD_SIZE):
            if (BOARD.instance().config[ y_low, 0 ].idx == self.get_girl_y_index(y_low)).all():
                BOARD.instance().score += 1
                self.oh_bingo_y(y_low)
                
        for x_low in range(BOARD_SIZE):
            if (BOARD.instance().config[ 0, x_low ].idx == self.get_girl_x_index(x_low)).all():
                BOARD.instance().score += 1
                self.oh_bingo_x(x_low)

          

class Girl_bingo_view(QGraphicsView):
    def __init__(self, scene, *args):
        super().__init__(scene, *args)
       

class Girl_bingo_Board(QGraphicsScene, SingletonInstane):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
    
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                Rect = QGraphicsRectItem()
                Rect.setRect(y*BOARD_SCALE, x*BOARD_SCALE, BOARD_SCALE, BOARD_SCALE)
                Rect.setPen(QPen(QColor(0, 0, 0, 255)))
                self.addItem(Rect)


class Girl_bingo_Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Girl_bingo_Window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Girl bing-go")

        self.view = Girl_bingo_view(Girl_bingo_Board(0, 0, 700, 800).instance(), self.widget)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.view.setBackgroundBrush(QColor(230, 200, 167))


        self.timer = QBasicTimer()
        self.step = 0
        
        self.GameStart.clicked.connect(self.doAction)
        self.RandomShuffle.clicked.connect(Reset_bingo_Board)
        self.Close.clicked.connect(self.close)
        self.progressBar.setValue(BOARD.instance().score*10)

    def timerEvent(self, e):
        if self.step >= 1000 or self.progressBar.value() == 100:
            self.timer.stop()
            self.GameStart.setText('GameFinished')
            return

        self.step = self.step + 1
        score = np.sum( [1 for v_low in BOARD.instance().config for v in v_low if v.done] )
        self.progressBar.setValue( score*4 )
        
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.GameStart.setText('GameStart')
        else:
            self.timer.start(1000, self)
            self.GameStart.setText('GameStop')

        
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = Girl_bingo_Window()
    window.show() 
    app.exec()