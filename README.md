#CappyBird
>Jogo desenvolvido em Python, utilizando a biblioteca pygame.

##Sobre o CappyBird
>Tem como referência o jogo FlappyBird, porém devidamente modificado para game com jeito curitibano.
>O jogo se passa no Parque do Barigui, onde o jogador irá submergir no lago barigui e ter que desviar de troncos até completar seu desafio que é chegar aos 10 pontos.

##Estrutura do CappyBird
```

|-----main.py #Arquivo principal da execuçao do jogo
|-----menu.py #Menu inicial do jogo, onde o usuário poderá iniciar o jogo e acessar o menu com informação de como jogar
|-----instruction.py #Tela com informações de como jogar
|-----game.py #Arquivo com o controle da lógica principal do jogo
|-----DRobj.py #Onde estão os parametros dos objetos e cenário do jogo
|-----cappy.py #Arquivo contempla as informações e características de nosso personagem do jogo.
|-----canos.py #Arquivo com a lógica dos obstáculos (troncos)
```
##Como executar o Cappy Bird
>Para criar seu executável, será necessário possuir minimamente o Python na sua versão 3.10. 
>Caso não possua, você deverá baixar o Python em [Python.org/downloads] (Python.org/downloads).
>Após a instalação, abra o CMD ou PowerShell e digite python -V
>Deverá exibir a versão do Python instalada em seu SO.
>Em Macs, o Python já está instalado nativamente. Apenas certifique-se da versão e se necessário, atualize com o comando pip3 install --upgrade pip.
>
>O jogo requer também algumas dependências como:
>pygame, que é a biblioteca essencial para criação de jogos em python;
>random, utilizada para criar elementos de forma aleatória, como os obstáculos do jogo.
>cv2, utilizamos para poder exibir vídeos nas telas quando o usuário perder e ganhar.
>numpy, ajuda no tratamento de grandes volumes de dados numéricos e operações matemáticas complexas
>
>Instale as dependências no Python utilizando o terminal com o comando:
>Windows
```
>[pip] ou [python] install [nome-da-dependencia]
```
>Macs, o comando reconhecido foi pip3
```
>pip3 install [nome-da-dependencia]
```
>Após instalar todas as dependências, execute seu arquivo main.py.
>No terminal, certifique que esteja na pasta do projeto.
>Digite, python main.py e o jogo será aberto em uma nova janela.

##Como jogar o CappyBird
>Com apenas uma tecla você joga o CappyBird.
>Pressione a barra de espaço para nadar e subir. 
>A capivara irá começar a descer caso você não aperte a barra de espaços.
>Você só precisa desviar dos nossos obstáculos, os troncos de arvore para ganhar.


