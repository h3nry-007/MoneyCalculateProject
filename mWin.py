from PySide6.QtWidgets import QPushButton, QWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

class MWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Money Calculate ")

        money_lable = QLabel("Enter Amount")
        self.input_amount = QLineEdit()

        day_lable = QLabel("Enter Days:")
        self.input_day = QLineEdit()

        ok_btn = QPushButton("Calculate")
        ok_btn.clicked.connect(self.calculate)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear)


        self.output = QLabel()

        money_layout = QHBoxLayout()
        money_layout.addWidget(money_lable)
        money_layout.addWidget(self.input_amount)

        day_layout = QHBoxLayout()
        day_layout.addWidget(day_lable)
        day_layout.addWidget(self.input_day)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(clear_btn)

        v_layout = QVBoxLayout()
        v_layout.addLayout(money_layout)
        v_layout.addLayout(day_layout)
        v_layout.addLayout(btn_layout)
        v_layout.addWidget(self.output)

        self.setLayout(v_layout)

    def calculate(self):
        money = int(self.input_amount.text())
        day = int(self.input_day.text())
        for i in range(day):
            percentage = money * 0.01
            money = money + percentage
            i+1

        self.output.setText(str(int(money)))

    def clear(self):
        self.input_day.setText('')
        self.input_amount.setText('')
        self.output.setText('')


