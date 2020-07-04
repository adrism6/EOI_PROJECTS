from PyQt5.QtGui import QKeySequence, QTextDocument, QFont, QCursor, QMouseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDir, QEvent
from os.path import expanduser
from os import getcwd
import os


app = QApplication([])
app.setApplicationName("PyNotepad")
editor = QPlainTextEdit()
editor.document().setDefaultFont(QFont("monospace"))


def ask_for_confirmation():
    answer = QMessageBox.question(
        window,
        "Confirm closing",
        "You have unsaved changes. Are you sure you want to exit?",
        QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
    )
    return answer


class MyMainWindow(QMainWindow):
    def closeEvent(self, e):
        if not editor.document().isModified():
            return
        answer = ask_for_confirmation()
        if answer == QMessageBox.Save:
            if not save():
                e.ignore()
        elif answer == QMessageBox.Cancel:
            e.ignore()


window = MyMainWindow()
window.setWindowTitle("PyNotepad")
window.setCentralWidget(editor)

file_menu = window.menuBar().addMenu("&File")
file_path = None


def check_is_modified():
    if editor.document().isModified():
        answer = ask_for_confirmation()
        if answer == QMessageBox.Save:
            if not save():
                return
        elif answer == QMessageBox.Cancel:
            return
    return True


def new_document():
    global file_path
    if check_is_modified() == True:
        editor.clear()
        file_path = None


new_action = QAction("&New document")
new_action.triggered.connect(new_document)
new_action.setShortcut(QKeySequence.New)
file_menu.addAction(new_action)


def show_open_dialog():
    global file_path
    if check_is_modified() == True:
        filename, _ = QFileDialog.getOpenFileName(window, "Open...")
        if filename:
            file_contents = ""
            with open(filename, "r") as f:
                file_contents = f.read()
            editor.setPlainText(file_contents)
            file_path = filename


open_action = QAction("&Open file...")
open_action.triggered.connect(show_open_dialog)
open_action.setShortcut(QKeySequence.Open)
file_menu.addAction(open_action)


def save():
    if file_path is None:
        return show_save_dialog()
    else:
        with open(file_path, "w") as f:
            f.write(editor.toPlainText())
        editor.document().setModified(False)
        return True


def show_save_dialog():
    global file_path
    filename, _ = QFileDialog.getSaveFileName(window, "Save as...")
    if filename:
        file_path = filename
        save()
        return True
    return False


save_action = QAction("&Save")
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
file_menu.addAction(save_action)

close_action = QAction("&Close")
close_action.triggered.connect(window.close)
close_action.setShortcut(QKeySequence.Quit)
file_menu.addAction(close_action)


def show_about_dialog():
    text = """
        <center>
            <h1>PyNotepad</h1><br/>
            <img src=logo.png width=200 height=200>
        </center>
        <p>Version 0.0.1</p>
    """
    QMessageBox.about(window, "About PyNotepad", text)


help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
about_action.triggered.connect(show_about_dialog)
help_menu.addAction(about_action)


class MyTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        path = expanduser("~")  # antes tenia de funcion getcwd()
        self.tree.setRootIndex(self.model.index(path))
        # estaria bien implementar que se abra desde home hasta el directorio actual
        self.tree.doubleClicked.connect(self.open_file)
        self.tree.setSortingEnabled(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.context_menu)
        dockwidget = QDockWidget("TreeView")
        dockwidget.setWidget(self.tree)
        dockwidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        global window
        window.addDockWidget(Qt.LeftDockWidgetArea, dockwidget)
        # treeview.setColumnWidth(0, 150)  # estaria bien implementar que se ajuste solo

    def context_menu(self):
        global open_action
        menu = QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        delete = menu.addAction("Delete")
        delete.triggered.connect(self.delete_file)
        rename = manu.addAction("Rename")
        rename.triggered.connect(self.rename_file)
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        global file_path
        if check_is_modified() == True:
            index = self.tree.currentIndex()
            filename = self.model.filePath(index)
            if filename:
                file_contents = ""
                with open(filename, "r") as f:
                    file_contents = f.read()
                editor.setPlainText(file_contents)
            file_path = filename

    def delete_file(self):
        pass

    def rename_file(self):
        pass


treeview = MyTreeView()


window.show()
app.exec()
