
def main():
    ruta_libro = "books/frankestein.txt"
    reporte(ruta_libro)

def get_texto(libro):
    with open(libro) as f:
        contenido = f.read()
    return contenido

def cuenta_palabras(texto):
    contador = len(texto.split())
    return(contador)

def cuenta_caracteres(texto):
    minusculas = texto.lower()
    caracteres = {}
    for caracter in minusculas:
        caracteres[caracter] = caracteres.get(caracter, 0) + 1
    return caracteres

def reporte(ruta):
    texto = get_texto(ruta)
    #palabras = cuenta_palabras(texto)
    print(f"--- Begin report of {ruta} ---")
    letras = cuenta_caracteres(texto)
    letras_ordenadas = dict(sorted(letras.items(), key=lambda item: item[1], reverse=True))
    for letra in letras_ordenadas:
        if letra.isalpha():
            print(f"The '{letra}' character was found {letras_ordenadas[letra]} times")
    print("--- End report ---")

main()
