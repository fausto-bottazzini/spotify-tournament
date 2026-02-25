# Spotify Playlist Tournament

Este proyecto permite transformar cualquier playlist de Spotify en un cuadro de eliminación directa (torneo). Es una herramienta que combina la integración de datos externos con lógica de estructuras de datos para organizar enfrentamientos entre canciones.
Se toman todas las canciones de una playlist elegida y se ordenan según popularidad, a partir de esto se crea un cuadro de eliminación directa y se vá dando al usuario a elegir en cada cruce de canciones.
Actualmente funciona todo por consola, próxima mejora crear toda una interfaz de usuario estétcia. Hace falta contar con `Client ID` para la API. 

## Funcionalidades
- **Conexión con Spotify API:** Autenticación y extracción de metadatos de canciones (título, artista, álbum).
- **Lógica de Torneo:** Implementación de un algoritmo de "bracket" para generar cruces de forma dinámica según el tamaño de la playlist.
- **Interfaz de Usuario:** Sistema de votación para que el usuario elija su canción favorita en cada ronda.

