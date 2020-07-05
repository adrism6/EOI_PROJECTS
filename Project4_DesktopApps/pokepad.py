from PyQt5.QtGui import QKeySequence, QFont, QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDir, QSize
from os.path import expanduser, isdir
from os import remove
from PyQt5.QtWebEngineWidgets import QWebEngineView
from markdown2 import Markdown


app = QApplication([])
app.setApplicationName("PokéPad")
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
window.setWindowTitle("PokéPad")
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
        webengine.markdown_to_html()
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
            webengine.markdown_to_html()


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
        webengine.markdown_to_html()
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
            <h1>PokéPad</h1><br/>
            <img src=pokepad.png width=300 height=450>
            <p>Version 0.0.2</p>
            <p>Date: 05/07/2020</p>
            <p>Last updates at:</p>
            <a href="https://github.com/adrism6/EOI_PROJECTS/tree/master/Project4_DesktopApps">Github</a>
        </center>
    """
    QMessageBox.about(window, "About PokéPad", text)


def show_tools_dialog():
    text = """
        <b><p>Main Menu:</p></b>
            <p>- New document: Opens an empty document without an associated directory.</p>
            <p>- Open file: Opens an existing file.</p>
            <p>- Save: Saves the changes of the file. If the file is new, name it and select a directory.</p>
            <p>- Close: Closes the application.</p>
            <p>- View Menu: Click to show or close each dock widget.</p>
        <b><p>File Explorer doble click:</p></b>
            <p>- On directories: Opens and closes the directory on the treeview.</p>
            <p>- On files: Opens on the editor, if file is acceptable.</p>
        <b><p>File Explorer right click:</p></b>
            <p>- Open: Opens files on the editor, if file is acceptable.</p>
            <p>- New file: Opens an empty file with the given name and directory.</p>
            <p>- Rename: Renames the selected file and places it in the selected directory.</p>
            <p>- Delete: Deletes the selected file.</p>
        <b><p>Markdown Viewer:</p></b>
            <p>- Generates a HTML corresponding to the Markdown given in the editor.</p>
            <p>- Automatically generated when new files are opened or current file is saved.</p>
            <p>- Can update the current HTML view with the "Refresh" button.</p>
    """
    QMessageBox.about(window, "Poképad tools", text)


view_menu = window.menuBar().addMenu("&View")

help_menu = window.menuBar().addMenu("&Help")

tools_action = QAction("&Tools")
tools_action.triggered.connect(show_tools_dialog)
tools_action.setShortcut(QKeySequence("Ctrl+T"))

about_action = QAction("A&bout")
about_action.triggered.connect(show_about_dialog)
about_action.setShortcut(QKeySequence("Ctrl+B"))

help_menu.addAction(tools_action)
help_menu.addAction(about_action)


class MyTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        path = expanduser("~")
        self.tree.setRootIndex(self.model.index(path))
        self.tree.doubleClicked.connect(self.open_file)
        self.tree.setSortingEnabled(True)
        header = self.tree.header()
        header.setSectionResizeMode(3)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.context_menu)
        dockwidget = QDockWidget("File Explorer")
        dockwidget.setWidget(self.tree)
        dockwidget.setAllowedAreas(Qt.LeftDockWidgetArea)
        window.addDockWidget(Qt.LeftDockWidgetArea, dockwidget)
        view_menu.addAction(dockwidget.toggleViewAction())

    def context_menu(self):
        menu = QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        new_file = menu.addAction("New file")
        new_file.triggered.connect(self.new_file)
        rename = menu.addAction("Rename")
        rename.triggered.connect(self.rename_file)
        delete = menu.addAction("Delete")
        delete.triggered.connect(self.delete_file)
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        global file_path
        if check_is_modified() == True:
            index = self.tree.currentIndex()
            filename = self.model.filePath(index)
            isDirectory = isdir(filename)
            if isDirectory == True:
                return
            else:
                file_contents = ""
                with open(filename, "r") as f:
                    file_contents = f.read()
                editor.setPlainText(file_contents)
                file_path = filename
                webengine.markdown_to_html()

    def new_file(self):
        global file_path
        if check_is_modified() == True:
            newname, _ = QFileDialog.getSaveFileName(window, "Open as...")
            if newname:
                editor.clear()
                file_contents = ""
                with open(newname, "w") as f:
                    f.write(file_contents)
                editor.setPlainText(file_contents)
                file_path = newname
                webengine.markdown_to_html()

    def rename_file(self):
        global file_path
        if check_is_modified() == True:
            index = self.tree.currentIndex()
            filename = self.model.filePath(index)
            newname, _ = QFileDialog.getSaveFileName(window, "Rename as...")
            if newname:
                with open(filename, "r") as f:
                    with open(newname, "w") as fw:
                        for line in f:
                            fw.write(line)
                editor.document().setModified(False)
                if filename == file_path:
                    file_path = newname
                remove(filename)
                webengine.markdown_to_html()
                return True
            return False

    def delete_file(self):
        global file_path
        index = self.tree.currentIndex()
        filename = self.model.filePath(index)
        if file_path == filename:
            editor.clear()
            file_path = None
        remove(filename)
        webengine.markdown_to_html()


treeview = MyTreeView()


class MyWebEngineView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = QWebEngineView()
        refresh_button = QPushButton(window)
        refresh_button.setText("Refresh")
        refresh_button.clicked.connect(self.markdown_to_html)
        window.menuBar().setCornerWidget(refresh_button, corner=Qt.TopRightCorner)
        dockwidget = QDockWidget("Markdown Viewer")
        dockwidget.setWidget(self.view)
        dockwidget.setAllowedAreas(Qt.RightDockWidgetArea)
        dockwidget.setMinimumWidth(250)
        window.addDockWidget(Qt.RightDockWidgetArea, dockwidget)
        view_menu.addAction(dockwidget.toggleViewAction())

    def markdown_to_html(self):
        mk = Markdown()
        editor_text = editor.toPlainText()
        content = mk.convert(editor_text)
        self.view.setHtml(content)


webengine = MyWebEngineView()

window.show()
app.exec()
