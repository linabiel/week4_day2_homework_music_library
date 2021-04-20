import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Billie", "Jones")
artist_repository.save(artist_1)

artist_2 = Artist("Merlin", "Manson")
artist_repository.save(artist_2)

album_1 = Album("Greatest Hits", "blues", artist_1,)
album_2 = Album("Beautiful People", "metal", artist_2)

album_repository.save(album_1)
album_repository.save(album_2)

pdb.set_trace()
