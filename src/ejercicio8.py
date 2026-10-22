from collections import namedtuple

Articulo = namedtuple('Articulo', [
    'nombre',       # tipo str
    'categoria',    # tipo str
    'precio',       # tipo float
    'fecha_caducidad'  # tipo date
])

def vende_articulos(articulos: list[Articulo], objetivo_ganancia: float, descuentos: dict[str, float]) -> tuple[list[Articulo], float]:
    """
    Dada una lista de artículos de alimentación, un objetivo de ganancia y un diccionario de descuentos por categoría,
    devuelve una lista de artículos vendidos y la ganancia total obtenida.

    Si una categoría no aparece en el diccionario de descuentos, no se aplica ningún descuento a los artículos de esa categoría.

    Los artículos vendidos se retiran de la lista de artículos recibida. 

    Los artículos se venden empezando por los que tengan una fecha de caducidad más próxima. Si algún artículo
    ya está caducado (su fecha de caducidad ya ha pasado), no se vende pero se retira de la lista recibida.

    Parámetros:
    articulos (list[Articulo]): Lista de artículos disponibles para la venta.
    objetivo_ganancia (float): La ganancia mínima que se desea obtener.
    descuentos (dict[str, float]): Diccionario con categorías como claves y porcentajes de descuento como valores.

    Devuelve:
    tuple[list[Articulo], float]: Una tupla con la lista de artículos vendidos y la ganancia total obtenida.
    """
    # TODO: Borra este comentario y la instrucción pass, e implementa la función
    pass