def Aufgabe7():
    def nachPunkten(n):
        def Selektor(element):
            return int(element[2])

        n.sort(key=Selektor)
        return n

    #def nachNachnameVorname(n):


def Aufgabe8():
    def Notenspiegel(noten):
        #Rückgabe: Liste aus Tuplen, wobei: Tuple[0]--> Note und Tuple[1]--> Anzahl

        notenspiegel=[0,0,0,0,0,0]
        for i in noten:
            if i==1:
                notenspiegel[0]+=1
            elif i==2:
                notenspiegel[1]+=1
            elif i==3:
                notenspiegel[2]+=1
            elif i==4:
                notenspiegel[3]+=1
            elif i==5:
                notenspiegel[4]+=1
            elif i==6:
                notenspiegel[5]+=1

        ergebnis=[]
        for i in range(len(notenspiegel)):
            if notenspiegel[i]!=0:
                ergebnis.append((i+1, notenspiegel[i]))
        return ergebnis

def Aufgabe9():
    def median(n):
        n.sort()
        if len(n)%2==1: #wenn länge von n ungerade
            return n[int(((len(n)-1)/2))] #dann gib den in der Mitte stehenden Wert von sortierter liste n zurück

        elif len(n)%2==0: #wenn länge von n gerade
            mittel1=n[int(len(n)/2)-1]
            mittel2=n[int(len(n)/2)]

            return (mittel1+mittel2)/2 #dann gib das arithmetische Mittel der beiden in der Mitte stehenden Werte von sortierter liste n zurück

def Aufgabe10():
    def anzahl(n, notenpunkt):
        count=0
        for i in n:
            if i==notenpunkt:
                count=count+1
        return count

#def Aufgabe11():


def Aufgabe12():
    def buchstaben(n):
        n.sort()
        n.reverse()
        return n

def Aufgabe13():

    def projektion(n, liste_projizierte_spalten):
        indices=[]
        for i in liste_projizierte_spalten: #Welche indices entsprechen den angegebenen Spalten in -liste_projizierte_spalten- ?
            if i in n[0]: #Wenn Spalte existiert
                index_ausgeweahlte_spalte=n[0].index(i)
                indices.append(index_ausgeweahlte_spalte)

            else: #Andernfalls
                raise Exception("Projizierte Spalte " + i + " existiert nicht!")
                return 0

        ergebnis_liste=[]
        for i in range(1, len(n)):
            element=[]
            for j in indices:
                element.append(n[i][j])
            ergebnis_liste.append(element)

        print(ergebnis_liste)

    def selektion(n, preadikat_ausdruck): #Variante 2: preadikat als Ausdruck in Form eines Strings schreiben
                #Beispiel Ausdruck: "Datenfeldx > Datenfeldy"
                #berücksichtigte Operatoren: >, <, =, >=, <=, &, $

        def run_for_one_partial_expression(n, preadikat_ausdruck): #Variante 2: preadikat als Ausdruck in Form eines Strings schreiben

            operator=""
            Datenfeld1=""
            Datenfeld2=""
            index_Datenfeld1=None
            index_Datenfeld2=None

             #Wie lautet der angegebene Operator?
            for i in range(len(preadikat_ausdruck)):
                if preadikat_ausdruck[i]==">":
                    if preadikat_ausdruck[i+1]=="=":
                        operator=">="
                        break
                    else:
                        operator=">"
                        break

                elif preadikat_ausdruck[i]=="<":
                    if preadikat_ausdruck[i+1]=="=":
                        operator="<="
                        break
                    else:
                        operator="<"
                        break

                elif preadikat_ausdruck[i]=="=":
                    operator="="
                    break

            #Wie lautet das erste und das zweite Datenfeld
            if (operator==">" or  operator=="<" or  operator=="="):
                Datenfeld1=preadikat_ausdruck[0:preadikat_ausdruck.index(operator)]
                Datenfeld2=preadikat_ausdruck[preadikat_ausdruck.index(operator)+1:len(preadikat_ausdruck)]

            else:
                Datenfeld1=preadikat_ausdruck[0:preadikat_ausdruck.index(operator[0])]
                Datenfeld2=preadikat_ausdruck[preadikat_ausdruck.index(operator[1])+1:len(preadikat_ausdruck)]


            #Was sind die entsprechenden indices im Tabellenkopf für Datenfeld1 und Datenfeld2?

            index_Datenfeld1=None
            if Datenfeld1 in n[0]: #Wenn Spalte existiert
                index_Datenfeld1=n[0].index(Datenfeld1)
            else:
                raise Exception(Datenfeld1 + "not found.")
                return 0

            index_Datenfeld2=None
            if not(Datenfeld2[0]=="$" and Datenfeld2[-1]=="$"): #Wenn Datenfeld nicht in Tüdelchen ($$)
                if Datenfeld2 in n[0]: #Wenn Spalte existiert
                    index_Datenfeld2=n[0].index(Datenfeld2)
                else:
                    raise Exception(Datenfeld2 + "not found.")
                    return 0

            def check_if_expression_true_2_indexes(zeilen_tuple, index_1, index_2, operator): #Funktion, um zu überprüfen, ob
                Wert1=zeilen_tuple[index_1]
                Wert2=zeilen_tuple[index_2]

                if operator==">":
                    if Wert1>Wert2:
                        return True
                    else:
                        return False

                elif operator=="<":
                    if Wert1<Wert2:
                        return True
                    else:
                        return False

                elif operator=="=":
                    if Wert1==Wert2:
                        return True
                    else:
                        return False

                elif operator==">=":
                    if Wert1>=Wert2:
                        return True
                    else:
                        return False

                elif operator=="<=":
                    if Wert1<=Wert2:
                        return True
                    else:
                        return False

            def check_if_expression_true_1_index(zeilen_tuple, index_1, Wert_2, operator): #Funktion, um zu überprüfen, ob
                Wert1=str(zeilen_tuple[index_1])
                Wert2=Wert_2.replace("$", "")

                if operator==">":
                    if Wert1>Wert2:
                        return True
                    else:
                        return False

                elif operator=="<":
                    if Wert1<Wert2:
                        return True
                    else:
                        return False

                elif operator=="=":
                    if Wert1==Wert2:
                        return True
                    else:
                        return False

                elif operator==">=":
                    if Wert1>=Wert2:
                        return True
                    else:
                        return False

                elif operator=="<=":
                    if Wert1<=Wert2:
                        return True
                    else:
                        return False


            neue_liste=[]
            neue_liste.append(n[0]) #zuerst Tabellenkopf angefügt

            if not(Datenfeld2[0]=="$" and Datenfeld2[-1]=="$"):
                for i in range(1, len(n)):
                    if (check_if_expression_true_2_indexes(n[i], index_Datenfeld1, index_Datenfeld2, operator)):
                        neue_liste.append(n[i])

                return neue_liste

            else:
                for i in range(1, len(n)):
                    if (check_if_expression_true_1_index(n[i], index_Datenfeld1, Datenfeld2, operator)):
                        neue_liste.append(n[i])

                return neue_liste

        preadikat_ausdruck=preadikat_ausdruck.replace(" ", "")
        ausdruecke=preadikat_ausdruck.split("&")
        aktuelle_liste=n
        for i in ausdruecke:
            aktuelle_liste=run_for_one_partial_expression(aktuelle_liste, i)

        return aktuelle_liste
