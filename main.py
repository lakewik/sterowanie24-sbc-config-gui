import subprocess
import sys

from PyQt4 import QtCore, QtGui
import xml.etree.cElementTree as ET
from PyQt4.QtGui import QComboBox
from PyQt4.QtGui import QHeaderView
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QStandardItemModel
import string
from sterowanie_main import Ui_Dialog


class Sterowanie24(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initialize_gpio_table ()
        QtCore.QObject.connect(self.ui.toolButton_2, QtCore.SIGNAL("clicked()"), self.save_config)
        QtCore.QObject.connect(self.ui.toolButton, QtCore.SIGNAL("clicked()"), self.start_daemon)
        # initialize combobox
        list1 = [
            self.tr("Wlaczony"),
            self.tr('Wylaczony'),

        ]
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(list1)
        print self.get_config_parametr_from_xml( "module_id")
        self.initialize_configuration()
        # GET AND SAVE TABLE GPIO DATA #
        for iterator in range(9):
            c = QComboBox()
            #print c[3].currentIndex()
            #i = self.ui.
            #self.ui.tableView.setIndexWidget(i, c)

    def get_gpio_names_list (self):
        gpios_list = []
        for x in range(self.get_usable_gpio_number()):
            gpios_list.append("GPIO "+str(x))
        return gpios_list

    def start_daemon (self):
        output = subprocess.Popen(["python", "wdaemon.py", "start"], stdout=subprocess.PIPE).communicate()[0]

    def initialize_configuration(self):
        self.ui.lineEdit_4.setText(str(self.get_config_parametr_from_xml( "module_id")))
        self.ui.lineEdit.setText(str(self.get_config_parametr_from_xml( "server_address")))
        self.ui.lineEdit_2.setText(str(self.get_config_parametr_from_xml( "server_port")))
        self.ui.lineEdit_3.setText(str(self.get_config_parametr_from_xml( "refresh_every")))
        self.ui.lineEdit_5.setText(str(self.get_config_parametr_from_xml( "module_token")))
        if int(self.get_config_parametr_from_xml( "uptime_send")) == 1:
            self.ui.checkBox.setChecked(True)
        else:
            self.ui.checkBox.setChecked(False)
        self.ui.comboBox.setCurrentIndex(int(self.get_config_parametr_from_xml( "state_high_action")))
        model = self.ui.tableView.model()
        # saving gpios configuration table #
        for x in range(self.get_usable_gpio_number()):
            lineEdits[x].setCurrentIndex( int(self.get_config_parametr_from_xml("gpio_index_config_"+str(x))))
            # end gpio config saving #


        for row in range(model.rowCount()):
            # data.append([])
            concat = str(self.get_config_parametr_from_xml("gpio_name_"+str(row)))
            index = model.index(row, 1)
            # We suppose data are strings
            # data[row].append(str(model.data(index).toString()))
            #model.
            #model.setItem(row, 2, QtGui.QTableWidgetItem( str(self.get_config_parametr_from_xml("gpio_name_"+str(x)))))
            item = QStandardItem(concat)
            item2 = QStandardItem(concat)
            model.setItem(row, 1, item)
            #model.setItem(row, 0, item2)
            #ET.SubElement(doc, "gpio_name_" + str(row), name="" + str(row)).text = str(model.data(index).toString())

            print concat
    def get_usable_gpio_number(self):
        return 16

    def get_config_parametr_from_xml(self, parametr):
        from xml.dom import minidom
        from xml.etree import ElementTree
        import lxml
        from lxml import etree
        #value = [10]
        value = [0]
        #value[0] = [0]


        et = etree.parse("uploader_config.xml")
        value[0] = str(et.xpath("/mainconfig/configdata/"+str(parametr)+"/text()"))
        value[0] = string.replace(value[0], ']', '')
        value[0] = string.replace(value[0], "'", '')

        return string.replace(value[0], '[', '')
        #value
        #document = ElementTree.parse('uploader_config.xml')
        # Open XML document using minidom parser
        #DOMTree = minidom.parse('uploader_config.xml')

        # pobieramy elementy struktury dokumentu XML
        #cNodes = DOMTree.childNodes
        #for i in cNodes[0].getElementsByTagName("configdata"):
            # nazwa taga
            # return i.getElementsByTagName(parametr)[0].nodeName


        #for main_tag in document.findall('mainconfig/configdata'):
            # testname = main_tag.find('.//'+str(parametr))
            # return 'TestName:'


    def save_config (self):
         # function to save configuration to xml


         root = ET.Element("mainconfig")
         doc = ET.SubElement(root, "configdata")
         server_address = self.ui.lineEdit.text()
         server_port = self.ui.lineEdit_2.text()
         refresh = self.ui.lineEdit_3.text()
         module_id = self.ui.lineEdit_4.text()
         module_token = self.ui.lineEdit_5.text()
         print lineEdits[3].currentIndex()

         if self.ui.checkBox.isChecked():
             uptime_send = "1"
         else:
             uptime_send = "0"
         state_high = str(self.ui.comboBox.currentIndex())



         ET.SubElement(doc, "server_address").text = str(server_address)
         ET.SubElement(doc, "server_port").text = str(server_port)
         ET.SubElement(doc, "refresh_every").text = str(refresh)
         ET.SubElement(doc, "module_id").text = str(module_id)
         ET.SubElement(doc, "module_token").text = str(module_token)
         ET.SubElement(doc, "uptime_send").text = str(uptime_send)
         ET.SubElement(doc, "state_high_action").text = str(state_high)
         #ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

        # saving gpios configuration table #
         for x in range(self.get_usable_gpio_number()):
             ET.SubElement(doc, "gpio_index_config_"+str(x), name="GPIO24").text = str(lineEdits[x].currentIndex())
        # end gpio config saving #



        # controlled gpios names saving #
         model = self.ui.tableView.model()
         #data = []
        
         for row in range(model.rowCount()):
            #data.append([])

            index = model.index(row, 1)

            # We suppose data are strings
            #data[row].append(str(model.data(index).toString()))
            ET.SubElement(doc, "gpio_name_" + str(row), name=""+str(row)).text = str(model.data(index).toString())

            print str(model.data(index).toString())



         tree = ET.ElementTree(root)
         tree.write("uploader_config.xml")

    def initialize_gpio_table (self):


        gpio_range = int(self.get_usable_gpio_number())
        global lineEdits
        lineEdits = {}
        for x in range(gpio_range):
            lineEdits[x] = 0
        model = QStandardItemModel(gpio_range, 3) # second parametr - column count
        for row in range(gpio_range):
            for column in range(3): # column count
                item = QStandardItem("Kanal sterujacy %d" % (row+1))
                model.setItem(row, column, item)
        model.setHorizontalHeaderLabels(['Kanal sterowania', 'Nazwa sterowanego kanalu', 'Wybierz GPIO'])
        self.ui.tableView.setModel(model)
        for row in range(gpio_range):



            #lineEdits[3].setText("My new text")
            c = QComboBox()
            c.addItems(self.get_gpio_names_list())
            #GPIO_combo = QtGui.QLineEdit("myLineEdit")
            lineEdits[row] = c
            i = self.ui.tableView.model().index(row, 2)
            self.ui.tableView.setIndexWidget(i, c)
            width = self.ui.tableView.size().width()
            self.ui.tableView.setColumnWidth(2, width * 0.30)
            self.ui.tableView.setColumnWidth(0, width * 0.30)
            self.ui.tableView.setColumnWidth(1, width * 0.35)
            #self.ui.tableView.setHorizontalHeader(['Kanal sterowania', '2', 'Wybierz GPIO', '4', '5'])
    #def initialize_gpio_table (self):


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Sterowanie24()
    myapp.show()
    sys.exit(app.exec_())
