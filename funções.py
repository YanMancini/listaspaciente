import os
import random as r
fila=[]
numbre=[]
op=1
fazer=0
def mostrarlista():
    os.system("cls")
    print ("-----------------------------\n")
    for fil in fila:print (fil)
    print ("-----------------------------\n")
    print ("o que deseja fazer?\n1-adicionar\n2-remover\n3-Chamar o próximo paciente.\n4-Mostrar os próximos N pacientes.\n5-Mostrar o total de pacientes na fila.\n6-Buscar um paciente pelo nome.")
    fazer=int(input(" "))

def adicionarpaciente(op):
    while op!="ss":
        os.system("cls")

        fila.append(input("Adicione os pacientes na lista"))
        sort=r.randrange(0, 100)
        numbre.append(sort)
        op=(input("adicionar mais um paciente?"))
def removerpaciente():
    while op!="ss":
        os.system("cls")
        fila.pop()
        op=(input("remover mais um paciente?"))
