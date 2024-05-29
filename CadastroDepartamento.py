import pyautogui
import time
import datetime

class CadastroDepartamento:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroDepartamento\\'

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

        # TELA INICIAL
        screenshot = self.screenshot('01-telaInicial.png')
        self.click_on_screen(screenshot, (20,421,301,463))

        # BOTÃO CADASTRO CARGO
        screenshot = self.screenshot('02-cadastroDepartamento.png')
        self.click_on_screen(screenshot, (64,616,154,633))

        # INCLUIR NOVO CADASTRO
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (1846,123,1871,140))

        # PREENCHE CADASTRO
        screenshot = self.screenshot('04-telaDepartamento1.png')

        # NOME
        hoje = datetime.date.today()
        nome = 'Departamento ' + hoje.strftime('%d/%m/%Y')
        self.preenche_cadastro(screenshot, (501,253,901,287), nome)
        
        # SIGLA
        self.preenche_cadastro(screenshot, (920,253,1320,287), 'D')
        
        # BOTÃO CONTINUAR
        self.click_on_screen(screenshot, (1660,328,1901,364))
        time.sleep(10)

        # FINALIZA O CADASTRO
        screenshot = self.screenshot('05-telaDepartamento2.png')
        self.click_on_screen(screenshot, (1644,549,1888,580))
        time.sleep(10)
        
        # VOLTA PARA TELA INICIAL
        self.click_on_screen(screenshot, (47,213,263,253))

if __name__ == "__main__":
    cadastro = CadastroDepartamento()
    cadastro.run()
