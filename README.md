Gerenciador de Tarefas em Python
Este é um aplicativo simples de gerenciamento de tarefas em Python com uma interface gráfica usando Tkinter. Ele permite adicionar, listar, marcar como concluídas, editar e remover tarefas, além de armazená-las em um arquivo JSON para persistência de dados.

Funcionalidades
Adicionar Tarefa: Adicione uma nova tarefa com descrição, prazo, prioridade e categoria.
Listar Tarefas: Exibe todas as tarefas em uma lista, organizadas por prioridade.
Marcar Tarefa como Concluída: Selecione uma tarefa e marque-a como concluída.
Remover Tarefa: Remova uma tarefa selecionada.
Editar Tarefa: Edite a descrição, prazo, prioridade e categoria de uma tarefa existente.
Como Usar
Instalação: Certifique-se de que o Python 3 está instalado em seu sistema.
Dependências: Nenhuma dependência externa é necessária além do Python 3.
Executar o Aplicativo: Execute o script no terminal usando o comando:
bash
Copiar código
python gerenciador_de_tarefas.py
Interface Gráfica:
Ao iniciar, a janela principal mostrará a lista de tarefas.
Use os botões disponíveis para adicionar, editar, remover ou marcar uma tarefa como concluída.
Estrutura de Dados
As tarefas são armazenadas em um arquivo tarefas.json no formato JSON.
Cada tarefa possui:
descricao: descrição da tarefa.
prazo: prazo de conclusão no formato DD/MM/AAAA.
prioridade: nível de prioridade (alta, média ou baixa).
categoria: categoria da tarefa (ex.: Trabalho, Pessoal).
concluida: status da tarefa (concluída ou pendente).
Exemplo de Uso
Adicionar uma tarefa:
Clique no botão "Adicionar Tarefa" e preencha os detalhes.
Listar tarefas:
Todas as tarefas são exibidas automaticamente e atualizadas em tempo real.
Marcar como concluída:
Selecione uma tarefa na lista e clique em "Marcar Como Concluída".
Editar uma tarefa:
Selecione uma tarefa na lista e clique em "Editar Tarefa" para modificar os detalhes.
Erros Comuns
Data inválida: Certifique-se de digitar a data no formato DD/MM/AAAA.
Prioridade inválida: Escolha entre "alta", "média" ou "baixa".
