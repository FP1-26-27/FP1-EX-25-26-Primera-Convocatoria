from collections import namedtuple

Articulo = namedtuple('Articulo', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_caducidad'  # tipo date
])

def categoria_precio_medio_menor(articulos: list[Articulo]) -> str:
    """
    Dada una lista de artículos de alimentación, devuelve la categoría
    cuya media de precios es menor. Aunque en la lista puede haber varios
    artículos repetidos, sólo se deben tener en cuenta los artículos únicos 
    (mismo nombre, categoria y precio, aunque puede variar la fecha de caducidad)
    para calcular la media de precios.

    Si la lista de artículos está vacía, debe devolverse una cadena vacía.

    Parámetros:
    articulos (list[Articulo]): Lista de artículos disponibles.

    Devuelve:
    str: La categoría con la media de precios menor. Si la lista está vacía,
         devuelve una cadena vacía.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass