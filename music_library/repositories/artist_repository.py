from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['first_name'], result['last_name'], result['id'])
    return artist

def albums(artist):
    albums = []

    sql  = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)

    return albums
