# controlador_principal.py


from views.vista_principal import Ui_MainWindow
from models.modelo_principal import modelo_principal
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from PyQt5 import QtWidgets


class controlador_principal:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = modelo_principal()
        self.MainWindow = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_saludar.clicked.connect(self.saludar)
        self.ui.btn_sobre.clicked.connect(self.mostrar_sobre_nosotros)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    # Funciones especificas
    def saludar(self):
        # app = QtWidgets.QApplication(sys.argv)
        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()

        saludo = "Hola " + self.ui.txta_nombre.toPlainText()
        new_ui.lbl_main_text.setText(saludo)

        copy_mwindow = self.MainWindow
        self.block_focus(copy_mwindow)
        new_dialog.exec()

        self.ui.txta_nombre.setText("")
        self.unblock_focus(copy_mwindow)

    def block_focus(self, window):
        self.MainWindow.setEnabled(False)
        self.MainWindow.setFixedSize(window.size())

    def unblock_focus(self, window):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(self.MainWindow.maximumSizeHint())

        self.MainWindow.setEnabled(True)

    def mostrar_sobre_nosotros(self):
        from controllers.controlador_sobre_nosotros import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
