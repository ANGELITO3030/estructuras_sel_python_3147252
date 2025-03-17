estado_civil = input("digita tu estado civil(soltero/casado/comprometido)")
edad = int(input("digita tu edad: "))
temperamento = input("digita tu temperamento (buena persona/mala persona)")
fisico = input("digita tu fisico (lindo/a/feo/a)")
salario= int(input("digita tu salario: "))
if estado_civil == "casado" or estado_civil == "comprometido":
    print("no puedes acercarte a esa persona")
elif edad < 18:
    print("no puedes acercarte a esa persona, po que no tienes la sificiente edad ")
elif temperamento == "mala persona":
    print("no puedes acercarte a esa persona, por que te genera estres")
elif fisico == "feo/a":
    print("no puedes acercarte a esa persona,por que no te atrae fisicamente")
elif salario   < 3000000:
    print("no puedes acercarte a esa persona,no gana lo suficiente")
    
else:
    print("puedes acercarte a esa persona")
print("fin del programa")