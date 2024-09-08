from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication([])

QMessageBox.information(None, "Info", "Welcome to PySide6!")

reply = QMessageBox.question(None, "Question", "Do you like PySide6?", QMessageBox.Yes | QMessageBox.No)
if reply == QMessageBox.Yes:
    print("User likes PySide6!")
else:
    print("User doesn't like PySide6.")

app.exec()
