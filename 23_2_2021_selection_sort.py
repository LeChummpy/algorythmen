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
