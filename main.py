import sys
import random
from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем UI из файла
        self.pushButton.clicked.connect(self.on_click)  # Подключаем обработчик нажатия кнопки

        self.circles = []  # Список для хранения окружностей

    def on_click(self):
        # Генерация случайных данных для окружности
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()  # Перерисовываем окно

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Рисуем каждую окружность
        for (x, y, diameter) in self.circles:
            painter.setBrush(QBrush(QColor(255, 255, 0)))  # Желтый цвет
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
