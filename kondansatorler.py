#171602012 - Ender Yılmaz
#Bilişim Sistemleri Mühendisliği
#Elektronik Komponent Kayıt Kontrol Sistemi
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kondansatorler(object):
    def setupUi(self, kondansatorler):
        kondansatorler.setObjectName("kondansatorler")
        kondansatorler.resize(268, 129)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("buton_resim/kondansator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kondansatorler.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(kondansatorler)
        self.centralwidget.setObjectName("centralwidget")
        self.hesapla_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hesapla_btn.setGeometry(QtCore.QRect(190, 80, 51, 23))
        self.hesapla_btn.setObjectName("hesapla_btn")
        self.yuk = QtWidgets.QLineEdit(self.centralwidget)
        self.yuk.setGeometry(QtCore.QRect(90, 20, 151, 20))
        self.yuk.setObjectName("yuk")
        self.gerilim = QtWidgets.QLineEdit(self.centralwidget)
        self.gerilim.setGeometry(QtCore.QRect(90, 50, 151, 20))
        self.gerilim.setObjectName("gerilim")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 51, 16))
        self.label_3.setObjectName("label_3")
        self.siga_label = QtWidgets.QLabel(self.centralwidget)
        self.siga_label.setGeometry(QtCore.QRect(90, 80, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.siga_label.setFont(font)
        self.siga_label.setObjectName("siga_label")
        kondansatorler.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(kondansatorler)
        self.statusbar.setObjectName("statusbar")
        kondansatorler.setStatusBar(self.statusbar)

        self.retranslateUi(kondansatorler)
        QtCore.QMetaObject.connectSlotsByName(kondansatorler)

    def retranslateUi(self, kondansatorler):
        _translate = QtCore.QCoreApplication.translate
        kondansatorler.setWindowTitle(_translate("kondansatorler", "Kondansatör Hesaplama"))
        self.hesapla_btn.setText(_translate("kondansatorler", "Hesapla"))
        self.label.setText(_translate("kondansatorler", "Yük(q)  :"))
        self.label_2.setText(_translate("kondansatorler", "Gerilim(V) :"))
        self.label_3.setText(_translate("kondansatorler", "Sığa(C)    :"))
        self.siga_label.setText(_translate("kondansatorler", "000 F"))