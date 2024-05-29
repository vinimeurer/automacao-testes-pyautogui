import pyautogui
import time
import datetime
from GeraDocs import GeraDocs

class CadastroEmpresa:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroEmpresa\\'

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

        # BOTÃO CADASTRO EMPRESA
        screenshot = self.screenshot('02-cadastroEmpresa.png')
        self.click_on_screen(screenshot, (55,472,146,499))

        # INCLUIR NOVO CADASTRO
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (1839,118,1876,148))

        # PREENCHE CADASTRO
        screenshot = self.screenshot('04-telaEmpresa.png')

        # NOME
        nome = 'Empresa ' + hoje.strftime('%d/%m/%Y')
        self.preenche_cadastro(screenshot, (503,484,894,518), nome)

        # NUMERO DOCUMENTO
        cnpj = GeraDocs.generate_cnpj()
        self.preenche_cadastro(screenshot, (1331,486,1722,520), cnpj)

        # CODIGO INTERNO
        cod_interno = hoje.strftime('%d%m%Y')
        self.preenche_cadastro(screenshot, (502,561,893,595), cod_interno)

        # SIGLA
        self.preenche_cadastro(screenshot, (923,561,1314,595), 'T')

        # ENDEREÇO
        self.preenche_cadastro(screenshot, (921,709,1312,743), 'Endereco')

        # CIDADE
        self.preenche_cadastro(screenshot, (1339,711,1730,745), 'Cidade')

        # BAIRRO
        self.preenche_cadastro(screenshot, (501,808,892,842), 'Bairro')

        # ESTADO
        self.preenche_cadastro(screenshot, (918,814,1309,848), 'Estado')

        # PAÍS
        self.preenche_cadastro(screenshot, (1337,809,1728,843), 'Pais')

        # TIPO DOCUMENTO
        screenshot = self.screenshot('05-tipoDocumento.png')
        self.click_on_screen(screenshot, (915,487,1311,514))
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + '05-tipoDocumento.png')
        self.click_on_screen(screenshot, (925,581,972,603))
        time.sleep(1)

        # FINALIZA
        self.click_on_screen(screenshot, (1653,869,1893,899))
        time.sleep(10)
        
        # VOLTA PARA TELA INICIAL
        self.click_on_screen(screenshot, (47,213,263,253))
        
if __name__ == "__main__":
    cadastro = CadastroEmpresa()
    cadastro.run()
