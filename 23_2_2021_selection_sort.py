import math

def selectionsort(liste):

    def minimum(liste, x):
        #returns tuple of minimum in liste[x:len(liste)] and index of minimum
        kandidat = (liste[x], x)
        for i in range(x, len(liste)):
            if (liste[i]<kandidat[0]):
                kandidat = (liste[i], i)

        return kandidat

    sorted_partition = []
    for i in range(len(liste)):
        min_tuple = minimum(liste, i)
        liste[min_tuple[1]] = liste[i]
        liste[i] = min_tuple[0]

    return liste

def Nullstellen(a, b, c, d):

    def loeseQuadratischeGleichung(a, b, c):
        if (a==0):
            if (b==0 and c!=0):
                return None

            elif (b==0 and c==0):
                return "unendlich"

        else:
            p = b/a
            q = c/a

            try:
                x1 = -(p/2) - math.sqrt((p/2)**2 - q)
                x2 = -(p/2) + math.sqrt((p/2)**2 - q)

                if x1==x2:
                    return [float(x2)]

                else:
                    return [float(x1), float(x2)]

            except (ValueError):
                return None

    def MaximaStammfunktion(a, b, c, d, startwert):
        schrittweite = 0.0005/b
        x = startwert
        while True:
            g_term = schrittweite * (a*(x**3) + b*(x**2) + c*x + d)
            x += g_term
            if (abs(g_term)<=1e-8):
                return round(x, 10)

    def MinimaStammfunktion(a, b, c, d, startwert):
        schrittweite = 0.0005/b
        x = startwert
        while True:
            g_term = schrittweite * (a*(x**3) + b*(x**2) + c*x + d)
            x -= g_term
            if (abs(g_term)<=1e-8):
                return round(x, 10)

    def finde1Nullstelle(a, b, c, d):
        if (a>0):
            x = MinimaStammfunktion(a, b, c, d, 1)
            return x
        elif (a<0):
            x = MaximaStammfunktion(a, b, c, d, 1)
            return x

    if (a==0): #verhält sich wie quadratische Funktion
        return loeseQuadratischeGleichung(b, c, d)

    else:
        x1 = finde1Nullstelle(a, b, c, d) #eine Nullstelle mit Gradientenverfahren näherungsweise berechnen, nun mit Hornaverfahern weitere Nullstellen berechnen

        a = a*x1+b
        b = (a*x1+b)*x1+c
        c = ((a*x1+b)*x1+c)*x1+d
        weitere_Nullstellen = loeseQuadratischeGleichung(a, b, c)
        weitere_Nullstellen.append(x1)
        return  weitere_Nullstellen

print(Nullstellen(0, 112, -12, -12))
