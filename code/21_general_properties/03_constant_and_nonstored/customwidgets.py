from PySide6.QtCore import Property, Signal
from PySide6.QtWidgets import (QWidget, QLineEdit,
    QLabel, QVBoxLayout)


# 1. Subclass QWidget to create a custom widget.

class SignupWidget(QWidget):
    
    usernameChanged = Signal(str)

    def __init__(self, parent=None):

        super().__init__(parent)
        
        self._firstname = ''
        self._lastname = ''
        self._domain = 'company.com'
        
        self.fname_edit = QLineEdit()
        self.lname_edit = QLineEdit()
        self.email_label = QLabel()
        
        self.fname_edit.editingFinished.connect(self.on_firstname_changed)
        self.lname_edit.editingFinished.connect(self.on_lastname_changed)
        
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('First Name:'))
        layout.addWidget(self.fname_edit)
        layout.addWidget(QLabel('Last Name:'))
        layout.addWidget(self.lname_edit)
        layout.addWidget(QLabel('Email:'))
        layout.addWidget(self.email_label)
    
    @Property(str)
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, value):
        value = value.strip()
        if value != self._firstname:
            self._firstname = value
            self._update_email_label()
            self.usernameChanged.emit(self.username)

    @Property(str)
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value):
        value = value.strip()
        if value != self._lastname:
            self._lastname = value
            self._update_email_label()
            self.usernameChanged.emit(self.username)
    
    # 2. Declare a constant property.
    
    @Property(str, constant=True)
    def domain(self):
        return self._domain
    
    # 3. Declare non-stored properties.
    
    @Property(str, stored=False)
    def username(self):
        if self.firstname and self.lastname:
            return f'{self.firstname}.{self.lastname}'
        else:
            return ''
    
    @Property(str, stored=False)
    def email(self):
        if self.username:
            return f'{self.username}@{self.domain}'
        else:
            return ''
    
    def on_firstname_changed(self):
        self.firstname = self.fname_edit.text()
        
    def on_lastname_changed(self):
        self.lastname = self.lname_edit.text()
        
    def _update_email_label(self):
        self.email_label.setText(self.email)
