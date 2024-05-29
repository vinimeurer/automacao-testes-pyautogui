import pyautogui
import time
import datetime

class CadastroCargo:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroCargo\\'

    def screenshot(self, nome):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + nome)
        return screenshot

    def click_on_screen(self, screenshot, area):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        time.sleep(1)

    def preenche_cadastro(self, screenshot, area, texto):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        pyautogui.write(texto)

    def run(self):
        time.sleep(5)
        hoje = datetime.date.today()

        # TELA INICIAL
        screenshot = self.screenshot('01-telaInicial.png')
        self.click_on_screen(screenshot, (20,421,301,463))

        # BOTÃO CADASTRO CARGO
        screenshot = self.screenshot('02-cadastroCargo.png')
        self.click_on_screen(screenshot, (63,579,107,597))

        # INCLUIR NOVO CADASTRO
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (1846,123,1872,141))

        # PREENCHE CADASTRO
        screenshot = self.screenshot('04-telaCargo1.png')

        # NOME
        nome = 'Cargo ' + hoje.strftime('%d/%m/%Y')
        self.preenche_cadastro(screenshot, (709,258,1104,288), nome)
        
        # BOTÃO CONTINUAR
        self.click_on_screen(screenshot, (1654,337,1901,364))
        time.sleep(15)

        # FINALIZA O CADASTRO
        screenshot = self.screenshot('05-telaCargo2.png')
        self.click_on_screen(screenshot, (1644,549,1888,580))
        time.sleep(10)

        # VOLTA PARA TELA INICIAL
        self.click_on_screen(screenshot, (47,213,263,253))

if __name__ == "__main__":
    cadastro = CadastroCargo()
    cadastro.run()
