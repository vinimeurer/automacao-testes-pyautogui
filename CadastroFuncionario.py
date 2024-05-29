import pyautogui
import time
import datetime
from GeraDocs import GeraDocs
from GeraDocs import geradorDePisPasep

class CadastroFuncionario:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroFuncionario\\'

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
        screenshot = self.screenshot('02-cadastroFuncionario.png')
        self.click_on_screen(screenshot, (58,544,143,563))

        # INCLUIR NOVO CADASTRO
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (1890,122,1909,146))
        time.sleep(2)

        # PREENCHE CADASTRO
        screenshot = self.screenshot('04-telaFuncionario1.png')

        # NOME
        nome = 'Teste ' + hoje.strftime('%d/%m/%Y')
        self.preenche_cadastro(screenshot, (880,287,1287,324), nome)

        # NUMERO CPF
        cpf = GeraDocs.generate_cpf()
        self.preenche_cadastro(screenshot, (1309,286,1504,324), cpf)

        # NUMERO PIS
        pis = geradorDePisPasep(False)
        self.preenche_cadastro(screenshot, (1094,368,1289,406), pis)
        
        # VINCULA EMPRESA
        pesquisa = hoje.strftime('%d/%m/%Y')
        self.click_on_screen(screenshot, (700,528,1108,563))
        screenshot = self.screenshot('05-selecionaEmpresa.png')
        self.preenche_cadastro(screenshot,(708,576,1099,610),pesquisa)
        self.click_on_screen(screenshot,(712,624,1103,658))
        
        # DATA ADMISSÂO
        screenshot = self.screenshot('04-telaFuncionario1.png')
        self.click_on_screen(screenshot, (698,611,891,638))
        screenshot = self.screenshot('06-telaData.png')
        self.click_on_screen(screenshot, (1107,701,1185,720))

        # MATRICULA
        screenshot = self.screenshot('04-telaFuncionario1.png')
        matricula = hoje.strftime('%d%m%Y')
        self.preenche_cadastro(screenshot, (1128,606,1323,644), matricula)
        time.sleep(1)
        
        # SCROLL PARA O FINAL DA TELA
        pyautogui.scroll(-5000)
        
        # VINCULA HORARIO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        pesquisa = hoje.strftime('%d/%m/%Y')
        self.click_on_screen(screenshot, (700,240,894,272))
        screenshot = self.screenshot('08-selecionaHorario.png')
        self.preenche_cadastro(screenshot,(706,286,883,318),pesquisa)
        self.click_on_screen(screenshot,(704,330,881,362))

        # DATA INÍCIO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        self.click_on_screen(screenshot, (914,237,1107,276))
        screenshot = self.screenshot('06-telaData.png')
        self.click_on_screen(screenshot, (1107,701,1185,720))
        
        # DATA INÍCIO MARCAÇÃO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        self.click_on_screen(screenshot, (1130,235,1323,274))
        screenshot = self.screenshot('06-telaData.png')
        self.click_on_screen(screenshot, (1107,701,1185,720))
        
        # VINCULA DEPARTAMENTO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        pesquisa = hoje.strftime('%d/%m/%Y')
        self.click_on_screen(screenshot, (698,355,1103,385))
        screenshot = self.screenshot('09-selecionaDepartamento.png')
        self.preenche_cadastro(screenshot,(704,400,887,434),pesquisa)
        self.click_on_screen(screenshot,(712,448,895,482))
        
        # VINCULA CARGO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        pesquisa = hoje.strftime('%d/%m/%Y')
        self.click_on_screen(screenshot, (1120,353,1528,392))
        screenshot = self.screenshot('10-selecionaCargo.png')
        self.preenche_cadastro(screenshot,(1136,400,1524,431),pesquisa)
        self.click_on_screen(screenshot,(1135,449,1280,480))
        
        # FINALIZA O REGISTRO
        screenshot = self.screenshot('07-telaFuncionario2.png')
        self.click_on_screen(screenshot, (1291,640,1538,678))

        # FINALIZA O CADASTRO
        screenshot = self.screenshot('11-finalizaFuncionario.png')
        self.click_on_screen(screenshot, (1292,835,1531,873))
        time.sleep(20)
        
        # VOLTA PARA TELA INICIAL
        self.click_on_screen(screenshot, (47,213,263,253))

if __name__ == "__main__":
    cadastro = CadastroFuncionario()
    cadastro.run()