# Clase: Anotaciones
# https://platzi.com/home/clases/10002-python/71732-anotaciones-de-tipo/

# Tipos Avanzados:
print("\fTipos Avanzados:")
print("1. Union: Permite indicar múltiples tipos posibles.")
from typing import Union

def multiplicar(valor: Union[int, float]) -> float:
    return valor * 2

print(multiplicar(10.6))

print("\n2. Optional: Permite indicar que un argumento puede ser None.")
from typing import Optional

def obtener_nombre(usuario_id: int) -> Optional[str]:
    if usuario_id == 1:
        return "Alice"
    return None
print(obtener_nombre(1))

print("\n3. Any: Permite cualquier tipo de dato, ideal cuando no se conoce el tipo exacto.")
from typing import Any

def procesar_dato(dato: Any) -> None:
    print(f"Dato procesado: {dato}")

procesar_dato(True)

