#171602012 - Ender Yılmaz
#Bilişim Sistemleri Mühendisliği
#Elektronik Komponent Kayıt Kontrol Sistemi
from PyQt5.QtWidgets import *
import sys
from menu import Ui_menu
from direncler import Ui_direncler
from kondansatorler import Ui_kondansatorler
from komponentler import Ui_komponentler
from bobinler import Ui_bobinler
import sqlite3

class komponent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_komponentler()
        self.ui.setupUi(self)
        self.listele()

        self.ui.listele_btn.clicked.connect(self.ozelListele)
        self.ui.ekle_btn.clicked.connect(self.ekle)
        self.ui.sil_btn.clicked.connect(self.sil)
        self.ui.guncelle_btn.clicked.connect(self.guncelle)
        self.ui.ara_btn.clicked.connect(self.ara)
        self.ui.temizle_btn.clicked.connect(self.temizle)
        self.ui.liste.cellClicked.connect(self.veriSec)
        
    gtur = ""
    gdeger = ""
    gstok = ""

    def listele(self):
    	baglanti = sqlite3.connect('veri_tabani.sqlite')
    	sorgu = baglanti.execute("SELECT * FROM komponent")
    	self.ui.liste.setRowCount(0)
    	for satir_no, satir_veri in enumerate(sorgu):
    		self.ui.liste.insertRow(satir_no)
    		for sutun_no, veri in enumerate(satir_veri):
    			self.ui.liste.setItem(satir_no, sutun_no, QTableWidgetItem(str(veri)))
    	baglanti.close()

    def ozelListele(self):
    	ozel_tur = self.ui.ozel_tur.currentText()
    	if(ozel_tur == "Tümü"):
    		self.listele()
    	else:
    		baglanti = sqlite3.connect('veri_tabani.sqlite')
    		sorgu = baglanti.execute("SELECT * FROM komponent WHERE tur='{}'".format(ozel_tur))
    		self.ui.liste.setRowCount(0)
    		for satir_no, satir_veri in enumerate(sorgu):
    			self.ui.liste.insertRow(satir_no)
    			for sutun_no, veri in enumerate(satir_veri):
    				self.ui.liste.setItem(satir_no, sutun_no, QTableWidgetItem(str(veri)))
    		baglanti.close()

    def ara(self):
    	ara = self.ui.ara.text()
    	baglanti = sqlite3.connect('veri_tabani.sqlite')
    	sorgu = baglanti.execute("SELECT * FROM komponent WHERE tur LIKE '%{}%' OR deger LIKE '%{}%' OR stok LIKE '%{}%'".format(ara,ara,ara))
    	self.ui.liste.setRowCount(0)
    	for satir_no, satir_veri in enumerate(sorgu):
    		self.ui.liste.insertRow(satir_no)
    		for sutun_no, veri in enumerate(satir_veri):
    			self.ui.liste.setItem(satir_no, sutun_no, QTableWidgetItem(str(veri)))
    	baglanti.close()
    
    def ekle(self):
    	tur = self.ui.tur.currentText()
    	deger = self.ui.deger.text()
    	stok = self.ui.stok.text()
    	baglanti = sqlite3.connect('veri_tabani.sqlite')
    	ekle = baglanti.cursor()
    	ekle.execute("INSERT INTO komponent VALUES ('{}', '{}', '{}')".format(tur,deger,stok))
    	baglanti.commit()
    	baglanti.close()
    	self.listele()

    def sil(self):
    	baglanti = sqlite3.connect('veri_tabani.sqlite')
    	sil = baglanti.cursor()
    	sil.execute("DELETE FROM komponent WHERE tur='{}' AND deger='{}' AND stok='{}'".format(self.gtur,self.gdeger,self.gstok))
    	baglanti.commit()
    	baglanti.close()
    	self.listele()
    
    def guncelle(self):
    	tur = self.ui.tur.currentText()
    	deger = self.ui.deger.text()
    	stok = self.ui.stok.text()
    	baglanti = sqlite3.connect('veri_tabani.sqlite')
    	guncelle = baglanti.cursor()
    	guncelle.execute("UPDATE komponent SET tur='{}', deger='{}', stok='{}' WHERE tur='{}' AND deger='{}' AND stok='{}'".format(tur,deger,stok,self.gtur,self.gdeger,self.gstok))
    	baglanti.commit()
    	baglanti.close()
    	self.listele()

    def veriSec(self, satir, sutun):
    	tur = self.ui.liste.item(satir, 0)
    	deger = self.ui.liste.item(satir, 1)
    	stok = self.ui.liste.item(satir, 2)
    	self.gtur = tur.text()
    	self.gdeger = deger.text()
    	self.gstok = stok.text()
    	self.ui.tur.setCurrentText(tur.text())
    	self.ui.deger.setText(deger.text())
    	self.ui.stok.setText(stok.text())
    
    def temizle(self):
    	self.ui.deger.clear()
    	self.ui.stok.clear()
    	self.ui.ara.clear()
    	self.gtur = ""
    	self.gdeger = ""
    	self.gstok = ""

