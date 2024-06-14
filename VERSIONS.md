# Notas de Versão - Projeto de Automação

## [Versão 1.2.1] - 2024-06-14

**Adicionado**
- Correção de um bug relacinado ao loop em caso de lentidão

**Alterado**
- Foi alterada a lógica de cliques na função `click_on_screen` devido a um erro que estava ocorrendo

**Removido**
- N/A



## [Versão 1.2.0] - 2024-06-12

**Adicionado**
- Adição da variável ```self.mensagem_erro``` que armazena erros de imagem e de botão não encontrado
- Adição da variável ```limite_erros``` que define o limite de segundos para clicar nos botões

**Alterado**
- Foram substituídos os valores fiuxos de limite de tempo pela variável ```limite_erros```

**Removido**
- N/A



## [Versão 1.1.0] - 2024-06-12

**Adicionado**
- Implementação de medição de tempo de execução usando ```time.time()``` para cada etapa do processo de cadastro.
- Armazenamento dos tempos de cada tela no dicionário ```tempos_tela = {}```.
- Impressão dos tempos de execução ao final do processo de cadastro.

**Alterado**
- A lógica de cliques em botões foi ajustada para incluir a medição de tempo entre as telas e a impressão dos tempos de execução.

**Removido**
- N/A



## [Versão 1.0.1] - 2024-06-10

**Adicionado**
- Correção de um bug no direcionamento de imagens 

**Alterado**
- foi alterado o `self.caminhoScreenshot` o método `__init__` devido a um mal direcionamento de capturas de tela

**Removido**
- N/A



## [Versão 1.0.0] - 2024-06-10

**Adicionado**
- Implementação de validação de cor no método `click_on_screen` para garantir a precisão do clique em botões.
- Incremento do contador de erros `self.contador_erros` no método `__init__` para monitorar tentativas de clique mal sucedidas.
- Loop de tentativas de clique em botões até que a cor esperada seja encontrada.
- Adição de variáveis de cores para as cores esperadas dos botões.
- Lógica para retornar à tela inicial em caso de falha na localização dos botões.
- Tratamento de exceção para lidar com imagens não encontradas.

**Alterado**
- A lógica de cliques em botões foi modificada para incluir as funcionalidades extras adequadamente.

**Removido**
- Pausas fixas com `time.sleep` após os cliques em botões.



## [Versão 0.1.0] - 2024-05-30

**Adicionado**
- Implementação inicial do código de automatização de cadastros utilizando PyAutoGUI.

**Alterado**
- N/A

**Removido**
- N/A
