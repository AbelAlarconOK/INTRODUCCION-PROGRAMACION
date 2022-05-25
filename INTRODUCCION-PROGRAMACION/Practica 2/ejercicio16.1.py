año=int(input("aÃ±o"))

if( not(año % 100 == 0 and año % 400!=0) and año % 4 ==0):
    print("bisiesto")
else:
    print("no bisisto")