import typing
from PyQt5 import QtGui
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtWidgets import QTimeEdit, qApp


class ClickCopyTimeedit(QTimeEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, a0: QObject | None, a1: QEvent | None) -> bool:
        print(a0)
        print(a1)
        return super().eventFilter(a0, a1)
