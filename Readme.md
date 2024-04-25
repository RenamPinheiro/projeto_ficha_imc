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

Exemplo de Saída
----------------

Segue abaixo um exemplo de saída do código após a execução:


```
Olá aluno(a), qual seu nome?: João

Seja bem vindo(a), João. Nos informe algumas informações sobre você para calcularmos seu IMC:

Qual sua idade?: 25 
Qual seu peso?: 70 
Qual sua altura?: 1.75  
Parabéns, sua ficha foi gerada com sucesso!
```

Após a execução, um arquivo PDF chamado `ficha_aluno.pdf` será gerado no mesmo diretório do script contendo os resultados do cálculo do IMC.

Visualização da Ficha Gerada
----------------------------

A ficha gerada pelo script apresenta os resultados do cálculo do IMC de forma clara e organizada. Abaixo está uma visualização da ficha em formato PDF:

![image](https://github.com/RenamPinheiro/projeto_ficha_imc/assets/118815226/15a0c9ce-fe09-4a45-a56c-d3a526bcd7c3)


