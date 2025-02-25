import sys
import random
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Рандомные шарики")
        self.setGeometry(100, 100, 800, 600)

        self.pushButton = QPushButton("Добавить шарик", self)
        self.pushButton.setGeometry(350, 20, 100, 40)
        self.pushButton.clicked.connect(self.on_click)

        self.circles = []

    def on_click(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for (x, y, diameter, color) in self.circles:
            painter.setBrush(QBrush(color))
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
