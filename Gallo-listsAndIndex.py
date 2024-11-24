sostantivo = str(input("Inserisci qui un sostantivo singolare (tutte minuscole) per scoprirne il genere! "))
femminili_particolari = ["luce", "colazione","nave", "eco"]
maschili_particolari = ["mare", "cuore", "amore","bene","male","calice","fulmine","pane","cane","cellulare","bicchiere","leone", "papa", "papà"]
consonanti = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x","z" ]
if sostantivo[-4:] == "ista" and sostantivo[-5:] != "vista" and len(sostantivo) > 5:
    print("Questo sostantivo può essere sia maschile che femminile in base al contesto.")
elif sostantivo[-1] == "a" or sostantivo[-1] == "à" and sostantivo not in maschili_particolari or sostantivo[-1] == "i" or sostantivo in femminili_particolari: 
    print("Femminile")
elif sostantivo[-1] == "o" or sostantivo[-1] in consonanti or sostantivo in maschili_particolari: 
    print ("Maschile")
