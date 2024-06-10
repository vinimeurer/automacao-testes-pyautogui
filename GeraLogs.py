import time
import pyautogui
import pyperclip
import os

class GeraLogs: 
    def capturar_output():

        # atalho abrir console do navegador (Chrome)
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(1)
        pyautogui.hotkey('win','up')
        time.sleep(1)
        pyautogui.click(810,115)
        time.sleep(2)

        # Seleciona todo o texto
        pyautogui.hotkey('ctrl', 'a')

        # Copia o texto
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        # Obtém o texto copiado 
        console_output = pyperclip.paste()

        return console_output

    def salvar_arquivo(text, filename):
        logs_folder = "logs"
        if not os.path.exists(logs_folder):
            os.makedirs(logs_folder)
        file_path = os.path.join(logs_folder, filename)
        with open(file_path, 'w') as file:
            file.write(text)

    def limpar_e_fechar():
        pyautogui.hotkey('win','down')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('alt', 'f4')
        
    def abrir_e_fechar():
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('alt', 'f4') 