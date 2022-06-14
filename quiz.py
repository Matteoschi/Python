#first of all create a text file called history.txt, in this way python will save the results of the various players
DOMANDE = [
    ("Di quale stato fanno parte le Hawaii?", "Stati Uniti"),
    ("Quanti Stati ci sono negli Stati Uniti?", "50"),
    ("Qual è il fiume più lungo d'Italia", "Po"),
    ("Qual è l'oceano più grande del mondo?", "Oceano Pacifico"),
    ("In quale anno è stata sciolta l'Unione Sovietica?", "1991"),
    ("Come è morto Giulio Cesare?", "Assassinato"),
    ("Qual era il nome del Dio del sole nell'antico Egitto?", "Ra"),
    ("In che anno è stato ucciso John F. Kennedy", "1963"),
    ("Dov'è il deserto del Gobi?", "Asia"),
    ("Qual è la lingua più parlata al mondo?", "mandarino"),
    ("Qual è il paese più popolato del mondo", "Cina"),
    ("In quale anno è stato creato il World Wide Web?", "1991"),
    ("Chi è stato il primo presidente degli Stati Uniti?", "George Washington"),
    ("Come si chiama la famosa battaglia in cui fu sconfitto Napoleone Bonaparte?", "Waterloo"),
    ("Come è stata distrutta la biblioteca di Alessandria?", "saccheggiata"),
    ("Quanti anni è durata la Guerra dei 100 anni", "116"),
    ("Chi ha vinto la guerra del Vietnam?", "Vietnam del Nord"),
    ("Di chi è la canzone CANZONE?", "Lucio Dalla"),
    ("Come è morto Vincent Van Gogh?", "Suicidio"),
    ("Chi ha scritto LE METAMORFOSI?", "Ovidio"),
    ("Da dove provengono i Giochi Olimpici?", "Grecia"),
    ("Chi ha vinto la Coppa nel Mondo 2014?", "Germania"),
    ("Quale stile di nuoto è il più lento?", "Rana"),
    ("Dove è stata inventata la pallavolo?", "Stati Uniti"),
    ("Qual è la durata di una partita di calcio?", "90 minuti"),
    ("Dove è stato inventato il ping-pong?", "Inghilterra"),
    ("Quale Paese ha vinto il maggior numero di Mondiali?", "Brasile"),
    ("Con quale frequenza si svolgono i Giochi Olimpici?", "4"),
    ("Il teorema di di Ruffini vale in quale campo della scienza?", "Matematica"),
    ("Quanti grammi sono 100 millilitri?", "100 "),
    ("Come si chiamano le particelle subatomiche a carica negativa? ", "Elettroni"),
    ("Come si chiamano le cellule hanno un nucleo cellulare?", "Cellule eucariote"),
    ("Cosa significa DNA?", "Acido desossiribonucleico"),
    ("Dove si trovano le ossa dello scafoide?", "Polso"),
    ("Qual è la galassia più vicina alla Via Lattea?", "Andromeda"),
    ("Qual è il quarto pianeta del sistema solare?", "Marte"),
    ("Chi ha elaborato la teoria dell'evoluzione?", "Charles Darwin"),
    ("Come si chiama la pigmento che dà alle piante il colore verde?", "Clorofilla"),
    ("Gli ornitorinchi sono mammiferi: veri o falso?", "Vero"),
    ("Quante strisce ci sono sulla bandiera americana?", "13"),
    ("Fino al 1923, come si chiamava la città turca di Istanbul?", "Costantinopoli"),
    ("Qual è il paese più piccolo del mondo?", "Vaticano"),
    ("Qual è la capitale del Canada?", "Ottawa"),
    ("Qual è il nome gergale di New York City, usato dai suoi abitanti?", "Gotham"),
    ("Da quale città provengono i Beatles?", "Liverpool"),
    ("Quale pilota ha vinto il maggior numero di campionati di Formula 1?", "Schumacher")
]
Punti = 1
punti_corretti = 0
giocatore = input("Nome giocatore : ")
file = open("history.txt","a") 
for domande, domande_corrette in DOMANDE:
    risposta = input(f"{domande}? ")
    if risposta == domande_corrette:
        Punti += 1
        punti_corretti +=1
        print("corretto Punti:",Punti)
    else:
        Punti -= 1
        print("la risposta corretta è",domande_corrette,"non è", risposta,"Punti:",Punti)
    if Punti == 0:
        print("hai perso")
        file.write("{}\n".format(giocatore))
        file.write("{}\n".format(punti_corretti))  
        file.close()
        break
