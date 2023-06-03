# bot_logic in original

import random

shacocounterliste = ["hecarim","nunuve willump","talon","rengar","jarvan IV","lillia"]
counter_heros = {"hecarim": 0,"nunuve willump": 0,"talon": 0,"rengar": 0,"jarvan IV": 0,"lillia": 0}
def atik():
    cumle1 = 'Temizlik sağlığın temelidir!'
    cumle2 = 'Temizlik düzenin anahtarıdır!'
    cumle3 = 'Temiz bir çevre, mutlu bir yaşamın temelidir!'
    liste = [cumle1, cumle2, cumle3]
    return random.choice(liste)