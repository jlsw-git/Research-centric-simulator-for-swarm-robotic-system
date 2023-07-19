-------------------------------
Required Software Installation:
-------------------------------
1. Download Python 3.9 https://www.python.org/downloads/release/python-390/
    Note: pyqt5 is stable with Python 3.9.x

2. Install pip by running the following commands in command prompt:
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

    or manually install pip:
    1. Download and save https://bootstrap.pypa.io/get-pip.py into the same directory as Python
    2. In command prompt, use the cd command and navigate to the directory where Python is installed.
    3. Run the command: python get-pip.py

3. Install necessary packages: pyqt5-tools, opencv, pyautogui, Pillow, matplotlib
    Run these commands in command prompt:
        pip install pyqt5-tools
        pip install opencv-python
        pip install PyAutoGUI
        pip install Pillow
        pip install matplotlib

    Alternatively, an IDE such as PyCharm can be used to install the packages.


-----------------------------
How to run simulator program:
-----------------------------
1. Run main file: SwarmRoboticsSimulator.py


-----------------
Additional Notes:
-----------------
- Files with different file formats are provided in the testFiles folder for dragging and dropping into simulator.
- The only valid file format for dragging and dropping into the simulator is Python files (.py).
- The parameters folder is used to store JSON parameter files.
- The recordings folder is used to store video recordings in mp4 format.
