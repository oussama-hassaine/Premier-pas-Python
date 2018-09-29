annee=0
jour=0
mois=str.lower((input("le mois "))) #choix du mois + transformation en minuscule



def verifj(jour): #fct pour verifer que le jour est valide
    while jour < 1 or jour > 31: # tant que le jour est invalide ou reste dans la boucle
        try:
            jour=int(input("le jour : "))
        except ValueError:
            print("vous n'avez pas rentrer une date valide ")
    return (jour)

jour=verifj(jour)


def verif(annee): #fct pour vérifer que l'on rentre une date valide
    while annee < 1582 or annee > 2199: #tant que l'annee est invalide ou reste dans la boucle
        try:
            annee=int(input("l'année : "))
            global an
            an = int(annee / 100) # on garde les 2 premier chiffre de l'année
        except ValueError:
            print("vous n'avez pas rentrer une date valide ")
    return (annee)

annee=verif(annee)

def fin(annee): #fct pour garder que les 2 dernier chiffre de l'année
        f=annee%100 # on enleve le plus de fois 100 afin de garde que des dizaine au maximun
        return (f)
anneef=fin(annee)


def debut(an): # selon les siecle de l'année on determine un montant que l'on ajoutera plus tard a la somme
    if (an >= 16 and annee < 17) or (an >= 20 and an < 21):
        v=6
    elif (an >= 17 and an < 18) or (an >= 21 and annee < 22):
        v=4
    elif an >= 18 and annee < 19:
        v=2
    elif an >= 19 and an < 20:
        v=0
    return (v)

d=debut(an)


def bisextile(annee): # si l'année est bissextiles et le mois janvier ou fevrier on enleve 1 sinon cela reste a 0
    biss = 0
    if annee % 4 == 0 and annee % 100 !=0:
        biss = 1
    elif annee % 400 == 0:
        biss = 1
    else:
        biss = 0
    if biss == 1 and mois == 'janvier' or mois == 'fevrier':
        return -1
    else:
        return 0

c = bisextile(annee)

def calcul(jour,mois,annee,c,d,anneef): #fonction qui calcule la somme de l'annee avec le jour etc
    quart=anneef//4 # on determine le quart des 2 dernier chiffre de l'année

    if mois == "janvier" or mois == "octobre": # les conditions qui selon le mois determine b
        b=0
    elif mois == "fevrier" or mois == "mars" or mois == "novembre":
        b = 3
    elif mois == "avril" or mois == "juillet":
        b=6
    elif mois == "mai":
        b=1
    elif mois == "juin":
        b=4
    elif mois == "aout":
        b =2
    elif mois =="septembre" or mois == "decembre":
        b=5
    else:   # si le mois est invalide on quitte le prog
        print("vous avez rentrez un mois invalide")
        exit()
    a = anneef+(quart)+jour+b+d+c # expression du calcule
    return (a)

r=calcul(jour,mois,annee,c,d,anneef) #on appel la fonction qui calcule



def jourj(r): #sert a determiner le jour selon le modulo 7
    r=r%7
    if r==0:
        return ("dimanche")
    elif r==1:
        return ("lundi")
    elif r==2:
        return ("mardi")
    elif r==3:
        return ("mercredi")
    elif r==4:
        return ("jeudi")
    elif r==5:
        return ("vendredi")
    elif r ==6:
        return ("samedi")

deter=jourj(r) #on appel la fonction qui determine le jour de la semaine

print("le jour est un ",deter)
