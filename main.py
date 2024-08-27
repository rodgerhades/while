#while

senha = "python123"
tentativa =""

print("Bem vindo! Por favor digite sua senha")

while tentativa != senha:
    tentativa = input("Digite sua senha: ")
    if tentativa != senha:
        print("senha incorreta. tente novamente")
        
print("senha correta! Acesso permitido")
        