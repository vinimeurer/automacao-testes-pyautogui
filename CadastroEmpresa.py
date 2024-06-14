import pyautogui
import time
import datetime
import cv2
from GeraDocs import GeraDocs

class CadastroEmpresa:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroEmpresa\\'
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
        print('\nCADASTRO DE EMPRESA')
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
                while not self.click_on_screen(screenshot, (20,421,301,463),cor_branca):
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca) 
                        break

                if self.contador_erros > limite_erros:
                    continue
                
                tempo_tela_inicial = round(time.time() - tempo_inicial, 1)

################# BOTÃO CADASTRO EMPRESA
                tempo_inicial = time.time()
                screenshot = self.screenshot('02-cadastroEmpresa.png')
                while not self.click_on_screen(screenshot, (55,472,146,499),cor_branca):
                    screenshot = self.screenshot('02-cadastroEmpresa.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
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
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    continue
                
                tela2_tela3 = round(time.time() - tempo_inicial, 1)
                
################# PREENCHE CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('04-telaEmpresa.png')

                # PREENCHE NOME       
                nome = 'Empresa ' + hoje.strftime('%d/%m/%Y')
                self.preenche_cadastro(screenshot, (500,490,890,510), nome)
                
                # PREENCHE TIPO DOCUMENTO
                screenshot = self.screenshot('05-tipoDocumento.png')
                while not self.click_on_screen(screenshot, (915,487,1311,514), cor_cinza):
                    screenshot = self.screenshot('05-tipoDocumento.png')
                    
                screenshot = self.screenshot('05-tipoDocumento.png')
                while not self.click_on_screen(screenshot, (925,581,972,603), cor_branca):
                    screenshot = self.screenshot('05-tipoDocumento.png')
            
                # PREENCHE NUMERO DOCUMENTO
                screenshot = self.screenshot('04-telaEmpresa.png')
                cnpj = GeraDocs.generate_cnpj()
                self.preenche_cadastro(screenshot, (1330,480,1720,520), cnpj)

                # PREENCHE CODIGO INTERNO
                cod_interno = hoje.strftime('%d%m%Y')
                self.preenche_cadastro(screenshot, (500,560,890,590), cod_interno)
                time.sleep(2)
                
                # PREENCHE SIGLA
                screenshot = self.screenshot('04-telaEmpresa.png')
                self.preenche_cadastro(screenshot, (914,538,1320,616), 'E')
                
                # PREENCHE ENDEREÇO
                self.preenche_cadastro(screenshot, (920,700,1310,740), 'Endereco')
                
                # PREENCHE CIDADE
                self.preenche_cadastro(screenshot, (1330,710,1730,740), 'Cidade')
                
                # PREENCHE BAIRRO
                self.preenche_cadastro(screenshot, (500,800,890,840), 'Bairro')
                
                # PREENCHE ESTADO
                screenshot = self.screenshot('04-telaEmpresa.png')
                self.preenche_cadastro(screenshot, (910,810,1300,840), 'Estado')
                
                # PREENCHE PAÍS
                self.preenche_cadastro(screenshot, (1330,800,1720,840), 'Pais')
                
################# FINALIZA
                self.click_on_screen(screenshot, (1653,869,1893,899), cor_azul)
                
                tela3_finalizar = round(time.time() - tempo_inicial, 1)
                
################# VOLTA PARA TELA INICIAL 
                time.sleep(5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(0.5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)

                tempos_tela['tempo entre tela 1 e tela 2'] = tela1_tela2
                tempos_tela['tempo entre tela 2 e tela 3'] = tela2_tela3
                tempos_tela['tempo entre tela 3 e finalizar'] = tela3_finalizar

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
    cadastro = CadastroEmpresa()
    cadastro.run()
