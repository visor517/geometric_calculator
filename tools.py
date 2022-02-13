from PyQt5.QtWidgets import QLayout

# чистим layout
def clear_layout(layout: QLayout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
