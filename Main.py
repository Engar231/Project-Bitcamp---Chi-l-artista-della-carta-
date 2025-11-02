# _____________________________________________IMPORT & SETUP_____________________________________________
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import easyocr
import difflib
import pytesseract
from models_loader import get_modello
from dizionario import artisti_poke, artisti_magic, artisti_one, artisti_digi, storie_briscola, storie_macro, nomi_macro, nomi_briscola
from OCR_utils import pulisci_nickname

modello_macro = get_modello("macro")
modello_briscola = get_modello("briscola")

# _____________________________________________TESSERACT + OCR_____________________________________________
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Carica immagine 
lingueOCR = easyocr.Reader(['en','fr','de','it','es','pl'])

def ocr_generico(img, lang='eng+fra+jpn'):
    testo = pytesseract.image_to_string(img, lang=lang)
    testo = pulisci_nickname(testo)
    
    if not testo.strip():
        results_easy = lingueOCR.readtext(img, detail=0)
        testo = pulisci_nickname(" ".join(results_easy))

    return testo
# _____________________________________________DEFINIZIONI TESSERACT MAGIC_____________________________________________
def artista_mtg(img):
    h, w = img.shape[:2]
    x1, y1 = 0, int(h*0.90)
    x2, y2 = int(w*0.80), h

    roi = img[y1:y2, x1:x2]
    roi_clean = roi[:, int(roi.shape[1]*0.10):]
    roi_zoom = cv2.resize(roi_clean, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(roi_zoom, cv2.COLOR_BGR2GRAY)
    roi_inv = cv2.bitwise_not(gray)

    nickname = ocr_generico(roi_inv)
    match = difflib.get_close_matches(nickname, artisti_magic, n=1, cutoff=0.75)
    return match[0] if match else nickname


# _____________________________________________DEFINIZIONI TESSERACT DIGIMON_____________________________________________
def artista_digimon(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    x1 = int(img_rotated.shape[1] * 0.75)  
    y1 = int(img_rotated.shape[0] * 0.95)  
    x2 = img_rotated.shape[1]              
    y2 = img_rotated.shape[0]              
    x2 = int(img_rotated.shape[1] * 0.93)  
    roi = img_rotated[y1:y2, x1:x2]
    scale_factor = 3
    roi_zoom = cv2.resize(roi, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    nickname = ocr_generico(roi_zoom)
    match = difflib.get_close_matches(nickname, artisti_digi, n=1, cutoff=0.75)
    return match[0] if match else nickname
# _____________________________________________DEFINIZIONI TESSERACT ONE PIECE_____________________________________________
def artista_onepiece(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    x1 = int(img_rotated.shape[1] * 0.75)  
    y1 = int(img_rotated.shape[0] * 0.95)  
    x2 = img_rotated.shape[1]              
    y2 = img_rotated.shape[0]              
    x2 = int(img_rotated.shape[1] * 0.93)  
    roi = img_rotated[y1:y2, x1:x2]
    scale_factor = 3
    roi_zoom = cv2.resize(roi, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    nickname = ocr_generico(roi_zoom)
    match = difflib.get_close_matches(nickname, artisti_one, n=1, cutoff=0.75)
    nickname_finale= match[0] if match else nickname
    # 💬 DEBUG
    print(f"[DEBUG] Artista MTG rilevato: {nickname_finale}")

    return nickname_finale

# _____________________________________________DEFINIZIONI TESSERACT POKEMON_____________________________________________
def artista_pokemon(img): 
    h, w = img.shape[:2] 
    x1 = 0 
    y1 = int(h*0.94) 
    x2 = int(w*0.95) 
    y2 = h 
    roi = img[y1:y2, x1:x2] 
    cut_left_percentage = 0.0 
    width_to_keep = int(roi.shape[1] * (1 - cut_left_percentage)) 
    roi_clean = roi[:, int(roi.shape[1]*cut_left_percentage):] 
    roi_zoom = cv2.resize(roi_clean, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) 
    lab = cv2.cvtColor(roi_zoom, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    thresh = cv2.adaptiveThreshold(
        l,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        91,
        40
    )
    roi_inv = cv2.bitwise_not(lab) 
    nickname = ocr_generico(thresh)
    match = difflib.get_close_matches(nickname, artisti_poke, n=1, cutoff=0.75)
    return match[0] if match else nickname
    
#__________________________GUI SETUP_____________________________________________
finestra = tk.Tk()
finestra.title("Riconoscimento Carte")
finestra.geometry("880x620")
finestra.configure(bg="black")

font_sub = ("Segoe UI", 8, "italic")
font_title = ("Segoe UI", 16, "bold italic")
font_btn = ("Segoe UI", 12, "bold")
font_risultato = ("Segoe UI", 12, "bold italic")

# _____________________________________________GUI TITOLI E SUBTITOLI_____________________________________________
sottotitolo = tk.Label(finestra, text="BitCamp Presenta:", bg="black", fg="white", font=font_sub)
sottotitolo.pack(anchor="nw", padx=5, pady=5)

titolo = tk.Label(finestra, text="Vuoi sapere la storia e l'artista della carta?", bg="black", fg="white", font=font_title)
titolo.pack(anchor="nw", padx=15, pady=3)

# _____________________________________________FUNZIONE PER CARICARE L’IMMAGINE E PREDIRE_____________________________________________
def carica_immagine():
    percorso_file = filedialog.askopenfilename(filetypes=[("File immagine", "*.jpg;*.jpeg;*.png")])
    if not percorso_file:
        return

    try:
        img_orig = Image.open(percorso_file).convert("RGB")
        disp = img_orig.resize((300, 400))
        img_tk = ImageTk.PhotoImage(disp)
        label_immagine.configure(image=img_tk)
        label_immagine.image = img_tk

        inp = img_orig.resize((224, 224))
        arr = np.array(inp).astype("float32") / 255.0
        arr = arr.reshape(1, 224, 224, 3)

        probs_macro = modello_macro.predict(arr)
        idx_macro = int(np.argmax(probs_macro, axis=1)[0])
        #conf_macro = probs_macro[0, idx_macro]
        nome_macro = nomi_macro.get(idx_macro, f"Indice {idx_macro}")

        testo_risultato = f"Macro: {nome_macro}"
        extra_msg = storie_macro.get(nome_macro, "")
        if extra_msg:
            testo_risultato += f"\n{extra_msg}"

        if idx_macro == 0:
            probs_briscola = modello_briscola.predict(arr)
            idx_briscola = int(np.argmax(probs_briscola, axis=1)[0])
            nome_briscola = nomi_briscola.get(idx_briscola, f"Indice {idx_briscola}")
            testo_risultato += f"\n→ Briscola: {nome_briscola}"
            briscola_extra = storie_briscola.get(nome_briscola, "")
            if briscola_extra:
                testo_risultato += f"\n{briscola_extra}"
        
        carte_artisti = {
            1: artista_digimon,
            5: artista_onepiece,
            4: artista_mtg,
            6: artista_pokemon
        }
        nickname = ""
        if idx_macro in carte_artisti:
            func = carte_artisti[idx_macro]
            nickname = func(cv2.cvtColor(np.array(img_orig), cv2.COLOR_RGB2BGR))
        label_risultato.configure(state="normal")
        label_risultato.delete("1.0", tk.END)
        label_risultato.insert(tk.END, testo_risultato)
        label_risultato.configure(state="disabled")

        if nickname:
            artista_label.configure(text=f"Artista della carta: {nickname}")
        else:
            artista_label.configure(text="Artista della carta: ...")


    except Exception as e:
        label_risultato.configure(state="normal")
        label_risultato.delete("1.0", tk.END)
        label_risultato.insert(tk.END, f"Errore con immagine o modello:\n{e}")
        label_risultato.configure(state="disabled")

#_____________________________________________GUI ICONA + CARICA IMMAGINE_____________________________________________
img = Image.open(r"D:\Programmazione\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\carte.png")
img = img.resize((170, 170)) 
tk_img = ImageTk.PhotoImage(img)
bottone_carica = tk.Button(
    finestra,
    image=tk_img,
    command=carica_immagine,
    bg="black",
    borderwidth=0,
    activebackground="black"
)
bottone_carica.image = tk_img
bottone_carica.place(x=725, y=1)

# _____________________________________________FRAME PRINCIPALE CARTA_____________________________________________
frame_principale = tk.Frame(finestra, bg="black")
frame_principale.pack(expand=True, pady=20)

# _____________________________________________LABEL IMMAGINE CARTA_____________________________________________
label_immagine = tk.Label(frame_principale, bg="black")
label_immagine.pack(side="left",padx=20, pady=10) #tolto side=left e padx20

# _____________________________________________LABEL TESTO + RISULTATO TESSERACT CARTA_____________________________________________
label_risultato = tk.Text(
    frame_principale,
    bg="black",
    fg="white",
    font=font_risultato,
    width=30,      # numero di caratteri
    height=20,     # altezza in righe
    wrap="word"
)
label_risultato.pack(padx=5)
#label_risultato.configure(state="disabled")

artista_label = tk.Label(
    finestra,
    text="Artista: ",
    fg="white",
    bg="black",          # stesso sfondo del frame
    font=font_risultato
)
artista_label.pack(side="bottom", pady=5)



# _____________________________________________AVVIO GUI_____________________________________________
finestra.mainloop()