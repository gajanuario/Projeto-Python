import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},     
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Brasileira', 'ativo':False}]

def exibir_nome_do_programa(): 
    '''Essa função exibe o titulo.'''
    print('🅢 🅐 🅑 🅞 🅡 - 🅔 🅧 🅟 🅡 🅔 🅢 🅢 \n ')

def exibir_opções():
    '''Essa função exibe as opções.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair \n')

def cadastrar_novo_restaurante():       
    '''Essa função cadastra novos restaurantes.
    Inputs: nome do restaurante, categoria.
    Outputs: adiciona um novo restaurante a lista.
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: \n')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!') #f serve para colocar variável dentro de texto
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista os restaurantes.'''
    exibir_subtitulo('Listando os restaurantes')
    
    print(f'{'Nome:'.ljust(20)} | {'Categoria:'.ljust(20)} | {'Estado:'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'] 
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print( f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função volta altera o estado do restaurante.
    Inputs: Nome do restaurante.
    Outputs: Novo estado do restaurante(Ativado, Desativado) ou não encontrado.
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Essa função volta para o menu.
    Inputs: Qualquer tecla.
    Outputs: Volta ao menu principal.
    '''   
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    '''Essa função exibe o subtitulo.'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)  
    print(linha)
    print()

def finalizar_app():
    '''Essa função finaliza o app.'''
    exibir_subtitulo('Encerrando o App')

def opcao_invalida():
    '''Essa função diz que a opção está invalida.'''
    print('Opção invalida! \n')
    voltar_ao_menu_principal()

def escolher_opções():
    '''Essa função define as escolhas.
    Inputs: Escolher uma opção.
    Outputs: Opção 1, 2, 3, 4 ou invalida'''
    try:
        opcao_escolhida = int (input('Escolha uma opção: '))
        #definir variável inteira(int)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opções()

if __name__ == '__main__':
    main()