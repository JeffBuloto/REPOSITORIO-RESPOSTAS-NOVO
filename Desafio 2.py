A = ("I like living here")

B = ("She must do her homework")

C = ("They got to do something about this")

#====================================================#
def letra_maior(texto):
    return max(texto.lower(), key=str.lower)

maiorA = letra_maior(A)
maiorB = letra_maior(B)
maiorC = letra_maior(C)
#====================================================#
print(f"A maior letra em minúsculas da primeira frase é: {maiorA}")
print(f"A maior letra em minúsculas da segunda frase é:  {maiorB}")
print(f"A maior letra em minúsculas da terceira frase é: {maiorC}")