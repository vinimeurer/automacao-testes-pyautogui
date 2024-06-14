import pyautogui
import time
import datetime
import cv2
from GeraDocs import GeraDocs
from GeraDocs import geradorDePisPasep

class CadastroFuncionario:
    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroFuncionario\\'
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
        print('\nCADASTRO DE FUNCIONÁRIO')
        time.sleep(5)
        tempos_tela = {}
        limite_erros = 20
        
######### VARIÁVEIS FIXAS
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
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    continue
                
                
                tempo_tela_inicial = round(time.time() - tempo_inicial, 1)

################# BOTÃO CADASTRO EMPRESA
                tempo_inicial = time.time()
                screenshot = self.screenshot('02-cadastroFuncionario.png')
                while not self.click_on_screen(screenshot, (58,544,143,563), cor_branca):
                    screenshot = self.screenshot('02-cadastroFuncionario.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    continue
                
                tela1_tela2 = round(time.time() - tempo_inicial, 1)

################# INCLUIR NOVO CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('03-novoCadastro.png')
                while not self.click_on_screen(screenshot, (1880,110,1910,150), cor_azul):
                    screenshot = self.screenshot('03-novoCadastro.png')
                    if self.contador_erros > limite_erros:
                        self.click_on_screen(screenshot, (55,199,270,268), cor_branca)
                        break

                if self.contador_erros > limite_erros:
                    continue
                
                tela2_tela3 = round(time.time() - tempo_inicial, 1)

################# PREENCHE CADASTRO
                tempo_inicial = time.time()
                screenshot = self.screenshot('04-telaFuncionario1.png')
                while not self.click_on_screen( screenshot, (369,182,527,214), cor_azul):
                    screenshot = self.screenshot('04-telaFuncionario1.png')

                # NOME
                screenshot = self.screenshot('04-telaFuncionario1.png')
                nome = 'Teste ' + hoje.strftime('%d/%m/%Y')
                self.preenche_cadastro(screenshot, (874,270,1296,345), nome)
                
                # NUMERO CPF
                screenshot = self.screenshot('04-telaFuncionario1.png')
                cpf = GeraDocs.generate_cpf()
                self.preenche_cadastro(screenshot, (1300,280,1500,320), cpf)
                
                # NUMERO PIS
                screenshot = self.screenshot('04-telaFuncionario1.png')
                pis = geradorDePisPasep(False)
                self.preenche_cadastro(screenshot, (1084,345,1303,414), pis)
                
                # VINCULA EMPRESA
                pesquisa = hoje.strftime('%d/%m/%Y')
                
                screenshot = self.screenshot('04-telaFuncionario1.png')
                while not self.click_on_screen(screenshot, (700,528,1108,563), cor_cinza):
                    screenshot = self.screenshot('04-telaFuncionario1.png')
                    
                time.sleep(1)
                
                screenshot = self.screenshot('05-selecionaEmpresa.png')
                self.preenche_cadastro(screenshot,(708,576,1099,610),pesquisa)
                time.sleep(1)
                
                screenshot = self.screenshot('05-selecionaEmpresa.png')
                while not self.click_on_screen(screenshot,(712,624,1103,658), cor_branca):
                    screenshot = self.screenshot('05-selecionaEmpresa.png')

                # DATA ADMISSÂO
                screenshot = self.screenshot('04-telaFuncionario1.png')
                while not self.click_on_screen(screenshot, (698,611,891,638), cor_cinza):
                    screenshot = self.screenshot('04-telaFuncionario1.png')
                
                screenshot = self.screenshot('06-telaData.png')
                while not self.click_on_screen(screenshot, (1107,701,1185,720), cor_branca):
                    screenshot = self.screenshot('06-telaData.png')
                    
                # MATRICULA
                screenshot = self.screenshot('04-telaFuncionario1.png')
                matricula = hoje.strftime('%d%m%Y')
                self.preenche_cadastro(screenshot, (1128,606,1323,644), matricula)
                time.sleep(1)
                
                tela3_tela4 = round(time.time() - tempo_inicial, 1)
                
################# SCROLL PARA O FINAL DA TELA
                pyautogui.scroll(-5000)
                tempo_inicial = time.time()     
                       
                # VINCULA HORARIO
                pesquisa = hoje.strftime('%d/%m/%Y')
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (700,240,894,272), cor_cinza):
                    screenshot = self.screenshot('07-telaFuncionario2.png')
                    
                time.sleep(1)
                
                screenshot = self.screenshot('08-selecionaHorario.png')
                self.preenche_cadastro(screenshot,(706,286,883,318),pesquisa)
                time.sleep(1)
                
                screenshot = self.screenshot('08-selecionaHorario.png')
                while not self.click_on_screen(screenshot,(704,330,881,362), cor_branca):
                    screenshot = self.screenshot('08-selecionaHorario.png')

                # DATA INÍCIO
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (914,237,1107,276), cor_cinza):
                    screenshot = self.screenshot('07-telaFuncionario2.png')
                
                screenshot = self.screenshot('06-telaData.png')
                while not self.click_on_screen(screenshot, (1107,701,1185,720), cor_branca):
                    screenshot = self.screenshot('06-telaData.png')
                
                # DATA INÍCIO MARCAÇÃO
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (1130,235,1323,274), cor_cinza):
                    screenshot = self.screenshot('07-telaFuncionario2.png')
                
                screenshot = self.screenshot('06-telaData.png')
                while not self.click_on_screen(screenshot, (1107,701,1185,720), cor_branca):
                    screenshot = self.screenshot('06-telaData.png')
                
                # VINCULA DEPARTAMENTO
                pesquisa = hoje.strftime('%d/%m/%Y')
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (698,355,1103,385), cor_cinza):
                    screenshot = self.screenshot('07-telaFuncionario2.png')
                    
                time.sleep(1)
                
                screenshot = self.screenshot('09-selecionaDepartamento.png')
                self.preenche_cadastro(screenshot,(704,400,887,434),pesquisa)
                time.sleep(1)
                
                screenshot = self.screenshot('09-selecionaDepartamento.png')
                while not self.click_on_screen(screenshot,(712,448,895,482), cor_branca):
                    screenshot = self.screenshot('09-selecionaDepartamento.png')
                
                # VINCULA CARGO
                pesquisa = hoje.strftime('%d/%m/%Y')
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (1120,353,1528,392), cor_cinza):
                    screenshot = self.screenshot('07-telaFuncionario2.png')
                    
                time.sleep(1)
                    
                screenshot = self.screenshot('10-selecionaCargo.png')
                self.preenche_cadastro(screenshot,(1136,400,1524,431),pesquisa)
                time.sleep(1)
                
                screenshot = self.screenshot('10-selecionaCargo.png')
                while not self.click_on_screen(screenshot,(1135,449,1280,480),cor_branca):
                    screenshot = self.screenshot('10-selecionaCargo.png')
                
                # FINALIZA O REGISTRO
                screenshot = self.screenshot('07-telaFuncionario2.png')
                while not self.click_on_screen(screenshot, (1291,640,1538,678), cor_azul):
                    screenshot = self.screenshot('07-telaFuncionario2.png')

################# FINALIZA O CADASTRO
                screenshot = self.screenshot('11-finalizaFuncionario.png')
                while not self.click_on_screen(screenshot, (1302,843,1522,870), cor_azul):
                    screenshot = self.screenshot('11-finalizaFuncionario.png')
                
                tela4_finalizar = round(time.time() - tempo_inicial, 1)
                
################# VOLTA PARA TELA INICIAL 
                time.sleep(10)
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
    cadastro = CadastroFuncionario()
    cadastro.run()