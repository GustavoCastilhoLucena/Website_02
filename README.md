# Informações do Repositório

Esse repositório retrata um desafio de desenvolvimento web para a faculdade Fatec, com a proposta de criar um website.

## Pastas

### Statics

Contém os arquivos de estilo em cascata que foi utilizado para todo o projeto, sendo esses arquivos:

#### normalize.css

Contém os dados de estilo para padronizar o website, de forma que ele se mantenha da mesma forma em diversos navegadores.

#### estilo.css

Contém os estilos a serem implantados nas páginas, como formatação de imagem e formatação de texto.

### Imagens

Contém todas as imagens que foram alocadas no website, sendo essas a logo, a capa, o fundo da aba "home" e o fundo das abas "contato" e "quem somos".

### Templates

Contém todas as abas do website em formato de HTML (Hypertext), sendo essas:

#### base.html

É uma aba invisível para o usuário do website, tem toda a base fundamental que se repetiria em todas as abas, ela tem a função de diminuir o tamanho dos arquivos.

#### home.html

Contém a aba inicial, onde se encontra a capa e a apresentação do site.

#### contato.html

Contém um sistema de envio de email com entrada para escrever uma carta.

#### quem_somos.html

Contém uma descrição do pessoal do site com algumas curiosidades.

### app.py

contém o sistema que interliga as abas HTML

## Requisitos

Os requisitos são um navegador, preferencialmente o Google, o Visual Studio Code, dentro do Visual Studio Code a extensão Python, pelo terminal a criação da pasta "venv" e a instalação e execução do Flask, para poder acessar o website pelo navegador.

### Visual Studio Code

É possível instalar o Visual Studio Code pelo website da Microsoft, pesquisando em um navegador ou diretamente pelo seguinte link:

link do vscode

### Extensão Python

Dentro do Visual Studio Code, deve-se, dentro da aba de extensões, pesquisar "Python" e instalar a primeira extensão a aparecer.

### venv

A pasta venv deve ser criada toda vez na qual esses arquivos foram descarregados em um aparelho computador diferente. Com a extensão Python instalada, abrir o terminal do Visual Studio Code, colocar os seguintes comandos:

```
apt get update
py -m venv venv
```

Instalação e execução do Flask

Para instalar e executar o Flask, siga os comandos abaixo:

```
py -m pip install Flask
Flask run
```

Agora, aparecerá um link em formato de protocolo IP, onde, segurando o botão Control, deve-se clicar com o botão esquerdo do mouse.
Para navegar pelas abas do website pode-se clicar nos links em formato de nome no canto superior direito da tela.
