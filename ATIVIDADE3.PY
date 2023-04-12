print('\n1.Crie um programa que verifique se um número é positivo ou negativo e exiba uma mensagem correspondente.')
numero=float(input("Digite um número:"))
if numero >=0.01:
    print("Esse número é positivo.")
else:
    print('Esse número é negativo')


print('\n2.Crie um programa que verifique se um número é múltiplo de 3 e exiba uma mensagem correspondente.')
numero=int(input("Digite um número:"))
resultado=numero%3
if (resultado==0):
    print('É multiplo de 3.')
else:
    print('Não é multiplo de 3.')


print('\n3.Crie um programa que verifique se um número é múltiplo de 5 e exiba uma mensagem correspondente.')
numero=int(input("Digite um número:"))
resultado=numero%5
if (resultado==0):
    print('É multiplo de 5.')
else:
    print('Não é multiplo de 5.')


print('\n4.Crie um programa que verifique se um número é maior ou menor que 10 e exiba uma mensagem correspondente.')
numero=float(input("digite um número:"))
if numero >10:
    print('Esse número é maior que 10.')
elif numero==10:
    print('Esse é o número 10.')
else:
    print('Esse número é menor que 10.')


print('\n5.Crie um programa que verifique se um número é maior ou menor que 100 e exiba uma mensagem correspondente.')
numero=float(input("digite um número:"))
if numero >100:
    print('Esse número é maior que 100.')
elif numero==100:
    print('Esse é o número 100.')
else:
    print('Esse número é menor que 100.')


print('\n6.Crie um programa que verifique se uma palavra tem mais de 10 caracteres e exiba uma mensagem correspondente.')
texto=str(input("digite uma palavra aleatória:"))
n=len(texto)
if n >10:
    print('Essa palavra tem mais de 10 caracteres.')
elif n==10:
    print('Essa palavra tem 10 caracteres.')
else:
    print('Essa palavra não tem mais de 10 caracteres.')


print('\n7.Crie um programa que verifique se uma palavra tem mais de 20 caracteres e exiba uma mensagem correspondente.')
texto=str(input("digite uma palavra aleatória:"))
n=len(texto)
if n >20:
    print('Essa palavra tem mais de 20 caracteres.')
elif n==20:
    print('Essa palavra tem 20 caracteres.')
else:
    print('Essa palavra não tem mais de 20 caracteres.')


print('\n8.Crie um programa que verifique se uma pessoa é maior de idade (idade >= 18) e exiba uma mensagem correspondente.')
numero=int(input("digite sua idade:"))
if numero >=18:
    print('Você já é maior de idade.')
else:
    print('Você não é maior de idade.')


print('\n9.Crie um programa que verifique se uma pessoa é menor de idade (idade < 18) e exiba uma mensagem correspondente.')
numero=int(input("digite sua idade:"))
if numero <18:
    print('Você é menor de idade.')
else:
    print('Você é maior de idade.')


print('\n10.Crie um programa que verifique se uma pessoa é homem ou mulher e exiba uma mensagem correspondente.')
sexo=str(input("digite seu sexo(homem-h,mulher-m):"))
if sexo == "h":
    print('Você é homem.')
if sexo == "m":
    print('Você é mulher')


print('\n11.Crie um programa que verifique se uma pessoa é solteira ou casada e exiba uma mensagem correspondente.')
est=str(input("digite seu estado civil (solteiro(a)-s,casado(a)-c):"))
if est == "s":
    print('Você é solteiro(a).')
if est == "c":
    print('Você é casado(a)')


print('\n12.Crie um programa que verifique se um número é par ou ímpar e exiba uma mensagem correspondente.')
est=int(input("Digite um número:"))
num= est%2
if (num==0):
    print('Esse número é par.')
if (num!=0):
    print('Esse número impar.')


print('\n13.Crie um programa que verifique se uma pessoa tem mais de 18 anos e é solteira e exiba uma mensagem correspondente.')
idade=int(input("Digite sua idade:"))
estado=str(input("digite seu estado civil (solteiro(a)-s ou não-n):"))
if idade >=18 and estado =="s":
    print('Você é maior de idade e solteiro(a).')
elif estado=="n" and idade >=18:
    print('Você é maior de idade e não é solteiro(a).')
else:
    print('Você é menor de idade.')


print('\n14.Crie um programa que verifique se uma pessoa tem mais de 18 anos e é casada e exiba uma mensagem correspondente.') 
idade=int(input("Digite sua idade:"))
estado=str(input("digite seu estado civil (casado(a)-c ou não-n):"))
if idade >=18 and estado =="s":
    print('Você é maior de idade e casado(a).')
elif estado=="n" and idade >=18:
    print('Você é maior de idade e não é casado(a).')
else:
    print('Você é menor de idade.')


print('\n15.Crie um programa que verifique se um número é positivo, negativo ou zero e exiba uma mensagem correspondente.')
numero=float(input("Digite um número:"))
if numero >0:
    print("Esse número é positivo.")
elif numero <0:
    print('Esse número é negativo')
else:
    print("Esse número é zero.")


print('\n16.Crie um programa que verifique se um número é primo ou não e exiba uma mensagem correspondente.')
num=int(input('Digite um número:'))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é um número primo")
            break
    else:
        print(num, "é um número primo")
else:
    print(num, "não é um número primo")


print('\n17.Crie um programa que verifique se um número é um ano bissexto ou não e exiba uma mensagem correspondente.')
ano=int(input('Digite um ano:'))
if ano %100!=0 and ano%400==0 or ano%4==0:
    print("Esse é um ano bissexto.")
else:
    print('Esse não é um ano bissexto.')


print('\n18.Crie um programa que verifique se uma pessoa tem direito a voto (idade>=18) e exiba uma mensagem correspondente.')
voto=int(input('Digite sua idade:'))
if voto >=18:
    print('Você já tem direito a voto.')
else:
    print('Você ainda não pode votar.')


print('\n19.Crie um programa que verifique se uma pessoa pode dirigir (idade>=18 e habilitação válida) e exiba uma mensagem correspondente.')
idade=int(input('Digite sua idade:'))
cnh=str(input('Você tem CNH (sim ou não)?'))
if idade >= 18 and cnh == 'sim':
    print('Você pode dirigir.')
else:
    print('Você não pode dirigir.')


print('\n20.Crie um programa que verifique se um número é divisível por 3 ou 5 e exiba uma mensagem correspondente.')
nume=int(input('Digite um número:'))
if nume%3==0 and nume%5==0:
    print('Esse número é divisível por três e por cinco.')
    if nume%3==0:
        print('Esse número é divisível por três.')
    elif nume%5==0:
        print("Esse nuúmero é divisível por cinco.")
else:
    print('Esse número não é divisível por três nem por cinco.')

