import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

#Arquivo onde as tarefas serão guardadas
ARQUIVO_TAREFAS = 'tarefas.json'

#Função que carrega as tarefas do arquivo JSON
def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#Função para salvar tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as file:
        json.dump(tarefas, file, indent=4)

#Função para adicionar uma nova tarefa
def adicionar_tarefa():
    descricao = simpledialog.askstring("Descrição", "Digite a descrição da tarefa:")
    if not descricao:
        return

    prazo = simpledialog.askstring("Prazo", "Digite o prazo (DD/MM/AAAA):")
    try:
        prazo_data = datetime.strptime(prazo, "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Use o formato DD/MM/AAAA.")
        return

    prioridade = simpledialog.askstring("Prioridade", "Digite a prioridade (alta, média, baixa):")
    if prioridade not in ["alta", "média", "baixa"]:
        messagebox.showerror("Erro", "Prioridade inválida. Escolha entre alta, média ou baixa.")
        return

    categoria = simpledialog.askstring("Categoria", "Digite a categoria (ex: Trabalho, Pessoal):")

    nova_tarefa = {
        'descricao': descricao,
        'prazo': str(prazo_data),
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }

    tarefas = carregar_tarefas()
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
    listar_tarefas()

#Função para listar todas as tarefas
def listar_tarefas():
    tarefas = carregar_tarefas()
    lista_tarefas.delete(0, tk.END) 
    
    if not tarefas:
        lista_tarefas.insert(tk.END, "Nenhuma tarefa pendente.")
        return

    # Organizar por prioridade
    tarefas.sort(key=lambda t: {"alta": 1, "média": 2, "baixa": 3}[t['prioridade']])
    
    for i, tarefa in enumerate(tarefas, start=1):
        status = 'Concluída' if tarefa['concluida'] else 'Pendente'
        lista_tarefas.insert(tk.END, f"{i}. {tarefa['descricao']} (Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}) - {status}")

#Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida():
    indice = lista_tarefas.curselection()
    if not indice:
        messagebox.showerror("Erro", "Selecione uma tarefa para marcar como concluída.")
        return

    tarefas = carregar_tarefas()
    indice = indice[0]

    if tarefas[indice]['concluida']:
        messagebox.showinfo("Info", "Tarefa já foi concluída.")
    else:
        tarefas[indice]['concluida'] = True
        salvar_tarefas(tarefas)
        messagebox.showinfo("Sucesso", "Tarefa marcada como concluída!")
        listar_tarefas()

#Função para remover uma tarefa
def remover_tarefa():
    indice = lista_tarefas.curselection()
    if not indice:
        messagebox.showerror("Erro", "Selecione uma tarefa para remover.")
        return

    tarefas = carregar_tarefas()
    indice = indice[0]

    del tarefas[indice]
    salvar_tarefas(tarefas)
    messagebox.showinfo("Sucesso", "Tarefa removida com sucesso!")
    listar_tarefas()

# Função para editar uma tarefa
def editar_tarefa():
    indice = lista_tarefas.curselection()
    if not indice:
        messagebox.showerror("Erro", "Selecione uma tarefa para editar.")
        return

    tarefas = carregar_tarefas()
    indice = indice[0]
    
    descricao = simpledialog.askstring("Descrição", "Digite a nova descrição da tarefa:", initialvalue=tarefas[indice]['descricao'])
    prazo = simpledialog.askstring("Prazo", "Digite o novo prazo (DD/MM/AAAA):", initialvalue=tarefas[indice]['prazo'])
    try:
        prazo_data = datetime.strptime(prazo, "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Use o formato DD/MM/AAAA.")
        return

    prioridade = simpledialog.askstring("Prioridade", "Digite a nova prioridade (alta, média, baixa):", initialvalue=tarefas[indice]['prioridade'])
    if prioridade not in ["alta", "média", "baixa"]:
        messagebox.showerror("Erro", "Prioridade inválida. Escolha entre alta, média ou baixa.")
        return

    categoria = simpledialog.askstring("Categoria", "Digite a nova categoria:", initialvalue=tarefas[indice]['categoria'])

    tarefas[indice] = {
        'descricao': descricao,
        'prazo': str(prazo_data),
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': tarefas[indice]['concluida']
    }
    
    salvar_tarefas(tarefas)
    messagebox.showinfo("Sucesso", "Tarefa editada com sucesso!")
    listar_tarefas()

#Interface Gráfica
root = tk.Tk()
root.title("Gerenciador de Tarefas")

frame = tk.Frame(root)
frame.pack(pady=10)

lista_tarefas = tk.Listbox(frame, width=100, height=15)
lista_tarefas.pack()

#Botões
btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

btn_marcar_concluida = tk.Button(root, text="Marcar Como Concluída", command=marcar_tarefa_concluida)
btn_marcar_concluida.pack(pady=5)

btn_remover = tk.Button(root, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(pady=5)

btn_editar = tk.Button(root, text="Editar Tarefa", command=editar_tarefa)
btn_editar.pack(pady=5)

#Iniciar com a lista de tarefas atualizada
listar_tarefas()

#Iniciar o loop da interface gráfica
root.mainloop()
