from SokobanGame.Model.constants import coords_str_int, PATH_KEYS, PATH_LEVELS


def teclas(archivo):
    """Crea un diccionario tecla = direccion a partir de un archivo"""
    diccionario = {}
    with open(archivo, 'r') as f:
        for linea in f:
            if linea == "\n":
                continue
            tecla, clave = linea.rstrip("\n").replace(" ", "").split("=")
            clave = coords_str_int.get(clave, clave)
            diccionario[tecla.lower()] = clave
    return diccionario


def niveles_en_lista(archivo):
    """Crea una lista con los niveles del archivo dado"""
    lista_definitiva = []
    listas = []
    with open(archivo, "r") as f:
        for linea in f:
            if linea == "\n":
                lista_definitiva.append(listas)
                listas = []
            if linea[0] != "#" and linea[0] != " ":
                continue
            else:
                listas.append(linea.rstrip("\n"))
    return lista_definitiva


def obtener_movimientos_validos(keys_dict):
    ans = set()
    for clave in keys_dict.keys():
        if not isinstance(keys_dict[clave], str):
            ans.add(clave)
    return ans