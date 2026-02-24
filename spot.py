import numpy as np
import math
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# clien id -
# client secret -   


client_id = 'TU_CLIENT-ID'
client_secret = 'TU_CLIENT_SECRET'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# https://open.spotify.com/playlist/ "playlist url"
# playlist id 

playlist_id = 'ID_PLAYLIST_SELECCIONADA'

offset = 0
tracks = []
while True:
    datos = sp.playlist_tracks(playlist_id, offset = offset)
    if not datos['items']:
        break
    for item in datos['items']:
        track = item['track']
        track_name = track['name']
        artist_names = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
#       album_cover_url = track['album']['images'][0]['url']  (imagenes)
        popularity = track['popularity']
        tracks.append([track_name, artist_names, album_name, popularity])
    offset += len(datos['items'])
df = pd.DataFrame(tracks, columns=['Track', 'Artista', 'Album', 'Popularity'])

# FORMAS DE ACOMODAR EL CUADRO #

# ALEATORIO (todo)
# df = df.sort_values(by='Artista', ascending=True, inplace=True) #ver, el ultimo termino
# canciones = df['Track'].sample(frac=1).values   

# POPULARIDAD (cancion)
df = df.sort_values(by='Popularity', ascending=False) #ver, el ultimo termino
canciones = df['Track'].values   

# SEGUIDORES (artista)  (no anda)
# artist_id = track['artists'][0]['id']
# artist_info = sp.artist(artist_id)
# followers = artist_info['followers']['total']
 
####################################

N = len(canciones)
P = 2**math.ceil(math.log2(N))
byes = P - N                          # opcion b eliminarlos

cN_II = df['Track'].head(byes).values
cN_I = df['Track'].tail(N-byes).values

def Vs(x,y):
    while True:
        print("Elegir, VS")
        print(x, "vs", y)
        rta = input("1 o 2:")
        if rta == '1':  
            return x
            break
        elif rta == '2': 
            return y
            break
        else:
            print("no válido")

def bracket(A):
    B=[]
    for i in range(int(len(A)/2)):
        Bji = Vs(A[i],A[len(A) - int(i) -1 ]) 
        B.append(Bji)
    return B

cN_II = np.append(cN_II, bracket(cN_I))

print("......................")
print(cN_II)

def cuadro(A):
    n = len(A)
    cni=[]
    cni.append(bracket(A))
    print("......................")
    print(cni)
    for i in range(int(math.log2(n) - 1)):
        cni.append(bracket(cni[i]))
        print("......................")
        print(cni[i+1])  
    return cni[int(math.log2(n) - 1)]

Ganador = cuadro(cN_II)
print("El ganador es:")
print(Ganador)
