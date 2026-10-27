from PySide6.QtWidgets import QStyle, QProxyStyle, QStyleFactory

# 1 Create a custom style.

class MyProxyStyle(QProxyStyle):

    def __init__(self, level=None):
        super().__init__(QStyleFactory.create('Fusion'))
        self.logging_enabled = True
        self.last_widget = None
        
    # 2. Create the log method.

    def log(self, method, name, widget):
        
        if not self.logging_enabled:
            return

        widget_name = widget.metaObject().className()
        if widget_name != self.last_widget:
            print(f'\n{widget_name}')
            self.last_widget = widget_name

        print(f'    {method:<22}{name}')
        
    # 3. Reimplement the three methods.

    def drawPrimitive(self, element, option, painter, widget=None):
        name = QStyle.PrimitiveElement(element).name
        self.log('drawPrimitive()', name, widget)
        super().drawPrimitive(element, option, painter, widget)

    def drawControl(self, element, option, painter, widget=None):
        name = QStyle.ControlElement(element).name
        self.log('drawControl()', name, widget)
        super().drawControl(element, option, painter, widget)

    def drawComplexControl(self, control, option, painter, widget=None):
        name = QStyle.ComplexControl(control).name
        self.log('drawComplexControl()', name, widget)
        super().drawComplexControl(control, option, painter, widget)
