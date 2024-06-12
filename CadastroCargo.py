import pyautogui
import time
import datetime
import cv2

class CadastroCargo:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroCargo\\'
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
        print('\nCADASTRO DE CARGO')
        tempos_tela = {}
        time.sleep(5)
        limite_erros = 20

######### VARIÁVEIS
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
                while not self.click_on_screen(screenshot, (20, 421, 301, 463), cor_branca):  
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    return

                tempo_tela_inicial = round(time.time() - tempo_inicial, 1)

################# BOTÃO CADASTRO CARGO
                tempo_inicial = time.time()
                screenshot = self.screenshot('02-cadastroCargo.png')
                while not self.click_on_screen(screenshot, (63, 579, 107, 597), cor_branca): 
                    screenshot = self.screenshot('02-cadastroCargo.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    return

                tela1_tela2 = round(time.time() - tempo_inicial, 1)

################# INCLUIR NOVO CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1831,114,1885,154), cor_azul): 
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    return

                tela2_tela3 = round(time.time() - tempo_inicial, 1)

                # PREENCHE CADASTRO
                screenshot = self.screenshot('04-telaCargo1.png')

                # NOME
                nome = 'Cargo ' + hoje.strftime('%d/%m/%Y')
                self.preenche_cadastro(screenshot, (706,255,1107,292), nome)

                # BOTÃO CONTINUAR
                tempo_inicial = time.time()
                screenshot = self.screenshot('04-telaCargo1.png')
                while not self.click_on_screen(screenshot, (1654, 337, 1901, 364), cor_azul): 
                    screenshot = self.screenshot('04-telaCargo1.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    return

                tela3_tela4 = round(time.time() - tempo_inicial, 1)

################# FINALIZA O CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('05-telaCargo2.png')
                while not self.click_on_screen(screenshot, (1644, 549, 1888, 580), cor_azul):
                    screenshot = self.screenshot('05-telaCargo2.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)

                if self.contador_erros > limite_erros:
                    return

                tela4_finalizar = round(time.time() - tempo_inicial, 1)

################# VOLTA PARA TELA INICIAL 
                time.sleep(5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(0.5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)

################# EXIBE OS TEMPOS
                tempos_tela['tempo entre tela 1 e tela 2'] = tela1_tela2
                tempos_tela['tempo entre tela 2 e tela 3'] = tela2_tela3
                tempos_tela['tempo entre tela 3 e tela 4'] = tela3_tela4
                tempos_tela['tempo entre tela 4 e finalizar'] = tela4_finalizar

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
    cadastro = CadastroCargo()
    cadastro.run()
