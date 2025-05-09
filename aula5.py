nome = input("Digite o nome do aluno: ")
nota1 = float( input("Digite a primeira nota do aluno: ")) #definimos a variavel da nota1 ela é do tipo float para colocar numeros reais nota 2 e 3 tambem
nota2 = float( input("Digite a segunda nota do aluno "))
nota3 = float(input("Digite a terceira nota do aluno"))

media = (nota1 + nota2 + nota3) / 3 #calculo da média 

print(f"a média do aluno é: {media:.0f}")  #f  fstring siginifica para conseguir colocar uma variavel entre as aspas 
# media coloca entre as chaves porque colocamos a variavel media no string 
# :. 2f significa quantas casas apos a virgula.

if media >= 7:
      print("aprovado!")
else:
      print("Reprovado.")
        



