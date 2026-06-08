import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QFormLayout, QVBoxLayout, QLineEdit, QLabel)


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        form_layout = QFormLayout()

        self.fields = {
            'Amount': QLineEdit(),
            'Recipient': QLineEdit(),
            'Note': QLineEdit(),
        }

        for label, edit in self.fields.items():
            form_layout.addRow(label, edit)
            edit.editingFinished.connect(self.update_summary)

        self.summary_label = QLabel()
        self.summary_label.setFixedHeight(60)

        layout.addLayout(form_layout)
        layout.addStretch()
        layout.addWidget(self.summary_label)

    @Slot()
    def update_summary(self):
        self.summary_label.setText('\n'.join(
            f'{label}:\t{edit.text()}'
            for label, edit in self.fields.items()))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
