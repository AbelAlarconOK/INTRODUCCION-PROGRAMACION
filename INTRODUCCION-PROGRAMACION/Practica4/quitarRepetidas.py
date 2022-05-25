#d) una funciÃƒÆ’Ã‚Â³n que se llame quitarRepeticiones que tome dos parÃƒÆ’Ã‚Â¡metros, una
#cadena y una letra, y devuelva otra cadena igual a la anterior pero sin las
#repeticiones de esa letra. Por ejemplo, un programa que llame a la funciÃƒÆ’Ã‚Â³n
#asÃƒÆ’Ã‚Â­: quitarRepeticiones("mate cocido", "c"), deberÃƒÆ’Ã‚Â¡ retornar la cadena "mate
#coido".




def quitarRepeticiones(cadena,letra):
    nuevacadena=""
    for char in cadena:
        if letra not in nuevacadena or letra !=char:
            nuevacadena=nuevacadena+char
    print( nuevacadena)


quitarRepeticiones("mate cocido","c")
