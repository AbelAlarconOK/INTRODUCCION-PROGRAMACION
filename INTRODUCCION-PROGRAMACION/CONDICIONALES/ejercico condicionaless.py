#DADA TRES NOTAS PARCIALES. IDICAR SI SE PROMOCIONA, VA A FINAL O RECURSA
#SABIENDO QUE:
#[0,4)RECURSA
#[4,7) FINAL
#[7,10] PRMOCIONA

nota1=int(input("primer nota"))
nota2=int(input("segunda nota"))
nota3=int(input("tercer nota"))
resultado=(nota1+nota2+nota3)/3
if resultado >= 7:
    print("promociona")
else:
    if resultado < 4:
        print("recursa")
    else:
        print("final")
