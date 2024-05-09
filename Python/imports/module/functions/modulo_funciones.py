"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/DanielPerezMoralesDev13
Correo electrónico: danielperezdev@proton.me 
"""
def TipoDato(dato:str | int | float | bool | list | tuple | dict | set) -> str:
    return type(dato)