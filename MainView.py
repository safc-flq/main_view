import sys
import snap7
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from snap7 import util
from UI import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        window = QWidget()
        self.ui.plc = snap7.client.Client()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.plc_link)
        self.ui.pushButton_2.clicked.connect(self.plc_dislink)
        self.ui.pushButton_5.clicked.connect(self.rol_send)
        self.ui.pushButton_3.pressed.connect(self.forward_on)
        self.ui.pushButton_3.released.connect(self.forward_off)
        self.ui.pushButton_4.pressed.connect(self.backward_on)
        self.ui.pushButton_4.released.connect(self.backward_off)

        self.ui.pushButton_8.clicked.connect(self.hor_send)
        self.ui.pushButton_7.pressed.connect(self.hor_forward_on)
        self.ui.pushButton_7.released.connect(self.hor_forward_off)
        self.ui.pushButton_6.pressed.connect(self.hor_backward_on)
        self.ui.pushButton_6.released.connect(self.hor_backward_off)

        self.ui.pushButton_11.clicked.connect(self.ver_send)
        self.ui.pushButton_10.pressed.connect(self.ver_forward_on)
        self.ui.pushButton_10.released.connect(self.ver_forward_off)
        self.ui.pushButton_9.pressed.connect(self.ver_backward_on)
        self.ui.pushButton_9.released.connect(self.ver_backward_off)


    def plc_link(self):
        # add = str(self.lineEdit.text)
        # try:
        #     ip_text = self.ui.lineEdit.text()
        #     rack_text = self.ui.lineEdit_2.text()
        #     rack = int(rack_text)
        #     slot_text = self.ui.lineEdit_3.text()
        #     slot = int(slot_text)
        #     self.ui.plc.connect(ip_text, rack, slot, 102)
        #     print(ip_text)
        #     print(rack)
        #     print(slot)
        #     link = self.ui.plc.get_connected()
        #     print(link)
        #     if link:
        #         self.ui.pushButton.setEnabled(False)
        #         QMessageBox.information(window, "信息提示框", "连接成功")
        # except:
        #     pass

        ip_text = self.ui.lineEdit.text()
        rack_text = self.ui.lineEdit_2.text()
        rack = int(rack_text)
        slot_text = self.ui.lineEdit_3.text()
        slot = int(slot_text)
        self.ui.plc.connect(ip_text, rack, slot, 102)
        print(ip_text)
        print(rack)
        print(slot)
        link = self.ui.plc.get_connected()
        print(link)
        if link:
            self.ui.pushButton.setEnabled(False)
            QMessageBox.information(window, "信息提示框", "连接成功")


    def plc_dislink(self):
        self.ui.plc.disconnect()
        link = self.ui.plc.get_connected()
        self.ui.pushButton.setEnabled(True)
        QMessageBox.information(window, "信息提示框", "断开连接")
        print(link)

    def rol_send(self):
        print(self.ui.lineEdit_6.text())
        realData = bytearray(4)
        util.set_real(realData, 0, self.ui.lineEdit_6.text())
        self.ui.plc.db_write(2, 14, realData)

        realData2 = bytearray(4)
        util.set_real(realData2, 0, self.ui.lineEdit_5.text())
        self.ui.plc.db_write(2, 6, realData2)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, True)
        self.ui.plc.db_write(2, 44, boolData)

    def forward_on(self):
        print(self.ui.lineEdit_4.text())
        realData3 = bytearray(4)
        util.set_real(realData3, 0, self.ui.lineEdit_4.text())
        self.ui.plc.db_write(2, 2, realData3)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 1, True)
        self.ui.plc.db_write(2, 0, boolData)

    def forward_off(self):
            boolData = bytearray(1)
            util.set_bool(boolData, 0, 1, False)
            self.ui.plc.db_write(2, 0, boolData)   

    def backward_on(self):
        print(self.ui.lineEdit_4.text())
        realData3 = bytearray(4)
        util.set_real(realData3, 0, self.ui.lineEdit_4.text())
        self.ui.plc.db_write(2, 2, realData3)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, True)
        self.ui.plc.db_write(2, 0, boolData)   

    def backward_off(self):
            boolData = bytearray(1)
            util.set_bool(boolData, 0, 2, False)
            self.ui.plc.db_write(2, 0, boolData)      


    def ver_send(self):
        print(self.ui.lineEdit_12.text())
        realData = bytearray(4)
        util.set_real(realData, 0, self.ui.lineEdit_12.text())
        self.ui.plc.db_write(2, 52, realData)

        realData2 = bytearray(4)
        util.set_real(realData2, 0, self.ui.lineEdit_11.text())
        self.ui.plc.db_write(2, 60, realData2)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 3, True)
        self.ui.plc.db_write(2, 46, boolData)

    def ver_forward_on(self):
        print(self.ui.lineEdit_10.text())
        realData3 = bytearray(4)
        util.set_real(realData3, 0, self.ui.lineEdit_10.text())
        self.ui.plc.db_write(2, 48, realData3)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 1, True)
        self.ui.plc.db_write(2, 46, boolData)

    def ver_forward_off(self):
        boolData = bytearray(1)
        util.set_bool(boolData, 0, 1, False)
        self.ui.plc.db_write(2, 46, boolData)   

    def ver_backward_on(self):
        print(self.ui.lineEdit_10.text())
        realData3 = bytearray(4)
        util.set_real(realData3, 0, self.ui.lineEdit_10.text())
        self.ui.plc.db_write(2, 48, realData3)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, True)
        self.ui.plc.db_write(2, 46, boolData)   

    def ver_backward_off(self):
        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, False)
        self.ui.plc.db_write(2, 46, boolData)  


    def hor_send(self):
        print(self.ui.lineEdit_9.text())
        #水平移动速度
        realData4 = bytearray(4)
        util.set_real(realData4, 0, self.ui.lineEdit_9.text())
        self.ui.plc.db_write(2, 90, realData4)

        #水平移动距离
        realData5 = bytearray(4)
        util.set_real(realData5, 0, self.ui.lineEdit_8.text())
        self.ui.plc.db_write(2, 98, realData5)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 3, True)
        self.ui.plc.db_write(2, 4, boolData)

    def hor_forward_on(self):
        print(self.ui.lineEdit_7.text())
        realData6 = bytearray(4)
        util.set_real(realData6, 0, self.ui.lineEdit_7.text())
        self.ui.plc.db_write(2, 86, realData6)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 1, True)
        self.ui.plc.db_write(2, 84, boolData)

    def hor_forward_off(self):
        boolData = bytearray(1)
        util.set_bool(boolData, 0, 1, False)
        self.ui.plc.db_write(2, 84, boolData)   

    def hor_backward_on(self):
        print(self.ui.lineEdit_7.text())
        realData3 = bytearray(4)
        util.set_real(realData3, 0, self.ui.lineEdit_7.text())
        self.ui.plc.db_write(2, 86, realData3)

        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, True)
        self.ui.plc.db_write(2, 84, boolData)   

    def hor_backward_off(self):
        boolData = bytearray(1)
        util.set_bool(boolData, 0, 2, False)
        self.ui.plc.db_write(2, 84, boolData)    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())