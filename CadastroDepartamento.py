import pyautogui
import time
import datetime
import cv2

class CadastroDepartamento:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroDepartamento\\'
        self.contador_erros = 0  # Inicializa o contador de erros

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
                while not self.click_on_screen(screenshot, (20,421,301,463), cor_branca):
                    screenshot = self.screenshot('01-telaInicial.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # BOTÃO CADASTRO CARGO
                screenshot = self.screenshot('02-cadastroDepartamento.png')
                while not self.click_on_screen(screenshot, (64,616,154,633), cor_branca):
                    screenshot = self.screenshot('02-cadastroDepartamento.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # INCLUIR NOVO CADASTRO
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1839,118,1876,148), cor_azul):
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue  # Reinicia o processo se o contador de erros exceder 20

                # PREENCHE CADASTRO
                screenshot = self.screenshot('04-telaDepartamento1.png')

                # NOME
                nome = 'Departamento ' + hoje.strftime('%d/%m/%Y')
                self.preenche_cadastro(screenshot, (500,250,900,280), nome)
                
                # SIGLA
                self.preenche_cadastro(screenshot, (920,250,1320,280), 'D')
                
                # BOTÃO CONTINUAR
                screenshot = self.screenshot('04-telaDepartamento1.png')
                while not self.click_on_screen(screenshot, (1660,328,1901,364), cor_azul):
                    screenshot = self.screenshot('04-telaDepartamento1.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)  # Clica na tela inicial
                        break

                if self.contador_erros > 20:
                    continue

                # FINALIZA O CADASTRO
                screenshot = self.screenshot('05-telaDepartamento2.png')
                while not self.click_on_screen(screenshot, (1644,549,1888,580),cor_azul):
                    screenshot = self.screenshot('05-telaDepartamento2.png')
                    if self.contador_erros > 20:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca) 
                        break

                if self.contador_erros > 20:
                    continue 
                
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
    cadastro = CadastroDepartamento()
    cadastro.run()
