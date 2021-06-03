![Tec de Monterrey](images/logotecmty.png)
# Busqueda en lista
Listas- Buscar una palabra dentro de una lista

El programa se encuentra en el directorio `srs`, y el archivo se llama
`exercise.py`

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

Escribe un programa que pide una serie de palabras, y las va insertando
en una lista.
Este proceso se detiene cuando el usuario da como entrada un string vacio
(sólo teclea **Enter** sin ningun texto).

Después de esto el programa debe pedir otro sting mas, e imprimir
**Encontrado** si el nuevo string es uno de los elementos de la lista, o
imprimir **No encontrado** si no existe ese string en la lista.

La linea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La linea que dice  `pass` la puedes borrar. Su proposito es evitar que
el programa genere errores porque la función `main` esté vacia.

La salida del proframa debe de ser exactamente de la siguiente forma:

```plaintext
**Tom**
**Emma**
**Alex**
**Mary**

Search for? **Mary**
Mary was found!
```

```plaintext
**Tom**
**Emma**
**Alex**
**Mary**

Search for? **Logan**
Logan was not found!
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':`
 por el momento. No la vamos a necesitar para este programa,
 pero es una buena práctica incluirla y quedará más claro para que sirve
 en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a
tu repositorio en GitHub, con el proceso de commit + push.
