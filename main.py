meme_dict = {
            "CRINGE": "Algo exepcional raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!")

if word in meme_dict.keys():
    # ¿Que debemos hacer si se encuantra la palabra?
    print(meme_dict[word])
else:
    # ¿Que hacer si no se encuentra la palabra?
    print("Esa palabra no esta en el diccionario")
