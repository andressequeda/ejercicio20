def  invertir ( número ):
    invertido  =  ""
    para  numero  en  número :
        invertido  =  n  +  invertido
    volver  invertido


numero  =  str ( input ( "Ingrese un número entero a invertir:" ))
imprimir ( invertir ( numero ))