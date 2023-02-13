# Project

Hello new developers; Now is the time to start working on your project.
Hangman game! is the name of the project; If you want to know how to play this game, check the link below.

https://www.youtube.com/watch?v=leW9ZotUVYo

## Instructions
- Read all the bank of words or phrases from the JSON file. Select one and start the game.
- You will always receive numbers and letters, not symbols(except blank characters)
- Use everything you have learned so far, and try new things. Not include classes.
- Try to create the best user experience in your terminal.

## Bonus
- write tests.

### What was your creative process:
El primer paso es realizar la lectura del archivo .json, se requiere importar la libreria sjon para esto.
Luego se cargar ese dato en una variable para ingresar a ese dato y poder utilizar los datos dentro de la lista, pero antes leyendo el diccionario  que lo contiene.
Luego necesitamos de manera aleatoria un valor que este dentro de la lsita, para ello existe la libreria random, pero como en el juego del ahorcado no importa si es mayuscula o minuscula podemos colocar usando upper o lower la palabra, pero en este caso es mas facil trabajar con las minusculas 

Luego colocamos en numero de intentos que suele ser 5.
Tambien debemos mostrarle al usuario que usará el programa la cantidad de digitos que tendra que adivinar, capturamos la longitud de la palabra seleccionada de manera aleatoria y lo multiplicamos por un caracter caulquiera, usualmente se usa el "_" para simular la escritura.
luego definimos  variable de intentos internos para calculo y otro de contador descendente para notificar intentos que le quedan a l usuario
Ahora finalmente podemos hacer la lógica del juego, para lo cual se necesitan 2 restricciones, si es igual y el numero de intentos que no lleguen al tope establecido.
Ahora tenemos que comparar si el caracter digitado está dentro de la palabra y cuantas veces existe para realizar su reemplazo. Y en caso sea erroneo mostar un mensaje de error y descontando un intento, notificando al usuario sobre cuantos intentos le quedan
Si el usuario llega al limite establecido, se le debe notificar y mostrar la palabra final cerrando el programa para poder volver a ejecutarlo