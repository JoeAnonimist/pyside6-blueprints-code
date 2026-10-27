from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyle, QProxyStyle, QStyleFactory


# 1. Create a QProxyStyle subclass.

class MyProxyStyle(QProxyStyle):

    def __init__(self):
        base = QStyleFactory.create('Fusion')
        super().__init__(base)
        
    # 2. Reimplement pixelMetric().

    def pixelMetric(self, metric, option=None, widget=None):
        
        value = super().pixelMetric(metric, option, widget)

        if metric in (QStyle.PixelMetric.PM_ButtonMargin,
                        QStyle.PixelMetric.PM_IndicatorHeight,
                        QStyle.PixelMetric.PM_IndicatorWidth):
            return value + 20
        return value
    
    # 3. Reimplement styleHint().

    def styleHint(self, hint, option=None, widget=None, returnData=None):
        if hint == QStyle.StyleHint.SH_ComboBox_Popup:
            return 1
        if hint == QStyle.StyleHint.SH_TabBar_Alignment:
            return Qt.AlignmentFlag.AlignCenter
        return super().styleHint(hint, option, widget, returnData)
