import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QListWidgetItem, QStyle, QAbstractItemDelegate)

from tagbar import TagBar


class Note:

    def __init__(self):
        self.title = 'New Note'
        self.text = ''
        self.tags = set()


class NoteEditor(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(660, 420)

        central = QWidget()
        self.setCentralWidget(central)
        h_layout = QHBoxLayout(central)

        self.note_list = QListWidget()
        self.note_list.setFixedWidth(150)
        h_layout.addWidget(self.note_list)

        editor_panel = QWidget()
        v_layout = QVBoxLayout(editor_panel)
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(2)
        h_layout.addWidget(editor_panel)
        
        # 4. Integrate with the main window.
        
        self.tag_bar = TagBar()
        self.text_edit = QTextEdit()
        v_layout.addWidget(self.tag_bar)
        v_layout.addWidget(self.text_edit)
        
        self.tag_bar.setEnabled(False)
        self.text_edit.setEnabled(False)

        self.note_list.currentItemChanged.connect(self.on_note_changed)
        self.note_list.itemChanged.connect(self.on_item_changed)
        self.tag_bar.tagsChanged.connect(self.on_tags_changed)
        self.note_list.itemDelegate().closeEditor.connect(
            self.on_title_editor_closed)

        new_action = QAction('New', self)
        new_action.setIcon(self.style().standardIcon(
            QStyle.StandardPixmap.SP_FileIcon))
        new_action.triggered.connect(self.add_note)

        toolbar = self.addToolBar('Main')
        toolbar.addAction(new_action)
        toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

    @Slot()
    def add_note(self):

        note = Note()

        item = QListWidgetItem(note.title)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        item.setData(Qt.ItemDataRole.UserRole, note)

        self.note_list.addItem(item)
        self.note_list.setCurrentItem(item)
        self.note_list.editItem(item)

    @Slot()
    def on_note_changed(self, current, previous):

        if previous:
            note = previous.data(Qt.ItemDataRole.UserRole)
            if note:
                note.text = self.text_edit.toPlainText()
                note.tags = self.tag_bar.tags

        if current:
            note = current.data(Qt.ItemDataRole.UserRole)
            if note:
                self.text_edit.setPlainText(note.text)
                self.tag_bar.tags = note.tags
        else:
            self.text_edit.clear()
            self.tag_bar.tags = set()
            
        has_note = current is not None
        self.tag_bar.setEnabled(has_note)
        self.text_edit.setEnabled(has_note)
        
        if not has_note:
            self.text_edit.clear()
            self.tag_bar.tags = set()

    @Slot()
    def on_item_changed(self, item):
        note = item.data(Qt.ItemDataRole.UserRole)
        if note:
            note.title = item.text().strip() or 'Untitled'
    
    @Slot(set)     
    def on_tags_changed(self, tags):
        item = self.note_list.currentItem()
        if not item:
            return
        note = item.data(Qt.ItemDataRole.UserRole)
        if note:
            note.tags = tags 
            
    @Slot()
    def on_title_editor_closed(self, editor, hint):
        if hint == QAbstractItemDelegate.EndEditHint.SubmitModelCache:
            self.tag_bar.setFocus()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = NoteEditor()
    editor.show()
    sys.exit(app.exec())
