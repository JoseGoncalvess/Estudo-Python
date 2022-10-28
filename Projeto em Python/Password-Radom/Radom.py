import random

Name = print(input("Como Você se Chama?"))
print("Vamo Criar uma senha Super segura!")
length_pw = print(input("Qual o tamanho da senha desejada?"))

##caracteres##
low_case = "abcdefghijklmnopqrstuvwyxz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
symbol_case = "!@#$%*?\/"
number_case = "01234564789"

user_for = low_case + upper_case + symbol_case + number_case

password = "".join(random.sample(user_for, length_pw))

print(password)
