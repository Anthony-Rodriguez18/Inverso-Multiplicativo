def EUCLIDES(a,b):
    if b == 0:
        return a
    else:
        return EUCLIDES(b, a%b)

def EUCLIDESEXT(a,b):
    if b == 0:
        return(a,1,0)
    else:
        (d,x1,y1) = EUCLIDESEXT(b, a%b)
        aux = a/b
        p= int(aux)
        (x,y) = (y1, x1-(p*y1))
        return(d,x,y)

def inverso(a,n):
    if n < 0:
        m = "Número no válido, ingrese solo números positivos"
        return m
        
    if EUCLIDES(a,n) == 1:
        (p,x,y)=EUCLIDESEXT(a,n)
        m = "El inverso es: " , x%n
        return m
    else:
        m = "El número no tiene inverso"
        return m 


x = inverso(4,7)
print(x)

