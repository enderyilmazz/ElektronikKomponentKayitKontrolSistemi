#171602012 - Ender Yılmaz
#Bilişim Sistemleri Mühendisliği
#Elektronik Komponent Kayıt Kontrol Sistemi
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_direncler(object):
    def setupUi(self, direncler):
        direncler.setObjectName("direncler")
        direncler.resize(522, 230)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("buton_resim/direnc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        direncler.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(direncler)
        self.centralwidget.setObjectName("centralwidget")
        self.bant1 = QtWidgets.QComboBox(self.centralwidget)
        self.bant1.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.bant1.setObjectName("bant1")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.bant1.addItem("")
        self.carpan = QtWidgets.QComboBox(self.centralwidget)
        self.carpan.setGeometry(QtCore.QRect(210, 30, 91, 22))
        self.carpan.setObjectName("carpan")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.carpan.addItem("")
        self.tolerans = QtWidgets.QComboBox(self.centralwidget)
        self.tolerans.setGeometry(QtCore.QRect(310, 30, 91, 22))
        self.tolerans.setObjectName("tolerans")
        self.tolerans.addItem("")
        self.tolerans.addItem("")
        self.bant2 = QtWidgets.QComboBox(self.centralwidget)
        self.bant2.setGeometry(QtCore.QRect(110, 30, 91, 22))
        self.bant2.setObjectName("bant2")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.bant2.addItem("")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 81, 16))
        self.label_4.setObjectName("label_4")
        self.hesapla1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla1_btn.setGeometry(QtCore.QRect(410, 30, 101, 23))
        self.hesapla1_btn.setObjectName("hesapla1_btn")
        self.direnc1_label = QtWidgets.QLabel(self.centralwidget)
        self.direnc1_label.setGeometry(QtCore.QRect(350, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.direnc1_label.setFont(font)
        self.direnc1_label.setObjectName("direnc1_label")
        self.ozdirenc = QtWidgets.QLineEdit(self.centralwidget)
        self.ozdirenc.setGeometry(QtCore.QRect(90, 90, 161, 20))
        self.ozdirenc.setObjectName("ozdirenc")
        self.uzunluk = QtWidgets.QLineEdit(self.centralwidget)
        self.uzunluk.setGeometry(QtCore.QRect(90, 120, 161, 20))
        self.uzunluk.setObjectName("uzunluk")
        self.kesitalan = QtWidgets.QLineEdit(self.centralwidget)
        self.kesitalan.setGeometry(QtCore.QRect(90, 150, 161, 20))
        self.kesitalan.setObjectName("kesitalan")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_8.setObjectName("label_8")
        self.hesapla2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla2_btn.setGeometry(QtCore.QRect(200, 180, 51, 23))
        self.hesapla2_btn.setObjectName("hesapla2_btn")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.label_9.setObjectName("label_9")
        self.direnc2_label = QtWidgets.QLabel(self.centralwidget)
        self.direnc2_label.setGeometry(QtCore.QRect(90, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.direnc2_label.setFont(font)
        self.direnc2_label.setObjectName("direnc2_label")
        self.gerilim = QtWidgets.QLineEdit(self.centralwidget)
        self.gerilim.setGeometry(QtCore.QRect(350, 90, 161, 20))
        self.gerilim.setObjectName("gerilim")
        self.akim = QtWidgets.QLineEdit(self.centralwidget)
        self.akim.setGeometry(QtCore.QRect(350, 120, 161, 20))
        self.akim.setObjectName("akim")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 90, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(290, 120, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 150, 51, 16))
        self.label_12.setObjectName("label_12")
        self.direnc3_label = QtWidgets.QLabel(self.centralwidget)
        self.direnc3_label.setGeometry(QtCore.QRect(350, 150, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.direnc3_label.setFont(font)
        self.direnc3_label.setObjectName("direnc3_label")
        self.hesapla3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla3_btn.setGeometry(QtCore.QRect(460, 150, 51, 23))
        self.hesapla3_btn.setObjectName("hesapla3_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 60, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        direncler.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(direncler)
        self.statusbar.setObjectName("statusbar")
        direncler.setStatusBar(self.statusbar)

        self.retranslateUi(direncler)
        QtCore.QMetaObject.connectSlotsByName(direncler)

    def retranslateUi(self, direncler):
        _translate = QtCore.QCoreApplication.translate
        direncler.setWindowTitle(_translate("direncler", "Direnç Hesaplama"))
        self.bant1.setItemText(0, _translate("direncler", "Siyah"))
        self.bant1.setItemText(1, _translate("direncler", "Kahve"))
        self.bant1.setItemText(2, _translate("direncler", "Kırmızı"))
        self.bant1.setItemText(3, _translate("direncler", "Turuncu"))
        self.bant1.setItemText(4, _translate("direncler", "Sarı"))
        self.bant1.setItemText(5, _translate("direncler", "Yeşil"))
        self.bant1.setItemText(6, _translate("direncler", "Mavi"))
        self.bant1.setItemText(7, _translate("direncler", "Mor"))
        self.bant1.setItemText(8, _translate("direncler", "Gri"))
        self.bant1.setItemText(9, _translate("direncler", "Beyaz"))
        self.carpan.setItemText(0, _translate("direncler", "Siyah"))
        self.carpan.setItemText(1, _translate("direncler", "Kahve"))
        self.carpan.setItemText(2, _translate("direncler", "Kırmızı"))
        self.carpan.setItemText(3, _translate("direncler", "Turuncu"))
        self.carpan.setItemText(4, _translate("direncler", "Sarı"))
        self.carpan.setItemText(5, _translate("direncler", "Yeşil"))
        self.carpan.setItemText(6, _translate("direncler", "Mavi"))
        self.tolerans.setItemText(0, _translate("direncler", "Altın"))
        self.tolerans.setItemText(1, _translate("direncler", "Gümüş"))
        self.bant2.setItemText(0, _translate("direncler", "Siyah"))
        self.bant2.setItemText(1, _translate("direncler", "Kahve"))
        self.bant2.setItemText(2, _translate("direncler", "Kırmızı"))
        self.bant2.setItemText(3, _translate("direncler", "Turuncu"))
        self.bant2.setItemText(4, _translate("direncler", "Sarı"))
        self.bant2.setItemText(5, _translate("direncler", "Yeşil"))
        self.bant2.setItemText(6, _translate("direncler", "Mavi"))
        self.bant2.setItemText(7, _translate("direncler", "Mor"))
        self.bant2.setItemText(8, _translate("direncler", "Gri"))
        self.bant2.setItemText(9, _translate("direncler", "Beyaz"))
        self.label_1.setText(_translate("direncler", "1. Bant Değer"))
        self.label_2.setText(_translate("direncler", "2. Bant Değer"))
        self.label_3.setText(_translate("direncler", "3. Bant Çarpan"))
        self.label_4.setText(_translate("direncler", "4. Bant Tolerans"))
        self.hesapla1_btn.setText(_translate("direncler", "Hesapla"))
        self.direnc1_label.setText(_translate("direncler", "00000000 ohm %0Tolerans"))
        self.label_6.setText(_translate("direncler", "Özdirenç        :"))
        self.label_7.setText(_translate("direncler", "Tel Uzunluğu  :"))
        self.label_8.setText(_translate("direncler", "Tel Kesit Alan :"))
        self.hesapla2_btn.setText(_translate("direncler", "Hesapla"))
        self.label_9.setText(_translate("direncler", "Direnç            :"))
        self.direnc2_label.setText(_translate("direncler", "00000000 ohm"))
        self.label_10.setText(_translate("direncler", "Gerilim(V) :"))
        self.label_11.setText(_translate("direncler", "Akım(I)     :"))
        self.label_12.setText(_translate("direncler", "Direnç(R) :"))
        self.direnc3_label.setText(_translate("direncler", "00000000 ohm"))
        self.hesapla3_btn.setText(_translate("direncler", "Hesapla"))
        self.label_5.setText(_translate("direncler", "Direnç      :"))