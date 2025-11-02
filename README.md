# Bitcamp_End_Project/EasyOCR,Tesseract,Read_TGC_Artist
Progetto di fine corso per Bitcamp
Il programma utilizza pytesseract & easyocr per inviduare, tramite crop selezionato a mano, il punto in cui trovare il nome illustratore e scriverlo nell'interfaccia. (Main.py)
All'interno del dataset trovere i modelli addestrati, sia per le macro aree (One piece, magic, digimon etc etc) e uno a parte per le micro aree (tutte le briscole).
Essendo il dataset delle briscole fatto completamente a mano, con immagini prese su internet e quelle che tenevo a casa non è molto ricco ed ho dovuto inventare uno stratagemma per renderlo almeno "utilizzabile".

**IMPORTANTE**
Nel main utilizzo come directory la mia cartella personale, in questo caso cambiatela! Sennò non partirà mai.

Per farlo funziona bisogna installare tesseract-ocr (Ho messo l'installer di Windows, visto che è quello che ho utilizzato io) con i vari pacchetti linguistici e i vari installer di Python.
All'interno trovate delle carte con cui ho fatto dei test , non presenti nel dataset.
Nota : 
° Essendo un lettore ottico, le immagini a 60pixel o 120pixel fa fatica a leggerli, cercate almeno immagini che abbiano la scritta nitida o leggermente sgranata. 
° Il modello è stato addestrato a 224x224, non ho voluto usare altri programmi o metodi per mostrare anche le performance del mio PC.

C'è molto margine di miglioramento ed è sicuramente un progetto che approfondirò nel tempo libero a disposizione.
