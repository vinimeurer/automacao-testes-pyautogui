
# Documentação do Projeto de Automação

  

Este projeto de automação foi desenvolvido utilizando a biblioteca PyAutoGUI para automatizar tarefas relacionadas ao cadastro de empresas, departamentos, cargos, horários e funcionários.

  

## Estrutura de Diretórios

  
  

    - logs/
	  
    - screenshots/
	    - CadastroCargo/
	    - CadastroDepartamento/
	    - CadastroEmpresa/
	    - CadastroFuncionaio/
	    - CadastroHorario/
	   
    - CadastroCargo.py
    - CadastroDepartamento.py
    - CadastroEmpresa.py
    - CadastroFuncionaio.py
    - CadastroHorario.py
    - GeraDocs.py
    - GeraLogs.py
    - main.py

  
  

### Descrição dos Diretórios e Arquivos

  

- **logs/**: Contém arquivos de log para cada tipo de cadastro realizado.

- **screenshots/**: Armazena capturas de tela para referência durante o processo de automação.

- **CadastroCargo/**: Capturas de tela relacionadas ao cadastro de cargos.

- **CadastroDepartamento/**: Capturas de tela relacionadas ao cadastro de departamentos.

- **CadastroEmpresa/**: Capturas de tela relacionadas ao cadastro de empresas.

- **CadastroFuncionaio/**: Capturas de tela relacionadas ao cadastro de funcionários.

- **CadastroHorario/**: Capturas de tela relacionadas ao cadastro de horários.

- **.py files**: Scripts Python para cada funcionalidade específica do cadastro.

- **GeraDocs.py**: Script para gerar documentos relacionados aos cadastros.

- **GeraLogs.py**: Script para gerar arquivos de log durante o processo de automação.

- **main.py**: Arquivo principal que inicia a execução do programa.



## Requisitos

Para a execução adequada deste projeto de automação, é necessário o seguinte ambiente:

- Navegador Google Chrome com zoom ajustado para 80%.
- Monitor ou tela com resolução Full HD (1920x1080).
- Linguagem Python.

Certifique-se de que o navegador Google Chrome esteja configurado com um zoom de 80% para garantir que as capturas de tela e os cliques do mouse sejam precisos durante o processo de automação. Além disso, o projeto foi desenvolvido utilizando a linguagem Python, portanto, é necessário ter um ambiente Python configurado para executar os scripts de automação.




## Dependências

  

Este projeto requer as seguintes dependências, que podem ser instaladas usando o arquivo `requirements.txt`. Certifique-se de instalar estas dependências antes de executar o projeto. Você pode instalá-las usando o seguinte comando:

  

    pip install -r requirements.txt


Isso garantirá que todas as bibliotecas necessárias estejam presentes e no nível correto de versão para o funcionamento adequado do projeto. Tabmém é possível instalar as bibliotecas através do comando :

  

    pip install pyautogui pyperclip opencv-python
  

## Funcionalidades

  

O projeto oferece as seguintes funcionalidades:

  

- Cadastro de empresas.

- Cadastro de departamentos.

- Cadastro de cargos.

- Cadastro de horários.

- Cadastro de funcionários.

  

Cada funcionalidade é implementada em um arquivo Python separado, permitindo modularidade e facilitando a manutenção do código.

  

## Execução

  

Para executar o projeto, basta iniciar o arquivo `main.py`. Certifique-se de ter todas as dependências necessárias instaladas e que os arquivos de captura de tela estejam acessíveis no diretório correto.


## Explicação dos códigos .py (princiáis funções)

### Método init


    def __init__(self):
        self.caminhoScreenshot = '.\\screenshots\\CadastroCargo\\'
        self.contador_erros = 0  # Inicializa o contador de erros


Este método é o construtor da classe. Quando um novo objeto da classe é criado, este método é chamado automaticamente.

**self.caminhoScreenshot:** Este atributo é inicializado com o caminho onde as capturas de tela relacionadas ao cadastro de cargos serão salvas. Isso garante que as capturas de tela sejam organizadas em um diretório específico para essa finalidade.

**self.contador_erros:** Este atributo é inicializado com zero. Ele será usado para contar o número de erros que ocorrem durante o processo de automação.

### Método screenshot

    def screenshot(self, nome):
        screenshot = pyautogui.screenshot()
        screenshot.save(self.caminhoScreenshot + nome)
        return screenshot


Este método captura uma screenshot da tela atual e a salva no diretório especificado pelo atributo ```caminhoScreenshot```. Ele recebe como parâmetro o nome do arquivo a ser salvo. Após salvar a captura de tela, retorna a própria imagem.

### Método click_on_screen

    def click_on_screen(self, screenshot, area, cor_esperada, tolerancia=95):
        parte_recortada = screenshot.crop(area)
        parte_recortada.save(self.caminhoScreenshot + 'temp.png')  # Salva a parte recortada temporariamente
        imagem = cv2.imread(self.caminhoScreenshot + 'temp.png')

        media_cor = imagem.mean(axis=0).mean(axis=0)

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


Este método é responsável por clicar em uma determinada área da tela, verificar se a cor média dessa área corresponde à cor esperada e realizar a ação correspondente.Ele recebe como parâmetros: 
- screenshot (captura da tela inteira) 
- Área da tela onde deve ser clicado (x1,y1,x2,y2) 
- Cor esperada nessa área (padrão RGB)
- Tolerância para a verificação da cor.

O método começa recortando a área especificada da screenshot e a salva temporariamente em um arquivo. Em seguida, utiliza a biblioteca ```opencv-python``` para ler a imagem recortada e calcular a média das cores.

Se a média das cores estiver dentro da tolerância especificada em relação à cor esperada, o método localiza o centro da área na tela e realiza um clique usando ```pyautogui.click```. Caso contrário, incrementa o contador de erros e exibe uma mensagem de erro.



### Método preenche_cadastro

    def preenche_cadastro(self, screenshot, area, texto):
        parte_recortada = screenshot.crop(area)
        campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
        pyautogui.click(campo_x, campo_y)
        pyautogui.write(texto)

Este método é responsável por preencher um campo de cadastro na tela. Ele recebe como parâmetros:
- Screenshot (captura da tela inteira) 
- Área onde está localizado o campo na tela(x1,y1,x2,y2) 
- Texto a ser digitado no campo especificado

O método recorta a parte da ```screenshot``` correspondente à área especificada, localiza o centro dessa área na tela e em seguida escreve o texto fornecido usando ```pyautogui.write```.


### Método move_cursor

    def move_cursor(self, screenshot, area):
            parte_recortada = screenshot.crop(area)
            campo_x, campo_y = pyautogui.locateCenterOnScreen(parte_recortada)
            pyautogui.moveTo(campo_x, campo_y)  

Este método é responsável por mover o mouse até uma parte específica da tela. Ele recebe como parâmetros:
- Screenshot (captura da tela inteira) 
- Área onde está localizado o campo na tela(x1,y1,x2,y2) 

O método recorta a parte da ```screenshot``` correspondente à área especificada, localiza o centro dessa área na tela e em seguida move o mouse até o centro da área utilizando ```pyautogui.moveTo```.


### Método run

    def run(self):
        # Restante do código

Este método é chamado para iniciar o processo de automação. Ele pode conter chamadas para outros métodos que são necessários para executar a automação, como preencher formulários, clicar em botões, etc.

### Execução do programa

    if __name__ == "__main__":
        cadastro = CadastroEmpresa()
        cadastro.run()

Este bloco de código é responsável por verificar se o script está sendo executado diretamente ou importado como um módulo. Se for executado diretamente, ele cria um objeto da classe e chama o método ```run()``` desse objeto para iniciar o processo de automação. Isso permite que o script seja reutilizável como um módulo em outros programas, além de executar o processo de automação quando for executado como um script independente.


## Licença

Este projeto é distribuído sob a licença [MIT](https://opensource.org/licenses/MIT).