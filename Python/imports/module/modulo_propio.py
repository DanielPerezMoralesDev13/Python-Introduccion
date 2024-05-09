"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/DanielPerezMoralesDev13
Correo electrónico: danielperezdev@proton.me 
"""
def idValor(valor: str | int | float | bool | list | tuple | dict | set) -> str:
    return f"id {valor=} es " + str(id(valor)) 