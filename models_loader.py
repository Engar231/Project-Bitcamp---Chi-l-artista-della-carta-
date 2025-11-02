from tensorflow.keras.models import load_model
# _____________________________________________CONFIG PATH_____________________________________________
MODELLO_MACRO_PATH = r"D:\Programmazione\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\dataset\BestMacro.keras"
MODELLO_BRISCOLA_PATH = r"D:\Programmazione\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\dataset\carte_briscola\ottobrebriscola.keras"

# _____________________________________________FUNZIONI DI CARICAMENTO_____________________________________________
def get_modello(tipo="macro"):
    if tipo == "macro":
        return load_model(MODELLO_MACRO_PATH)
    elif tipo == "briscola":
        return load_model(MODELLO_BRISCOLA_PATH)
    else:
        raise ValueError(f"Tipo modello non valido: {tipo}")

