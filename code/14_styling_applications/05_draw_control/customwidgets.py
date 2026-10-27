from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QLabel, QCheckBox,
    QComboBox, QSlider, QLineEdit)


class WidgetFactory(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        MARGIN = 40

        main = QVBoxLayout(self)

        char_frame = QFrame()
        char_frame.setFrameShape(QFrame.Shape.StyledPanel)
        char_l = QHBoxLayout(char_frame)
        char_l.setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)

        char_l.addWidget(QLabel('Hero Name:'))
        char_l.addWidget(QLineEdit('Eldrin the Wise'))
        char_l.addWidget(QLabel('Class:'))
        cls = QComboBox()
        cls.addItems(['Mage', 'Warlock', 'Druid', 'Necromancer'])
        char_l.addWidget(cls)

        main.addWidget(char_frame)

        magic_frame = QFrame()
        magic_frame.setFrameShape(QFrame.Shape.StyledPanel)
        magic_l = QGridLayout(magic_frame)
        magic_l.setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)

        magic_l.addWidget(QLabel('Spell Power'), 0, 0)
        power = QSlider(Qt.Orientation.Horizontal)
        power.setRange(0, 100)
        power.setValue(55)
        magic_l.addWidget(power, 0, 1)

        magic_l.addWidget(QCheckBox('Auto-cast Cantrips'), 1, 0, 1, 2)

        main.addWidget(magic_frame)

        world_frame = QFrame()
        world_frame.setFrameShape(QFrame.Shape.StyledPanel)
        world_l = QVBoxLayout(world_frame)
        world_l.setContentsMargins(MARGIN, MARGIN, MARGIN, MARGIN)

        world_l.addWidget(QLabel('Realm:'))
        realm = QComboBox()
        realm.addItems(['Eldergrove', 'Shadowfen',
                        'Crystal Peaks', 'Ashen Wastes'])
        world_l.addWidget(realm)

        world_l.addWidget(QCheckBox('Eternal Night'))
        world_l.addWidget(QCheckBox('Roaming Dragons'))
        world_l.addWidget(QCheckBox('Ancient Ruins Visible'))
        world_l.addStretch()

        main.addWidget(world_frame)
