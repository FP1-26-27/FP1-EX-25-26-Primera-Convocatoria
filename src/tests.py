from datetime import date, timedelta
import math

from ejercicio1 import aproxima_numero_e
from ejercicio2 import expandir_cadena_incremental
from ejercicio3 import obtener_siguiente_lunes
from ejercicio4 import inserta_elementos
from ejercicio5 import comprueba_tablero_correcto
from ejercicio6 import limpiar_lineas_tetris
from ejercicio7 import categoria_precio_medio_menor, Articulo
from ejercicio8 import vende_articulos

def test_ejercicio1():
    print("Probando aproxima_numero_e...", flush=True, end="")
    
    # Caso base: 1 iteración (n=0) -> 1/0! = 1.0
    assert aproxima_numero_e(1) == 1.0
    
    # 2 iteraciones: 1 + 1/1! = 2.0
    assert aproxima_numero_e(2) == 2.0
    
    # 3 iteraciones: 1 + 1 + 1/2! = 2.5
    assert aproxima_numero_e(3) == 2.5
    
    # Comprobamos convergencia con margen de error para floats
    val_100 = aproxima_numero_e(100)
    assert abs(val_100 - math.e) < 0.0000001
    
    print("OK", flush=True)

def test_ejercicio2():
    print("Probando expandir_cadena_incremental...", flush=True, end="")
    assert expandir_cadena_incremental("abc") == "abbccc"
    assert expandir_cadena_incremental("Hola") == "Hoolllaaaa"
    assert expandir_cadena_incremental("123") == "122333"
    assert expandir_cadena_incremental("123 56") == "122333 55555666666"
    print("OK", flush=True)

def test_ejercicio3():
    print("Probando obtener_siguiente_lunes...", flush=True, end="")
    
    # Caso 1: La fecha dada es lunes -> Debería devolver el lunes de la semana siguiente (+7 días)
    lunes_ref = date(2023, 10, 30) # Es lunes
    assert obtener_siguiente_lunes(lunes_ref) == date(2023, 11, 6)
    
    # Caso 2: La fecha es domingo -> Debería devolver el día siguiente
    domingo_ref = date(2023, 10, 29)
    assert obtener_siguiente_lunes(domingo_ref) == date(2023, 10, 30)
    
    # Caso 3: La fecha es martes -> Debería devolver el lunes de la semana siguiente
    martes_ref = date(2023, 10, 31)
    assert obtener_siguiente_lunes(martes_ref) == date(2023, 11, 6)
    
    # Caso 4: Cambio de año
    viernes_ref = date(2023, 12, 29)
    assert obtener_siguiente_lunes(viernes_ref) == date(2024, 1, 1)
    print("OK", flush=True)

def test_ejercicio4():
    print("Probando inserta_elementos...", flush=True, end="")
    
    # Caso 1: un solo elemento a insertar
    lista = [10, 20, 30, 40, 50]
    elementos = [(0, 77)] 

    resultado = inserta_elementos(lista, elementos)
    assert resultado == [77, 10, 20, 30, 40, 50]

    # Probamos que la función no modifique la lista recibida
    copia_lista = lista.copy()
    inserta_elementos(lista, elementos)
    assert lista == copia_lista
    
    # Caso 2: varios elementos a insertar
    lista = [10, 20, 30, 40, 50]
    elementos = [(2, 99), (0, 77)]
    
    resultado = inserta_elementos(lista, elementos)
    assert resultado == [77, 10, 20, 99, 30, 40, 50]
    
    # Caso 3: un elemento fuera de rango
    lista = [10, 20, 30, 40, 50]
    elementos = [(2, 99), (0, 77), (10, 88)] # (10, 88) está fuera de rango
    
    resultado = inserta_elementos(lista, elementos)
    assert resultado == [77, 10, 20, 99, 30, 40, 50]
    
    # Caso 4: Lista vacía
    assert inserta_elementos([], [(0, 1)]) == [1]
    
    print("OK", flush=True)

def test_ejercicio5():
    print("Probando comprueba_tablero_correcto...", flush=True, end="")
    
    # Caso 1: Tablero correcto 5x3
    tablero_ok = [
        [False, False, False],
        [True,  True,  False],
        [False, True,  False],
        [True,  True,  True],
        [False, False, False]
    ]
    assert comprueba_tablero_correcto(tablero_ok) == True
    
    # Caso 2: Menos de 5 filas
    tablero_corto = [[False]*3] * 4
    assert comprueba_tablero_correcto(tablero_corto) == False
    
    # Caso 3: Filas de distinta longitud
    tablero_irregular = [
        [False, False],
        [False, False, False],
        [False, False],
        [False, False],
        [False, False]
    ]
    assert comprueba_tablero_correcto(tablero_irregular) == False
    
    # Caso 4: Valores que no son bool 
    tablero_invalido = [
        [False, "X", False],
        [False, False, False],
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]
    assert comprueba_tablero_correcto(tablero_invalido) == False

    print("OK", flush=True)

