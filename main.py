import funcoes # Importei as funções que defini anteriormente 
import sys # Importa o módulo sys para sair do programa

treinos = []

def main():

    funcoes.registrar_log("Iniciando menu interativo")
    funcoes.carregar_dados(treinos)

    while True: # Criando mensagem de introdução ao menu interativo 
        funcoes.limpar_terminal()
        print("""
------------- Sistema de registro de treinos -------------
                  1 - Cadastrar treino
                  2 - Listar treinos existentes 
                  3 - Editar treinos existentes 
                  4 - Deletar treinos 
                  5 - Sair do menu
--------------------------------------------------------
""")

        try:
            # Tratamento de entrada para evitar crash
            escolha_do_usuario = int(input("Escolha a opção desejada: "))
        except ValueError:
            funcoes.registrar_log("Usuário informou uma opção inválida (não-numérica)")
            print("Opção inválida. Por favor, digite um número de 1 a 5.")
            input("Pressione Enter para continuar...")
            continue # Volta para o início

        funcoes.limpar_terminal()
        print(f"Opção escolhida: {escolha_do_usuario}\n")

        if escolha_do_usuario == 1:
            funcoes.cadastrar_treino(treinos)
            funcoes.registrar_log("Cadastrar treino")
        elif escolha_do_usuario == 2:
            funcoes.listar_treinos(treinos)
            funcoes.registrar_log("Listar treinos existentes")
        elif escolha_do_usuario == 3:
            funcoes.editar_treino(treinos) 
            funcoes.registrar_log("Editar treinos existentes")
        elif escolha_do_usuario == 4:
            funcoes.deletar_treino(treinos)
            funcoes.registrar_log("Deletar treinos existentes")
        elif escolha_do_usuario == 5:
            print ("Saindo do menu...")
            funcoes.registrar_log("Saindo do menu")
            sys.exit(0) # Encerra o programa
        else:
            print("Opção inválida. Digite uma opção válida (1 a 5).")
            funcoes.registrar_log("Usuário informou uma opção inválida")
        
        # Pausa para o usuário ver o resultado da operação antes de limpar o terminal
        input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()
