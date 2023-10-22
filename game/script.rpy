# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # $ w = 0
    # while True:
        # if w == 4: 
            # return
        # $ semana = 'semana_' + str(w)
        # call expression semana
        # $ w = w + 1

    # This ends the game.

    # Observações de Miguel, o ancap favorito de todos desse grupo:
    # Existem 8 minigames de dragndrop no projeto:
    # Para cada linguagem: python, java, ruby e lua;
    # foi feito um minigame de Hello World e um minigame de BubbleSort.
    # Cada minigame tem um comando de setup, um comando de call screen, e uma label...
    # ... cujo nome é obrigatório, para que o minigame devolva o controle do jogo...
    # para a história.
    # Se a label que assumir o controle da história tiver nome diferente do que foi...
    # ... designado, o jogo irá quebrar.
    # Essa é a label start.
    # A label start chama os comandos $setup_python_hw_puzzle() e call screen python_hw_puzzle...
    # ... para arrumar e transitar, respectivamente, para o jogo de hello world do python.
    # Após o jogo de Hello World do python ser concluído, ele passa o controle do jogo para a label...
    # label python_hw_complete.
    # No caso, um setup puzzle e uma call screen encerram a label atual.
    # Portanto é obrigatório que todos os conteúdos multimídia da história na label sejam exibidos antes...
    # ... do jogo de arrastar ser executado.
    # No código abaixo, cada minigame transita para label escrita imediatamente a seguir.
    # No caso, puzzle de hw python puzzle invoca a label python hw complete.
    # A label python hw complete invoca o jogo java hw puzzle, que transita para a label java hw complete.
    # E assim por diante, conforme exibido na sequência.

    $setup_python_hw_puzzle() 
    call screen python_hw_puzzle

    label python_hw_complete:
        $setup_java_hw_puzzle()
        call screen java_hw_puzzle
    
    label java_hw_complete:
        $setup_ruby_hw_puzzle()
        call screen ruby_hw_puzzle
    
    label ruby_hw_complete:
        $setup_lua_hw_puzzle()
        call screen lua_hw_puzzle
    
    label lua_hw_complete:
        $setup_python_bs_puzzle()
        call screen python_bs_puzzle
    
    label python_bs_complete:
        $setup_java_bs_puzzle()
        call screen java_bs_puzzle
    
    label java_bs_complete:
        $setup_ruby_bs_puzzle()
        call screen ruby_bs_puzzle
    
    label ruby_bs_complete:
        $setup_lua_bs_puzzle()
        call screen lua_bs_puzzle
    
    label lua_bs_complete:

    return