A = ("Jonathan Kimble Simmons")

B = ("Manoj Nelliattu Shyamalan")

C = ("Jerome David Salinger")

#====================================#

def sigla_nome(nome_completo):
    partes = nome_completo.split()
    sobrenome = partes[-1].upper()
    iniciais = [parte[0].upper() + "." for parte in partes[:-1]]
    return f"{sobrenome}, {' '.join(iniciais)}"


#====================================#

print(sigla_nome(A))
print(sigla_nome(B))
print(sigla_nome(C))