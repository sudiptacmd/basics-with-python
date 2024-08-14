from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
import requests
from bs4 import BeautifulSoup

def getrate(fr, to):
    url = f"https://www.x-rates.com/calculator/?from={fr}&to={to}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()[:-4]
    rate = float(rate)
    return rate

def print_result():
    incur = in_combo.currentText().lower()
    outcur = target_combo.currentText().lower()
    user_in = float(in_text.text())
    rate = getrate(incur,outcur)
    message = f"{user_in} {incur.upper()} = {rate*user_in} {outcur.upper()}"
    output.setText(str(message))

coun = ['USD', 'EUR', 'INR']

app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

in_combo = QComboBox()
in_combo.addItems(coun)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(coun)
layout.addWidget(target_combo)

in_text = QLineEdit()
layout.addWidget(in_text)


btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(print_result)

output = QLabel('')
layout.addWidget(output)

window.setLayout(layout)
window.show()
app.exec()