from unicodedata import name
from random import shuffle

List = list (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
Table_frc = { "a" : 0.0834,
                'b' : 0.0154,
                'c' : 0.0273,
                'd' : 0.0414,
                "e": 0.1260,
                'f' : 0.0203,
                'g' : 0.0192,
                'h' : 0.0611,
                'i' : 0.0671,
                'j' : 0.0023,
                'k' : 0.087,
                'l' : 0.0424,
                'm' : 0.0253,
                "n" : 0.0680,
                "o" : 0.0770,
                'p' : 0.0166,
                'q' : 0.0009,
                'r' : 0.0568,
                's' : 0.0611,
                "t": 0.0937,
                'u' : 0.0285,
                'v' : 0.0106,
                'w' : 0.0234,
                'x' : 0.0020,
                'y' : 0.0204,
                'z' : 0.0006,
             }
Message = input("Entre votre message : ")
print("La clef doit etre < 26")
while True : 
    clef = int (input("Entre votre clef : "))
    if(clef > 0 and clef < 26):
        break

Message = Message.lower()
def chiffre_lettre(lettre, liste, clef) :
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste[i] == lettre:
            if clef + i > 25:
                k = (clef + i) % 26
                return str(liste[k])
            else:
                return str(liste[clef + i])
    return '?'

def dechf_lettre(lettre, liste, clef):
    for i in range(len(liste)):
        if lettre == ' ':
            return ' '
        elif liste[i] == lettre:
            if i - clef < 0:
                k = (i - clef) % 26
                return str(liste[k])
            else:
                return str(liste[i - clef])
    return '?'
        
Message_chff = str()


for lettre in Message:
    Message_chff += chiffre_lettre(lettre, List, clef)

Message_dech = str()
# Chaine_a_Dec = str('RdcvgpijapixdcndjhjrrthhujaanqgtpzRtphtgrxewtg')
Fichier = open('Chf.txt','r')
Chaine_a_Dec = Fichier.read()
print (Chaine_a_Dec)
Chaine_dec = str()

for lettre in Message_chff:
    Message_dech += dechf_lettre(lettre, List, clef)

Message_a_dech = str()
for lettre in Chaine_a_Dec:
     Message_a_dech += dechf_lettre(lettre, List, 9)

FileDe = open('texteClair.txt','a')
FileDe.write(Message_dech)

Lists_Decr = {}


for i in range(27):
    for lettre in Chaine_a_Dec.lower():
        Chaine_dec += dechf_lettre(lettre, List, i)
    FileDe.write('\n' + Chaine_dec + ' ' + str(i))
    Chaine_dec =''

def calcule_freq(chaine):
    for lettre in List:
            Lists_Decr[lettre] = float( chaine.count(lettre)) / float(len(chaine))
    return Lists_Decr

def Freq_Dech ():
    ChaineDecrypte = str()
    b = float()
    result = {}
    for i in range(27):
        for lettre in Chaine_a_Dec.lower():
            ChaineDecrypte += dechf_lettre(lettre, List, i)
        a = calcule_freq(ChaineDecrypte)
        for lettre in List:
           b  += abs(a[lettre] - Table_frc[lettre])
        result[i] = b
        b =  0
        ChaineDecrypte =''
    return result

  


if __name__ == '__main__':
    FileCh = open('D:\Crypto_Algo\TP1\TextChiffe.txt','w')
    FileCh.write(Message_chff)
    print(Freq_Dech())
    print('Le Message chiffré : '+ Message_chff)
    print('Le Message déchifré : '+ Message_dech)
    print('Le Message dech : '+ Message_a_dech)