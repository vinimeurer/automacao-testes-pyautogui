import pyautogui
import time
import datetime
import cv2
from GeraDocs import GeraDocs

class CadastroEmpresa:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroEmpresa\\'

    def screenshot(self, nome):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + nome)
        return screenshot

    def click_on_screen(self, screenshot, area, cor_esperada, tolerancia=95):
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

    def preenche_cadastro(self, screenshot, area, texto):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        pyautogui.write(texto)

    def run(self):
        time.sleep(5)
        
        # VARIÁVEIS FIXAS
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
                while not self.click_on_screen(screenshot, (20,421,301,463),cor_branca):
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # BOTÃO CADASTRO EMPRESA
                screenshot = self.screenshot('02-cadastroEmpresa.png')
                while not self.click_on_screen(screenshot, (55,472,146,499),cor_branca):
                    screenshot = self.screenshot('02-cadastroEmpresa.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # INCLUIR NOVO CADASTRO
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1839,118,1876,148),cor_azul):
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20
                
                # PREENCHE CADASTRO
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

                # FINALIZA
                self.click_on_screen(screenshot, (1653,869,1893,899), cor_azul)
                
                time.sleep(5)
                
                # VOLTA PARA TELA INICIAL 
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(0.5)
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                break
            except pyautogui.ImageNotFoundException:
                print("Imagem não encontrada, retornando para a tela inicial...")
                self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                time.sleep(1)
            
if __name__ == "__main__":
    cadastro = CadastroEmpresa()
    cadastro.run()
