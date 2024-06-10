# Notas de Versão - Automatização de Cadastro de Cargos

## [Versão 1.0.0] - 2024-06-10

**Adicionado**
- Implementação de validação de cor para garantir a precisão do clique em botões.
- Remoção de pausas com `time.sleep` após os cliques em botões.
- Incremento do contador de erros para monitorar tentativas de clique mal sucedidas.
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