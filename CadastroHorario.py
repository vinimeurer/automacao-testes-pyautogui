import pyautogui
import time
import datetime

class CadastroHorario:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroHorario\\'

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

        # BOTÃO CADASTRO HORÁRIO
        screenshot = self.screenshot('02-cadastroHorario.png')
        self.click_on_screen(screenshot, (57,512,118,529))

        # INCLUIR NOVO CADASTRO
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (1851,121,1868,148))
        time.sleep(5)

        # PREENCHE CADASTRO
        screenshot = self.screenshot('04-cargaHoraria.png')

        # DESCRIÇÃO
        descricao = 'Horario ' + hoje.strftime('%d/%m/%Y')
        self.preenche_cadastro(screenshot, (332,202,726,236), descricao)
        time.sleep(2)
        
        # TIPO DA CARGA
        self.click_on_screen(screenshot,(332,334,726,368))
        screenshot = self.screenshot('05-tipoCarga.png')
        self.click_on_screen(screenshot,(339,436,400,457))
        self.click_on_screen (screenshot,(1654,388,1895,424))
        time.sleep(5)
        screenshot = self.screenshot('06-periodo.png')
        
        #PERÍODO
        self.click_on_screen(screenshot,(1030,314,1172,351))
        screenshot = self.screenshot('07-replicaPeriodo.png')
        time.sleep(1)
        
        horarios_coordenadas = {
            '0800': (766, 438, 847, 468),
            '1200': (871, 437, 943, 467),
            '1300': (975, 438, 1047, 468),
            '1700': (1064, 438, 1136, 468)
        }
        dias_coordenadas = [
            (769, 707, 809, 737),
            (826, 707, 866, 737),
            (885, 707, 925, 737),
            (941, 707, 981, 737),
            (1000, 707, 1040, 737)
        ]

        # PREENCHE HORÁRIOS
        for horario, coordenadas in horarios_coordenadas.items():
            self.preenche_cadastro(screenshot, coordenadas, horario)

        # SELECIONA OS DIAS
        for coordenadas in dias_coordenadas:
            self.click_on_screen(screenshot, coordenadas)

        # APLICA
        self.click_on_screen(screenshot, (1018, 791, 1167, 829))
        screenshot = self.screenshot('06-periodo.png')
        self.click_on_screen(screenshot,(1665,904,1909,935))
        time.sleep(5)
        
        # POLITICAS
        screenshot = self.screenshot('08-politicas.png')
        self.click_on_screen(screenshot,(325,417,572,448))
        self.preenche_cadastro(screenshot,(657,534,1105,570),'Geral')
        screenshot = self.screenshot('08-politicas.png')
        self.click_on_screen(screenshot,(1662,911,1911,941))
        time.sleep(3)
        
        # PERCENTUAL EXTRA
        screenshot = self.screenshot('09-percentualExtra.png')
        self.click_on_screen (screenshot,(1653,646,1898,676))
        time.sleep(3)
        
        # FINALIZA O CADASTRO
        screenshot = self.screenshot('10-vinculoFuncionario.png')
        self.click_on_screen(screenshot,(1654,795,1900,832))
        time.sleep(10)
        
        # VOLTA PARA TELA INICIAL
        screenshot = self.screenshot('03-novoCadastro.png')
        self.click_on_screen(screenshot, (40,215,286,252))
        time.sleep(1)
        self.click_on_screen(screenshot, (40,215,286,252))

if __name__ == "__main__":
    cadastro = CadastroHorario()
    cadastro.run()
