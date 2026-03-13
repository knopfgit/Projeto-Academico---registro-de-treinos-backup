import os 
from datetime import datetime

# Estrutura de dados padronizada para um treino
# Usaremos chaves para melhor organização
CHAVES_TREINO = [
    "dia_semana",
    "grupo_muscular",
    "exercicios",
    "series",
    "repeticoes",
    "observacao"
]

def limpar_terminal():
    """Limpa o terminal (compatível com Windows e Linux/macOS)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_log(acao_do_usuario):
    """Registra a ação do usuário no arquivo de log, usando 'with open'."""
    try:
        # Caminho corrigido para a pasta 'Dados'
        with open("Dados/logs.sistema", "a", encoding="utf-8") as arquivo_de_log:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            arquivo_de_log.write(f"[{data_hora}] {acao_do_usuario} \n")
    except FileNotFoundError:
        print("AVISO: Arquivo de log não encontrado. O log não foi registrado.")

def carregar_dados(treinos):
    """Carrega os treinos do arquivo para a lista, com lógica corrigida e tratamento de erro."""
    try:
        # Caminho corrigido para a pasta 'Dados'
        with open("Dados/treinos.sistema", "r", encoding="utf-8") as arquivo_de_treinos:
            linhas = arquivo_de_treinos.readlines()
            
            # Limpa a lista antes de carregar novos dados
            treinos.clear() 
            
            for linha in linhas:
                # Ignora linhas vazias ou de cabeçalho
                if not linha.strip():
                    continue
                
            
                partes = linha.strip().split(";")
                if len(partes) == len(CHAVES_TREINO):
                    treino_dict = dict(zip(CHAVES_TREINO, partes))
                    treinos.append(treino_dict)
                else:
                    registrar_log(f"ERRO: Linha de treino ignorada devido a formato incorreto: {linha.strip()}")
            
    except FileNotFoundError:
        # Cria o arquivo se ele não existir
        print("AVISO: Arquivo de treinos não encontrado. Iniciando com lista vazia.")
        salvar_dados(treinos) # Cria o arquivo vazio
    except Exception as e:
        registrar_log(f"ERRO ao carregar dados: {e}")
        print(f"ERRO: Não foi possível carregar os dados. {e}")

def salvar_dados(treinos):
    """Salva os treinos na lista para o arquivo, usando 'with open' e chaves padronizadas."""
    try:
        # Caminho corrigido para a pasta 'Dados'
        with open("Dados/treinos.sistema", "w", encoding="utf-8") as arquivo_de_treinos:
            for treino in treinos:
                # Garante que a ordem e as chaves estão corretas
                valores = [str(treino.get(chave, '')) for chave in CHAVES_TREINO]
                linha = ";".join(valores) + "\n"
                arquivo_de_treinos.write(linha)
        
    except Exception as e:
        registrar_log(f"ERRO ao salvar dados: {e}")
        print(f"ERRO: Não foi possível salvar os dados. {e}")

def cadastrar_treino(treinos):
    """Pede as informações ao usuário e cadastra um novo treino, usando chaves padronizadas."""
    print("--- CADASTRO DE NOVO TREINO ---")
    
    # Usando variáveis em snake_case 
    dia_semana = input("Informe o dia da semana: ")
    grupo_muscular = input("Informe o Grupo Muscular alvo: ")
    exercicios = input("Liste os exercícios: ")
    series = input("Informe o número de séries: ")
    repeticoes = input("Informe quantas repetições por série: ")
    observacao = input("Informe qual observação você acha relevante cuidar: ")

    # Cria o dicionário com as chaves padronizadas (CHAVES_TREINO)
    novo_treino = {
        "dia_semana": dia_semana,
        "grupo_muscular": grupo_muscular,
        "exercicios": exercicios,
        "series": series,
        "repeticoes": repeticoes,
        "observacao": observacao
    }
    
    treinos.append(novo_treino)
    salvar_dados(treinos)
    print("\nTreino cadastrado com sucesso!")

def listar_treinos(treinos):
    """Lista todos os treinos cadastrados, com correção de sintaxe e exibição."""
    if len(treinos) == 0:
        print("Nenhum treino localizado.")
        return

    print("\n--- LISTA DE TREINOS CADASTRADOS ---")
    for i, treino in enumerate(treinos, 1):
        print(f"--- Treino #{i} ---")
        print(f"Dia da Semana: {treino.get('dia_semana', 'N/A')}")
        print(f"Grupo Muscular: {treino.get('grupo_muscular', 'N/A')}")
        print(f"Exercícios: {treino.get('exercicios', 'N/A')}")
        print(f"Séries: {treino.get('series', 'N/A')}")
        print(f"Repetições: {treino.get('repeticoes', 'N/A')}")
        print(f"Observações: {treino.get('observacao', 'N/A')}")
        print("-" * 20)

def editar_treino(treinos):
    """Função placeholder para edição (não implementada no original, mas necessária)."""
    print("\n--- EDITAR TREINO ---")
    listar_treinos(treinos)
    if not treinos:
        return

    try:
        indice = int(input("Digite o número do treino que deseja editar: ")) - 1
        if 0 <= indice < len(treinos):
            treino = treinos[indice]
            print(f"\nEditando Treino #{indice + 1} - Dia: {treino['dia_semana']}")
            
        
            for chave in CHAVES_TREINO:
                valor_atual = treino.get(chave, '')
                novo_valor = input(f"[{chave.replace('_', ' ').title()}] Valor Atual: '{valor_atual}'. Novo Valor (Enter para manter): ")
                if novo_valor:
                    treino[chave] = novo_valor
            
            salvar_dados(treinos)
            print("\nTreino editado com sucesso!")
        else:
            print("Número de treino inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def deletar_treino(treinos):
    """Função placeholder para deleção (não implementada no original, mas necessária)."""
    print("\n--- DELETAR TREINO ---")
    listar_treinos(treinos)
    if not treinos:
        return

    try:
        indice = int(input("Digite o número do treino que deseja DELETAR: ")) - 1
        if 0 <= indice < len(treinos):
            treino_deletado = treinos.pop(indice)
            salvar_dados(treinos)
            print(f"\nTreino do dia '{treino_deletado['dia_semana']}' deletado com sucesso!")
        else:
            print("Número de treino inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
