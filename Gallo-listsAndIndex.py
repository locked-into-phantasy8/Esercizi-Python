sostantivo = str(input("Inserisci qui un sostantivo (tutte minuscole) per scoprirne il genere! "))
e_femminili = ["luce", "colazione","nave"]
e_maschili = ["mare", "cuore", "amore","bene","male","calice","fulmine","pane","cane","cellulare","bicchiere","leone"]
if sostantivo[-1] == "a" or sostantivo in e_femminili: 
    print("Femminile")
elif sostantivo[-1] == "o" or sostantivo in e_maschili:
    print ("Maschile")
else:
  print("Ci dispiace, non conosciamo ancora il genere di questo sostantivo.")