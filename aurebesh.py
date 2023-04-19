from unicodedata import normalize


def basic_aurebesh_tranlator():

    text= input("Ingrese el texto que quiere traducir a Aurebesh: ") 
    basic_alphabet = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"}
     

    unicode_text= normalize('NFC', text.lower())

    translated_text = " "

    character_index = 0
    text_len = len(text)

    while character_index < text_len:

            simple_character = unicode_text[character_index]
            double_character = ""

            if character_index < text_len - 1:
                double_character = simple_character + unicode_text[character_index + 1]

            if double_character in basic_alphabet:
                translated_text += basic_alphabet[double_character]
                character_index += 2
            else:
                translated_text += basic_alphabet[simple_character] if simple_character in basic_alphabet else simple_character
                character_index += 1        

    return translated_text

    
print (basic_aurebesh_tranlator())

