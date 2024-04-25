Projeto Ficha IMC
=================

O Projeto Ficha IMC é uma aplicação simples em Python que calcula o Índice de Massa Corporal (IMC) com base nas informações fornecidas pelo usuário e gera uma ficha em PDF com os resultados do cálculo.

Funcionalidades
---------------

*   Calcula o IMC com base no peso e altura fornecidos pelo usuário.
*   Classifica o IMC em categorias como "Abaixo do peso", "Peso normal", "Sobrepeso" e diferentes graus de obesidade.
*   Gera uma ficha em PDF contendo informações como nome, idade, peso, altura, IMC e uma mensagem sobre a classificação do IMC.

Pré-requisitos
--------------

*   Ter o Python 3.11.7 (ou versões acima) instalado no sistema.
*   Biblioteca `fpdf` instalada. Você pode instalar utilizando o seguinte comando:
    
    `pip install fpdf`
    

Como usar
---------

1.  Siga as instruções fornecidas no terminal para inserir o nome, idade, peso e altura.
5.  Após inserir as informações, o script calculará o IMC e gerará automaticamente um arquivo PDF contendo uma ficha de academia com os resultados.

Observação
----------

*   Certifique-se de ter a imagem do template `template_ficha.png` no mesmo diretório que o script Python para que a ficha seja gerada corretamente.
