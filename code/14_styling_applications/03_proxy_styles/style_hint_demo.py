import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCharFormat, QColor, QPen, QBrush
from PySide6.QtWidgets import (
    QApplication, QTextBrowser, QProxyStyle, QStyle,
    QStyleFactory, QStyleHintReturnVariant
)


class MyStyle(QProxyStyle):

    def styleHint(self, hint, option=None,
                  widget=None, returnData=None):

        if (hint ==
                QStyle.StyleHint.SH_TextControl_FocusIndicatorTextCharFormat):

            if isinstance(returnData, QStyleHintReturnVariant):

                fmt = QTextCharFormat()

                fmt.setProperty(
                    QTextCharFormat.Property.OutlinePen,
                    QPen(
                        QColor('red'),
                        2,
                        Qt.PenStyle.DotLine
                    )
                )

                fmt.setProperty(
                    QTextCharFormat.Property.BackgroundBrush,
                    QBrush(QColor('yellow'))
                )

                returnData.variant = fmt

                print('STYLE HINT REQUESTED')

                return 1

        return super().styleHint(
            hint, option, widget, returnData
        )


app = QApplication(sys.argv)

style = MyStyle(QStyleFactory.create('windows11'))
app.setStyle(style)

browser = QTextBrowser()

browser.setHtml(
    '<p>'
    '<a href="https://example.com">FOCUSED LINK</a>'
    '</p>'
)

browser.setOpenExternalLinks(False)
browser.setTabChangesFocus(False)

browser.resize(400, 100)
browser.show()
browser.setFocus()

sys.exit(app.exec())