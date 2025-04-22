import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QListWidget, QWidget, QGridLayout, QListWidgetItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont


# Import the UI class from the main_ui module
from main_ui import Ui_MainWindow


# Defning a custom Mainwindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI from the generated 'untitled_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("Questions")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("./assets/menu.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.list_widget_content_only
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon = self.ui.list_widget_icon_only
        self.side_menu_icon.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.menubtn = self.ui.pushButton
        self.menubtn.setObjectName("menu_button")
        self.menubtn.setText("")
        self.menubtn.setIcon(QIcon("./assets/close.png"))
        self.menubtn.setCheckable(True)
        self.menubtn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        # Define a list of muni itmes with names and icons
        self.menu_list = [
            {
                "name": "Staging",
                "icon": "./assets/staging.svg"
            },
            {
                "name": "Local",
                "icon": "./assets/local.svg"
            },
            {
                "name": "Remote",
                "icon": "./assets/remote.svg"
            },
            {
                "name": "Branches",
                "icon": "./assets/branch.svg"
            },
            {
                "name": "Pull Requests",
                "icon": "./assets/pull_request.svg"
            }
        ]

        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_signal_slot()
        self.init_stackwidget()

    def init_signal_slot(self):
        # Connect the signals and slots for menu button and side menu
        self.menubtn.toggled["bool"].connect(self.side_menu.setHidden)
        self.menubtn.toggled["bool"].connect(self.title_label.setHidden)
        self.menubtn.toggled["bool"].connect(self.title_icon.setHidden)
        self.menubtn.toggled["bool"].connect(self.side_menu_icon.setVisible)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon.currentRowChanged["int"].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged["int"].connect(self.side_menu_icon.setCurrentRow)
        self.side_menu_icon.currentRowChanged["int"].connect(self.side_menu.setCurrentRow)

        self.menubtn.toggled.connect(self.button_icon_change)


    def button_icon_change(self, status):
        # Change the icon of the menu button based on its state
        if status:
            self.menubtn.setIcon(QIcon("./assets/menu.png"))
        else:
            self.menubtn.setIcon(QIcon("./assets/close.png"))


    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu.clear()
        self.side_menu_icon.clear()

        for menu in self.menu_list:
            # Add items to the side menu with text and icon
            item = QListWidgetItem()
            item.setIcon(QIcon(menu["icon"]))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon.addItem(item)
            self.side_menu_icon.setCurrentRow(0)

            # Add items to the side menu with icons only
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu["icon"]))
            item_new.setText(menu["name"])
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)


    def init_stackwidget(self):
        # Initialize the stack widget with pages
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        for menu in self.menu_list:
            text = menu["name"]
            layout = QGridLayout()
            label = QLabel(text=text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            font = QFont()
            font.setPixelSize(20)
            label.setFont(font)
            layout.addWidget(label)
            new_page = QWidget()
            new_page.setLayout(layout)
            self.main_content.addWidget(new_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open ("style.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())