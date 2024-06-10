import pyautogui
import time
import datetime
import cv2

class CadastroHorario:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroHorario\\'
        self.contador_erros = 0  # Inicializa o contador de erros

    def screenshot(self, nome):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + nome)
        return screenshot

    def click_on_screen(self, screenshot, area, cor_esperada, tolerancia=100):
        parte_recortada = screenshot.crop(area)
        parte_recortada.save(self.caminhoScreenshot + 'temp.png')  # Salva a parte recortada temporariamente
        imagem = cv2.imread(self.caminhoScreenshot + 'temp.png')

        # Calcula a média das cores em toda a região recortada
        media_cor = imagem.mean(axis=0).mean(axis=0)

        # Verifica se a média da cor está dentro da tolerância especificada
        if all(abs(media_cor - cor_esperada) < tolerancia):
            campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
            pyautogui.click(campo_x, campo_y)
            time.sleep(1)
            return True
        else:
            self.contador_erros += 1  # Incrementa o contador de erros
            print("Botão não encontrado")
            time.sleep(1)
            return False
        
    def move_cursor(self, screenshot, area):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.moveTo(campo_x, campo_y)  

    def preenche_cadastro(self, screenshot, area, texto):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        pyautogui.write(texto)

    def run(self):
        time.sleep(5)
        # VARIAVEIS
        hoje = datetime.date.today()
        cor_branca = (254,254,254)
        cor_azul = (41,86,128)
        cor_cinza = (235,237,238)

        while True:
            # Reinicia o contador de erros a cada iteração
            self.contador_erros = 0
            
            try:

                # TELA INICIAL
                screenshot = self.screenshot('01-telaInicial.png')
                while not self.click_on_screen(screenshot, (20,421,301,463), cor_branca):
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # BOTÃO CADASTRO HORÁRIO
                screenshot = self.screenshot('02-cadastroHorario.png')
                while not self.click_on_screen(screenshot, (57,512,118,529), cor_branca):
                    screenshot = self.screenshot('02-cadastroHorario.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # INCLUIR NOVO CADASTRO
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1839,118,1876,148),cor_azul):
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # INFORMAÇÕES GERAIS
                screenshot = self.screenshot('04-cargaHoraria.png')
                while not self.click_on_screen(screenshot, (362,262,591,288), cor_azul):
                    screenshot = self.screenshot('04-cargaHoraria.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                descricao = 'Horario ' + hoje.strftime('%d/%m/%Y')
                self.preenche_cadastro(screenshot, (330,200,720,230), descricao)

                # TIPO DA CARGA
                screenshot = self.screenshot('04-cargaHoraria.png')
                while not self.click_on_screen(screenshot,(332,334,726,368), cor_cinza):
                    screenshot = self.screenshot('04-cargaHoraria.png')

                screenshot = self.screenshot('05-tipoCarga.png')
                while not self.click_on_screen(screenshot,(339,436,400,457), cor_branca):
                    screenshot = self.screenshot('05-tipoCarga.png')

                screenshot = self.screenshot('04-cargaHoraria.png') 
                while not self.click_on_screen(screenshot,(1654,388,1895,424), cor_azul): 
                    screenshot = self.screenshot('04-cargaHoraria.png')

                # PERÍODO
                screenshot = self.screenshot('06-periodo.png')
                while not self.click_on_screen(screenshot,(681,260,910,286), cor_azul):
                    screenshot = self.screenshot('06-periodo.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                dias_horarios_coordenadas = {
                    'segunda': [((880, 435, 940, 460), (970, 435, 1040, 460))],
                    'terca': [((880, 555, 940, 600), (970, 555, 1040, 600))],
                    'quarta': [((880, 615, 940, 670), (970, 615, 1040, 670))],
                    'quinta': [((880, 675, 940, 740), (970, 675, 1040, 740))],
                    'sexta': [((880, 735, 940, 810), (970, 735, 1040, 810))]
                }

                for dia, horarios in dias_horarios_coordenadas.items():
                    for entrada, saida in horarios:
                        self.preenche_cadastro(screenshot, entrada, '13:00')
                        self.preenche_cadastro(screenshot, saida, '18:00')

                screenshot = self.screenshot('06-periodo.png')
                while not self.click_on_screen(screenshot,(1665,904,1909,935), cor_azul):
                    screenshot = self.screenshot('06-periodo.png')        

                # POLITICAS
                screenshot = self.screenshot('07-politicas.png')
                while not self.click_on_screen(screenshot, (1005,261,1234,287), cor_azul):
                    screenshot = self.screenshot('07-politicas.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                self.click_on_screen(screenshot,(325,417,572,448), cor_azul)
                
                time.sleep(1)

                self.preenche_cadastro(screenshot,(650,530,1100,570),'Geral')
                screenshot = self.screenshot('07-politicas.png')
                self.click_on_screen(screenshot,(1662,911,1911,941), cor_azul)

                # PERCENTUAL EXTRA
                screenshot = self.screenshot('08-percentualExtra.png')
                while not self.click_on_screen (screenshot,(1320,260,1550,280), cor_azul):
                    screenshot = self.screenshot('08-percentualExtra.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                self.move_cursor(screenshot,(1660,650,1890,670))
                pyautogui.click()

                # VÍNCULO FUNCIONÁRIO
                screenshot = self.screenshot('09-vinculoFuncionario.png')
                while not self.click_on_screen(screenshot,(1650,261,1872,287), cor_azul):
                    screenshot = self.screenshot('09-vinculoFuncionario.png')
                    if self.contador_erros > 20:
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                time.sleep(1)

                #FINALIZA O CADASTRO
                screenshot = self.screenshot('09-vinculoFuncionario.png')
                while not self.click_on_screen(screenshot,(1654,795,1900,832), cor_azul):
                    screenshot = self.screenshot('09-vinculoFuncionario.png')

                time.sleep(5)

                # VOLTA PARA TELA INICIAL 
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(0.5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)

                break  # Sai do loop principal após uma execução bem-sucedida
            
            except pyautogui.ImageNotFoundException:
                print("Imagem não encontrada, retornando para a tela inicial...")
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(1)

if __name__ == "__main__":
    cadastro = CadastroHorario()
    cadastro.run()
