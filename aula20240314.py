#primeiroPrograma

print('Olá mundo!')
nome = 'Gabriel'
print('Bem vindo,', nome + '!')
x=7
y=9
print(int((x+y)/2))

#taximetro

titulo = "Taxímetro"
print(f"{titulo:^30}")
bandeira = float(input("Qual o valor da bandeira? "))
custo_quilometro = float(input("Qual o valor do quilometro rodado? "))
quilometro = float(input("Quantos quiloetros foram rodados? "))
custo = bandeira + custo_quilometro * quilometro
print("O custo da corrida é de", custo, "reais.")

#conversor

farenheit = float(input("Qual a temperatura em graus Farenheit? "))
celsius = (farenheit - 32) / 9 * 5
print("A temperatura é de", celsius, "graus Celsius.")