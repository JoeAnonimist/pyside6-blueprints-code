from PySide6.QtCore import Signal, Slot, QSize, Qt
from PySide6.QtWidgets import QWidget, QLineEdit
from tagchip import TagChip


class TagBar(QWidget):

    tagsChanged = Signal(set)

    def __init__(self, parent=None):

        super().__init__(parent)

        self._tags = set()
        self.buttons = {}

        self.tag_edit = QLineEdit(self)
        self.tag_edit.setPlaceholderText('Add tag...')
        self.tag_edit.setFixedWidth(100)
        self.tag_edit.returnPressed.connect(self.on_return_pressed)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setMinimumHeight(40)
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
        self.update_geometry()

    def compute_rects(self):
        margin = 4
        spacing = 6
        row_h = 32
        available_w = max(100, self.width() - 2 * margin)

        x = margin
        y = margin

        positions = []
        widgets = []

        # Word-wrap algorithm for widgets: advance a cursor to the right,
        # drop to a new row whenever the next item would overflow.
        for chip in self.buttons.values():
            w = max(chip.sizeHint().width(), 60)

            if x + w > available_w and x > margin:
                x = margin
                y += row_h + spacing

            positions.append((x, y, w, row_h))
            widgets.append(chip)
            x += w + spacing

        # The edit field follows the same cursor as the chips.
        edit_w = 100
        if x + edit_w > available_w and x > margin:
            x = margin
            y += row_h + spacing

        positions.append((x, y, edit_w, row_h))
        widgets.append(self.tag_edit)

        total_h = y + row_h + 2 * margin
        return positions, widgets, total_h

    def update_geometry(self):
        if self.width() < 50:
            return

        positions, widgets, needed_h = self.compute_rects()

        for (x, y, w, h), widget in zip(positions, widgets):
            widget.setGeometry(x, y, w, h)
            widget.show()

        self.setMinimumHeight(needed_h)
        self.updateGeometry()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_geometry()

    def showEvent(self, event):
        super().showEvent(event)
        self.update_geometry()

    def sizeHint(self):
        _, _, h = self.compute_rects()
        return QSize(500, max(40, h))

    def create_button(self, tag):
        if tag in self.buttons:
            return
        chip = TagChip(tag, parent=self)
        chip.closed.connect(self.remove_tag)
        self.buttons[tag] = chip
        self.update_geometry()

    def clear_buttons(self):
        for chip in list(self.buttons.values()):
            chip.deleteLater()
        self.buttons.clear()

    def remove_tag(self, tag):
        if tag not in self._tags:
            return
        self._tags.discard(tag)
        chip = self.buttons.pop(tag, None)
        if chip:
            chip.deleteLater()
        self.tagsChanged.emit(set(self._tags))
        self.update_geometry()

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

    @Slot()
    def on_return_pressed(self):
        self.add_tag(self.tag_edit.text())
        self.tag_edit.setFocus()
