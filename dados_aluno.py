from fpdf import FPDF

nome = input('Olá aluno(a), qual seu nome?: ')

print(f'\nSeja bem vindo(a), {nome}. Nos informe algumas informações sobre você para calcularmos seu IMC:\n')

idade = input('Qual sua idade?: ')
peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
  classificação = 'Abaixo do peso'
  mensagem = 'Atenção! seu IMC está abaixo do normal!'
elif IMC < 24.9:
  classificação = 'Peso normal'
  mensagem = 'Parabéns, seu IMC está normal!'
elif IMC < 29.9:
  classificação = 'Sobrepeso'
  mensagem = 'Atenção! seu IMC está acima do normal!'
elif IMC < 34.9:
  classificação = 'Obesidade grau I'
  mensagem = 'Atenção! seu IMC está acima do normal!'
elif IMC < 39.9:
  classificação = 'Obesidade grau II'
  mensagem = 'Atenção! seu IMC está acima do normal!'
elif IMC < 49.9:
  classificação = 'Obesidade grau III'
  mensagem = 'Atenção! seu IMC está acima do normal!'
elif IMC < 59.9:
  classificação = 'Obesidade grau IV'
  mensagem = 'Atenção! seu IMC está acima do normal!'
else:
  classificação = 'Obesidade grau V'
  mensagem = 'Atenção! seu IMC está acima do normal!'

pdf = FPDF()

pdf.add_page()

template_ficha = r"C:\Users\renam\OneDrive\Área de Trabalho\git_github\projeto_imc\template_ficha.png"

pdf.image(template_ficha, x = 0, y = 0)

pdf.set_font('Arial', '', 14)

pdf.text(56, 126, nome)
pdf.text(56, 139, idade)
pdf.text(56, 152, str(peso))
pdf.text(56, 165, str(altura))
pdf.text(56, 179, str(round(IMC, 2)))

pdf.set_font('Arial', 'B', 18)

pdf.text(56, 192, mensagem)

pdf.output('ficha_aluno.pdf')

print('Parabéns, sua ficha foi gerada com sucesso!')