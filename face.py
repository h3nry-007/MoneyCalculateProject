import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor

class FaceWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.eye_x = 50
        self.eye_y = 50

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a face (a simple circle)
        painter.setBrush(QColor(255, 255, 0))  # Yellow color for the face
        painter.drawEllipse(50, 50, 200, 200)

        # Draw left eye
        painter.setBrush(QColor(0, 0, 0))  # Black color for the eye
        painter.drawEllipse(self.eye_x, self.eye_y, 40, 40)

class FaceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.face_widget = FaceWidget()
        self.setCentralWidget(self.face_widget)

        arrow_layout = QHBoxLayout()

        left_button = QPushButton("Left")
        left_button.clicked.connect(self.move_eye_left)
        arrow_layout.addWidget(left_button)

        right_button = QPushButton("Right")
        right_button.clicked.connect(self.move_eye_right)
        arrow_layout.addWidget(right_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(arrow_layout)
        main_layout.addWidget(self.face_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Moving Eye')
        self.show()

    def move_eye_left(self):
        self.face_widget.eye_x -= 10
        self.face_widget.update()

    def move_eye_right(self):
        self.face_widget.eye_x += 10
        self.face_widget.update()

def main():
    app = QApplication(sys.argv)
    window = FaceApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