def test_ejercicio6():
    print("Probando limpiar_lineas_tetris...", flush=True, end="")
    
    # Caso 1: Sin líneas completas
    tablero = [
        [False, False, False],
        [True,  False, True],
        [False, False, False],
        [True,  True,  False],
        [False, False, False]
    ]
    copia_tablero = [f.copy() for f in tablero]
    lineas = limpiar_lineas_tetris(tablero)
    assert lineas == 0
    assert tablero == copia_tablero # No debe cambiar
    
    # Caso 2: Con 1 línea completa
    tablero = [
        [False, True, False, False],
        [True,  True, True, True],  # Completa
        [False, False, True, False],
        [True,  False, True, False],
        [True,  False, True, True]
    ]
    lineas = limpiar_lineas_tetris(tablero)
    assert lineas == 1
    # Verificamos estado final: debe entrar una fila vacía arriba
    tablero_esperado = [
        [False, False, False, False], # Nueva vacía
        [False, True, False, False],
        [False, False, True, False],
        [True,  False, True, False],
        [True,  False, True, True]
    ]
    assert tablero == tablero_esperado


    # Caso 3: Con 2 líneas completas (una abajo y otra en medio)
    tablero = [
        [False, True, False, True],
        [True,  True, True, True],  # Completa
        [False, False, True, True],
        [True,  True, True, True],  # Completa
        [True,  False, True, True]
    ]
    
    lineas = limpiar_lineas_tetris(tablero)
    assert lineas == 2
    
    # Verificamos estado final: deben entrar 2 filas vacías arriba
    # y las filas incompletas deben bajar.
    tablero_esperado = [
        [False, False, False, False], # Nueva vacía
        [False, False, False, False], # Nueva vacía
        [False, True,  False, True], # La original fila 0
        [False, False, True, True],  # La original fila 2
        [True,  False, True, True]   # La original fila 4
    ]
    assert tablero  == tablero_esperado

    print("OK", flush=True)

def test_ejercicio7():
    print("Probando categoria_precio_medio_menor...", flush=True, end="")
    
    # Caso 1: No hay artículos duplicados
    articulos = [
        Articulo("Leche", "Lácteos", 1.0, date(2024,1,1)),
        Articulo("Queso", "Lácteos", 3.0, date(2024,1,1)),
        Articulo("Pan",   "Panadería", 1.75, date(2024,1,1)),
        Articulo("Muffin","Panadería", 2.5, date(2024,1,1))
    ]
    assert categoria_precio_medio_menor(articulos) == "Lácteos"    
    
    # Caso 2: Articulos con duplicados
    articulos = [
        Articulo("Leche", "Lácteos", 1.0, date(2024,1,1)),
        Articulo("Leche", "Lácteos", 1.0, date(2024,1,5)), # Duplicado (mismo nombre/cat/precio)
        Articulo("Queso", "Lácteos", 4.0, date(2024,1,1)),
        Articulo("Pan",   "Panadería", 1.5, date(2024,1,1)),
        Articulo("Muffin","Panadería", 3, date(2024,1,1))
    ]
    assert categoria_precio_medio_menor(articulos) == "Panadería"
    
    # Caso 3: Lista vacía
    assert categoria_precio_medio_menor([]) == ""
    
    print("OK", flush=True)

def test_ejercicio8():
    print("Probando vende_articulos...", flush=True, end="")
    
    hoy = date.today()
    ayer = hoy - timedelta(days=1)
    mañana = hoy + timedelta(days=1)
    pasado = hoy + timedelta(days=2)
    
    articulos = [
        Articulo("Caducado", "A", 10.0, ayer),
        Articulo("Barato",   "B", 10.0, mañana),
        Articulo("Caro",     "A", 50.0, pasado),
        Articulo("Extra",    "B", 20.0, pasado)
    ]
    
    objetivo = 15.0
    descuentos = {"A": 10.0, "B": 0.0} # 10% dto en A
    
    vendidos, ganancia = vende_articulos(articulos, objetivo, descuentos)
    
    assert len(vendidos) == 2
    assert vendidos[0].nombre == "Barato"
    assert vendidos[1].nombre == "Caro"
    assert abs(ganancia - 55.0) < 0.001
    
    # Verificamos efectos colaterales en la lista original
    # "Caducado" debió ser borrado por caducidad.
    # "Barato" y "Caro" borrados por venta.
    # "Extra" debe quedar.
    assert len(articulos) == 1
    assert articulos[0].nombre == "Extra"

    # Caso 2: Una categoría no aparece en el diccionario de descuentos
    articulos = [
        Articulo("Caducado", "A", 10.0, ayer),
        Articulo("Barato",   "B", 10.0, mañana),
        Articulo("Caro",     "A", 50.0, pasado),
        Articulo("Extra",    "B", 20.0, pasado)
    ]
    
    objetivo = 15.0
    descuentos = {"A": 10.0} # 10% dto en A
    
    vendidos, ganancia = vende_articulos(articulos, objetivo, descuentos)
    
    assert len(vendidos) == 2
    assert vendidos[0].nombre == "Barato"
    assert vendidos[1].nombre == "Caro"
    assert abs(ganancia - 55.0) < 0.001

    # Caso 3: Se venden todos los productos sin alcanzar el objetivo de ganancia
    articulos = [
        Articulo("Caducado", "A", 10.0, ayer),
        Articulo("Barato",   "B", 10.0, mañana),
        Articulo("Caro",     "A", 50.0, pasado),
        Articulo("Extra",    "B", 20.0, pasado)
    ]
    
    objetivo = 150.0
    descuentos = {"A": 10.0, "B": 0.0} # 10% dto en A
    
    vendidos, ganancia = vende_articulos(articulos, objetivo, descuentos)
    
    assert len(vendidos) == 3
    assert vendidos[0].nombre == "Barato"
    assert vendidos[1].nombre == "Caro"
    assert vendidos[2].nombre == "Extra"
    assert ganancia == 75.0

    # Verificamos efectos colaterales en la lista original
    # que debe quedar vacía
    assert len(articulos) == 0

    print("OK", flush=True)

###############################################
# Descomenta las pruebas que quieras ejecutar #
###############################################

# test_ejercicio1()
# test_ejercicio2()
# test_ejercicio3()
# test_ejercicio4()
# test_ejercicio5()
# test_ejercicio6()
# test_ejercicio7()
# test_ejercicio8()