# Import files
import sys

from PyQt5.QtWidgets import QApplication
from view.SimulatorView import SimulatorView

# Main function
def main():
    app = QApplication(sys.argv)
    mainWindow = SimulatorView()
    mainWindow.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()