from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLineEdit)
from tagchip import TagChip


class TagBar(QWidget):

    tagsChanged = Signal(set)

    def __init__(self, parent=None):

        super().__init__(parent)

        self._tags = set()
        self.buttons = {}

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setContentsMargins(2, 2, 2, 2)
        self.h_layout.setSpacing(4)

        self.tag_edit = QLineEdit()
        self.tag_edit.setPlaceholderText('Add tag...')
        self.tag_edit.setFixedWidth(80)
        self.tag_edit.returnPressed.connect(self.on_return_pressed)

        self.h_layout.addWidget(self.tag_edit)
        self.h_layout.addStretch()
        
        self.setFocusProxy(self.tag_edit)

    @property
    def tags(self):
        return set(self._tags)

    @tags.setter
    def tags(self, new_tags):
        if new_tags == self._tags:
            return
        self.blockSignals(True)
        self.clear_buttons()
        self._tags = set(new_tags)
        for tag in sorted(self._tags):
            self.create_button(tag)
        self.blockSignals(False)

    @Slot()
    def add_tag(self, tag):
        tag = tag.strip()
        if not tag or tag in self._tags:
            self.tag_edit.clear()
            return
        self._tags.add(tag)
        self.create_button(tag)
        self.tag_edit.clear()
        self.tagsChanged.emit(set(self._tags))

    def remove_tag(self, tag):
        if tag not in self._tags:
            return
        self._tags.discard(tag)
        button = self.buttons.pop(tag, None)
        if button:
            self.h_layout.removeWidget(button)
            button.deleteLater()
        self.tagsChanged.emit(set(self._tags))

    def create_button(self, tag):
        chip = TagChip(tag)
        chip.closed.connect(self.remove_tag)
        self.buttons[tag] = chip
        insert_index = self.h_layout.indexOf(self.tag_edit)
        self.h_layout.insertWidget(insert_index, chip)

    def clear_buttons(self):
        for button in self.buttons.values():
            self.h_layout.removeWidget(button)
            button.deleteLater()
        self.buttons.clear()

    @Slot()
    def on_return_pressed(self):
        self.add_tag(self.tag_edit.text())
        self.tag_edit.setFocus()
