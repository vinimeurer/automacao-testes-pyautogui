
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


## Licença

Este projeto é distribuído sob a licença [MIT](https://opensource.org/licenses/MIT).