class direnc(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_direncler()
		self.ui.setupUi(self)

		self.ui.hesapla1_btn.clicked.connect(self.direncHesapla1)
		self.ui.hesapla2_btn.clicked.connect(self.direncHesapla2)
		self.ui.hesapla3_btn.clicked.connect(self.direncHesapla3)

	renk_deger = {"Siyah":0,"Kahve":1,"Kırmızı":2, "Turuncu":3, "Sarı":4,"Yeşil":5,"Mavi":6,"Mor":7, "Gri":8, "Beyaz":9, "Altın":"5%", "Gümüş":"10%"}

	def direncHesapla1(self):
		bant1 = self.ui.bant1.currentText()
		bant2 = self.ui.bant2.currentText()
		carpan = self.ui.carpan.currentText()
		tolerans = self.ui.tolerans.currentText()
		direnc = int(str(self.renk_deger[bant1])+str(self.renk_deger[bant2]))*(10**self.renk_deger[carpan])
		self.ui.direnc1_label.setText("{} ohm {} Tolerans".format(direnc,self.renk_deger[tolerans]))
	
	def direncHesapla2(self):
		ozdirenc = int(self.ui.ozdirenc.text())
		uzunluk = int(self.ui.uzunluk.text())
		kesitalan = int(self.ui.kesitalan.text())
		if(kesitalan == 0):
			self.ui.direnc2_label.setText("Kesit Alan 0 Olamaz")
		else:
			direnc = (ozdirenc*uzunluk)/kesitalan
			self.ui.direnc2_label.setText("{:0.2f} ohm".format(direnc))

	def direncHesapla3(self):
		gerilim = int(self.ui.gerilim.text())
		akim = int(self.ui.akim.text())
		if(akim == 0):
			self.ui.direnc3_label.setText("Akım 0 Olamaz")
		else:
			direnc = gerilim/akim
			self.ui.direnc3_label.setText("{:0.2f} ohm".format(direnc))

class kondansator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_kondansatorler()
		self.ui.setupUi(self)

		self.ui.hesapla_btn.clicked.connect(self.sigaHesapla)

	def sigaHesapla(self):
		yuk = int(self.ui.yuk.text())
		gerilim = int(self.ui.gerilim.text())
		if(gerilim == 0):
			self.ui.siga_label.setText("Gerilim 0 Olamaz")
		else:
			siga = yuk/gerilim
			self.ui.siga_label.setText("{:0.2f} F".format(siga))

class bobin(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_bobinler()
		self.ui.setupUi(self)

		self.ui.hesapla_btn.clicked.connect(self.enduktansHesapla)

	def enduktansHesapla(self):
		mgecirgenlik = int(self.ui.mgecirgenlik.text())
		sarim = int(self.ui.sarim.text())
		kesitalan = int(self.ui.kesitalan.text())
		uzunluk = int(self.ui.uzunluk.text())
		if(uzunluk == 0):
			self.ui.enduktans_label.setText("Uzunluk 0 Olamaz")
		else:
			enduktans = (mgecirgenlik*(sarim**2)*kesitalan)/uzunluk
			self.ui.enduktans_label.setText("{:0.2f} H".format(enduktans))

class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu()
        self.ui.setupUi(self)
        self.drnc = direnc()
        self.kndstr = kondansator()
        self.bbn = bobin()
        self.kmpnt = komponent()

        
        self.ui.direnc_btn.clicked.connect(self.drnc_ac)
        self.ui.kondansator_btn.clicked.connect(self.kndstr_ac)
        self.ui.bobin_btn.clicked.connect(self.bbn_ac)
        self.ui.komponent_btn.clicked.connect(self.kmpnt_ac)
        self.ui.cikis_btn.clicked.connect(self.cikis)
       
    
    def drnc_ac(self):
    	self.drnc.show()
    def kndstr_ac(self):
    	self.kndstr.show()
    def bbn_ac(self):
    	self.bbn.show()
    def kmpnt_ac(self):
    	self.kmpnt.show()
    def cikis(self):
    	sys.exit()

def main():
    app = QApplication(sys.argv)
    main = menu()
    main.show()
    sys.exit(app.exec_())

main()