import pyautogui
import time
import datetime
import cv2

class CadastroHorario:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroHorario\\'
        self.contador_erros = 0
        self.mensagem_erro = ""

    def screenshot(self, nome):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + nome)
        return screenshot

    def click_on_screen(self, screenshot, area, cor_esperada, tolerancia=95):
        limite_erros = 20
        parte_recortada = screenshot.crop(area)
        parte_recortada.save(self.caminhoScreenshot + 'temp.png') 
        imagem = cv2.imread(self.caminhoScreenshot + 'temp.png')
        media_cor = imagem.mean(axis=0).mean(axis=0)
        if all(abs(media_cor - cor_esperada) < tolerancia):
            campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
            pyautogui.click(campo_x, campo_y)
            time.sleep(1)
            return True
        else:
            self.contador_erros += 1 
            print("Botão não encontrado")
            if self.contador_erros > limite_erros:
                print("Botão não encontrado devido a lentidão. Voltando para a tela inicial e iniciando o processo novamente")
                self.mensagem_erro = "Botão não encontrado devido a lentidão. Voltando para a tela inicial e iniciando o processo novamente"
                pyautogui.press('esc')
                pyautogui.click(150,230)
                time.sleep(1)
                pyautogui.click(150,230)
                time.sleep(1)
                return False
            time.sleep(1)
            return False
        
    def preenche_cadastro(self, screenshot, area, texto):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        pyautogui.write(texto)
        
    def move_cursor(self, screenshot, area):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.moveTo(campo_x, campo_y)  

    def run(self):
        print('\nCADASTRO DE HORÁRIO')
        tempos_tela = {}
        time.sleep(5)
        limite_erros = 20
        
######### VARIAVEIS
        hoje = datetime.date.today()
        cor_branca = (254,254,254)
        cor_azul = (41,86,128)
        cor_cinza = (235,237,238)

        while True:
            self.contador_erros = 0
            
            try:
                self.mensagem_erro = ""

################# TELA INICIAL
                tempo_inicial = time.time()
                screenshot = self.screenshot('01-telaInicial.png')
                while not self.click_on_screen(screenshot, (20,421,301,463), cor_branca):
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 

                tempo_tela_inicial = round(time.time() - tempo_inicial, 1)
                
################# BOTÃO CADASTRO HORÁRIO
                tempo_inicial = time.time()
                screenshot = self.screenshot('02-cadastroHorario.png')
                while not self.click_on_screen(screenshot, (57,512,118,529), cor_branca):
                    screenshot = self.screenshot('02-cadastroHorario.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 
                
                tela1_tela2 = round(time.time() - tempo_inicial, 1)

################# INCLUIR NOVO CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1839,118,1876,148),cor_azul):
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 
                
                tela2_tela3 = round(time.time() - tempo_inicial, 1)

################# INFORMAÇÕES GERAIS
                tempo_inicial = time.time()
                time.sleep(2)
                screenshot = self.screenshot('04-cargaHoraria.png')
                while not self.click_on_screen(screenshot, (362,262,591,288), cor_azul):
                    screenshot = self.screenshot('04-cargaHoraria.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 

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
                    
                tela3_tela4 = round(time.time() - tempo_inicial, 1)

################# PERÍODO
                tempo_inicial = time.time()
                time.sleep(2)
                screenshot = self.screenshot('06-periodo.png')
                while not self.click_on_screen(screenshot,(681,260,910,286), cor_azul):
                    screenshot = self.screenshot('06-periodo.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 

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
                    
                tela4_tela5 = round(time.time() - tempo_inicial, 1)        

################# POLITICAS
                tempo_inicial = time.time()
                time.sleep(2)
                screenshot = self.screenshot('07-politicas.png')
                while not self.click_on_screen(screenshot, (1005,261,1234,287), cor_azul):
                    screenshot = self.screenshot('07-politicas.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 

                self.click_on_screen(screenshot,(325,417,572,448), cor_azul)
                
                time.sleep(1)

                self.preenche_cadastro(screenshot,(650,530,1100,570),'Geral')
                screenshot = self.screenshot('07-politicas.png')
                self.click_on_screen(screenshot,(1662,911,1911,941), cor_azul)
                
                tela5_tela6 = round(time.time() - tempo_inicial, 1)

################# PERCENTUAL EXTRA
                tempo_inicial = time.time()
                time.sleep(2)
                screenshot = self.screenshot('08-percentualExtra.png')
                while not self.click_on_screen (screenshot,(1320,260,1550,280), cor_azul):
                    screenshot = self.screenshot('08-percentualExtra.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue

                self.move_cursor(screenshot,(1660,650,1890,670))
                pyautogui.click()
                
                tela6_tela7 = round(time.time() - tempo_inicial, 1)

################# VÍNCULO FUNCIONÁRIO
                tempo_inicial = time.time()
                time.sleep(2)
                screenshot = self.screenshot('09-vinculoFuncionario.png')
                while not self.click_on_screen(screenshot,(1650,261,1872,287), cor_azul):
                    screenshot = self.screenshot('09-vinculoFuncionario.png')
                    if self.contador_erros > limite_erros:
                        break

                if self.contador_erros > limite_erros:
                    continue 

                time.sleep(1)
                
                #FINALIZA O CADASTRO
                screenshot = self.screenshot('09-vinculoFuncionario.png')
                while not self.click_on_screen(screenshot,(1654,795,1900,832), cor_azul):
                    screenshot = self.screenshot('09-vinculoFuncionario.png')
                    
                tela7_finalizar = round(time.time() - tempo_inicial, 1)

################# VOLTA PARA TELA INICIAL 
                time.sleep(5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(0.5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)

################# EXIBE OS TEMPOS
                tempos_tela['tempo entre tela 1 e tela 2'] = tela1_tela2
                tempos_tela['tempo entre tela 2 e tela 3'] = tela2_tela3
                tempos_tela['tempo entre tela 3 e tela 4'] = tela3_tela4
                tempos_tela['tempo entre tela 4 e tela 5'] = tela4_tela5
                tempos_tela['tempo entre tela 5 e tela 6'] = tela5_tela6
                tempos_tela['tempo entre tela 6 e tela 7'] = tela6_tela7
                tempos_tela['tempo entre tela 7 e finalizar'] = tela7_finalizar

                for chave, valor in tempos_tela.items():
                    print(f"{chave}: {valor} segundos")
                
                break 

############# TRATA O ERRO DE IMAGEM
            except pyautogui.ImageNotFoundException:
                print("Imagem não encontrada, retornando para a tela inicial e iniciando o processo novamente")
                self.mensagem_erro = "Imagem não encontrada, retornando para a tela inicial e iniciando o processo novamente"
                pyautogui.press('esc')
                pyautogui.click(150,230)
                time.sleep(1)
                pyautogui.click(150,230)
                time.sleep(1)

if __name__ == "__main__":
    cadastro = CadastroHorario()
    cadastro.run()
