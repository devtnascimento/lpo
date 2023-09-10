
from aima3.logic import expr, FolKB, fol_fc_ask 

clauses = []

# Pedro e Antonia criou quatro filhos, o João, a Clara,
# o Francisco e a Ana.

# teste descendencia
clauses.append(expr('Progenitor(Tenorio, Flavio)'))
clauses.append(expr('Progenitor(Flavio, Pedro)'))


clauses.append(expr('Progenitor(Pedro, Joao)'))
clauses.append(expr('Progenitor(Pedro, Clara)'))
clauses.append(expr('Progenitor(Pedro, Francisco)'))
clauses.append(expr('Progenitor(Pedro, Ana)'))
clauses.append(expr('Progenitor(Antonia, Joao)'))
clauses.append(expr('Progenitor(Antonia, Clara)'))
clauses.append(expr('Progenitor(Antonia, Francisco)'))
clauses.append(expr('Progenitor(Antonia, Ana)'))

# Que a Ana teve duas filhas, a Helena e a Joana
clauses.append(expr('Progenitor(Ana, Helena)'))
clauses.append(expr('Progenitor(Ana, Joana)'))

# Mário é filho do João
clauses.append(expr('Progenitor(Joao, Mario)'))

# o Carlos nasceu da relação entre a Helena, muito formosa, e o Mário
clauses.append(expr('Progenitor(Mario, Carlos)'))
clauses.append(expr('Progenitor(Helena, Carlos)'))

# Clara era mãe de Pietro e Enzo
clauses.append(expr('Progenitor(Clara, Pietro)'))
clauses.append(expr('Progenitor(Clara, Enzo)'))


##################################################################################################
# Casais

# Francisco não teve filhos, mas casou-se com Milene
clauses.append(expr('Casal(Fransisco, Milene)'))

# o Carlos nasceu da relação entre a Helena, muito formosa, e o Mário
clauses.append(expr('Casal(Mario, Helena)'))

# Pedro e Antonia criou quatro filhos, o João, a Clara,
# o Francisco e a Ana.
clauses.append(expr('Casal(Pedro, Antonia)'))

# sexo
clauses.append(expr('Sexo(Antonia, Feminino)'))
clauses.append(expr('Sexo(Clara, Feminino)'))
clauses.append(expr('Sexo(Ana, Feminino)'))
clauses.append(expr('Sexo(Helena, Feminino)'))
clauses.append(expr('Sexo(Joana, Feminino)'))
clauses.append(expr('Sexo(Clara, Feminino)'))
clauses.append(expr('Sexo(Milene, Feminino)'))

clauses.append(expr('Sexo(Pedro, Masculino)'))
clauses.append(expr('Sexo(Joao, Masculino)'))
clauses.append(expr('Sexo(Fransisco, Masculino)'))
clauses.append(expr('Sexo(Mario, Masculino)'))
clauses.append(expr('Sexo(Carlos, Masculino)'))
clauses.append(expr('Sexo(Pietro, Masculino)'))
clauses.append(expr('Sexo(Enzo, Masculino)'))

####################################################################################################
# Irmaos
clauses.append(expr('Progenitor(x, y) & Progenitor(x, z) ==> Irmao(y, z)'))


# Tios
clauses.append(expr('Progenitor(x, y) & Irmao(x, z) ==> Tio(z, y)'))
clauses.append(expr('Tio(x, y) & Sexo(x, Feminino) ==> Tia(x, y)'))

# Avos
clauses.append(expr('Progenitor(x, y) & Progenitor(y, z) ==> Avoo(z, y)'))
clauses.append(expr('Avoo(x, y) & Sexo(x, Feminino) ==> Avoa(x, y)'))

# primo
clauses.append(expr('Progenitor(x, y) & Progenitor(w, z) & Irmao(x, w) ==> Primo(y, z)'))
clauses.append(expr('Primo(x, y) & Sexo(x, Feminino) ==> Prima(y, z)'))

# Descendente
clauses.append(expr('Progenitor(x, y) ==> Descendente(y, x)'))
clauses.append(expr('Progenitor(x, y) & Descendente(x, z) ==> Descendente(y, z)'))

# Ascendente
clauses.append(expr('Descendente(x, y) ==> Ascendente(y, x)'))

genealogia = FolKB(clauses)

perguntas = [
    "Sexo(x, y)",
    "Irmao(x, y)",
    "Tio(x, y)",
    "Tia(x, y)",
    "Primo(x, y)",
    "Prima(x, y)",
    "Avoo(x, y)",
    "Avoa(x, y)",
    "Descendente(x, y)",
    "Ascendente(x, y)"
]


for p in perguntas:
    resposta = fol_fc_ask(genealogia, expr(p))
    print(f"{p} -> {list(resposta)}")




