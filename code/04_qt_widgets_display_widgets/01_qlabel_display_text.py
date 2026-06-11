import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setWindowTitle('Account Summary')
        self.resize(300, 120)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        name = 'Current Account'
        account_type = 'Checking'
        description = 'Primary everyday spending account'
        balance = 2450.00
        overdrawn = True
        
        # 1. Create QLabel objects.
        
        name_label = QLabel(name)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = name_label.font()
        font.setPointSize(12)
        font.setBold(True)
        name_label.setFont(font)
        
        type_label = QLabel(f'Type: {account_type}')
        
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        
        balance_label = QLabel(f'Balance: **${balance:,.2f}**')
        
        overdraft_label = QLabel()
        if overdrawn:
            overdraft_label.setText(
                '<span style="color: red;">'
                'Overdraft protection active'
                '</span>')
        
        # 2. Optionally, set their text format.

        balance_label.setTextFormat(Qt.TextFormat.MarkdownText)
        overdraft_label.setTextFormat(Qt.TextFormat.RichText)
        
        # 3. Add the objects to the layout.

        layout.addWidget(name_label)
        layout.addWidget(type_label)
        layout.addWidget(desc_label)
        layout.addWidget(balance_label)
        layout.addWidget(overdraft_label)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
