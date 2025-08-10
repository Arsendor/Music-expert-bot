import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS spotify_data (
                id INTEGER PRIMARY KEY,
                energy REAL,
                tempo REAL,
                danceability REAL,
                playlist_genre TEXT,
                loudness REAL,
                liveness REAL,
                valence REAL,
                track_artist TEXT,
                time_signature INTEGER,
                speechiness REAL,
                track_popularity INTEGER,
                track_href TEXT,
                uri TEXT,
                track_album_name TEXT,
                playlist_name TEXT,
                analysis_url TEXT,
                track_id TEXT,
                track_name TEXT,
                track_album_release_date TEXT,
                instrumentalness REAL,
                track_album_id TEXT,
                mode INTEGER,
                key INTEGER,
                duration_ms INTEGER,
                acousticness REAL,
                playlist_subgenre TEXT,
                type TEXT,
                playlist_id TEXT
            )''')
            conn.commit()

    def executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def select_data(self, sql, data=tuple()):
        """
        Универсальный метод для выполнения SQL-запросов с параметрами
        """
        conn = sqlite3.connect(self.database)
        try:
            with conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                results = cur.fetchall()
                return results if results else []
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return [f"Error: {e}"]
        finally:
            conn.close()

    def select_by_energy(self, energy):
        if energy is None or energy == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE energy = ?'
        return self.select_data(sql, (energy,))
    
    def select_by_tempo(self, tempo):
        if tempo is None or tempo == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE tempo = ?'
        return self.select_data(sql, (tempo,))
        
    def select_by_danceability(self, danceability):
        if danceability is None or danceability == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE danceability = ?'
        return self.select_data(sql, (danceability,))

    def select_by_loudness(self, loudness):
        if loudness is None or loudness == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE loudness = ?'
        return self.select_data(sql, (loudness,))

    def select_by_liveness(self, liveness):
        if liveness is None or liveness == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE liveness = ?'
        return self.select_data(sql, (liveness,))

    def select_by_valence(self, valence):
        if valence is None or valence == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE valence = ?'
        return self.select_data(sql, (valence,))

    def select_by_track_artist(self, track_artist):
        if track_artist is None or track_artist.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_artist LIKE ?'
        return self.select_data(sql, (f'%{track_artist}%',))

    def select_by_time_signature(self, time_signature):
        if time_signature is None or time_signature == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE time_signature = ?'
        return self.select_data(sql, (time_signature,))
    
    def select_by_speechiness(self, speechiness):
        if speechiness is None or speechiness == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE speechiness = ?'
        return self.select_data(sql, (speechiness,))

    def select_by_track_popularity(self, track_popularity):
        if track_popularity is None or track_popularity == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_popularity = ?'
        return self.select_data(sql, (track_popularity,))
    
    def select_by_track_href(self, track_href):
        if track_href is None or track_href.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_href = ?'
        return self.select_data(sql, (track_href,))

    def select_by_uri(self, uri):
        if uri is None or uri.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE uri = ?'
        return self.select_data(sql, (uri,))

    def select_by_analysis_url(self, analysis_url):
        if analysis_url is None or analysis_url.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE analysis_url = ?'
        return self.select_data(sql, (analysis_url,))

    def select_by_track_album_name(self, track_album_name):
        if track_album_name is None or track_album_name.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_album_name LIKE ?'
        return self.select_data(sql, (f'%{track_album_name}%',))

    def select_by_track_name(self, track_name):
        if track_name is None or track_name.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_name LIKE ?'
        return self.select_data(sql, (f'%{track_name}%',))

    def select_by_playlist_name(self, playlist_name):
        if playlist_name is None or playlist_name.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE playlist_name LIKE ?'
        return self.select_data(sql, (f'%{playlist_name}%',))

    def select_by_track_id(self, track_id):
        if track_id is None or track_id.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_id = ?'
        return self.select_data(sql, (track_id,))

    def select_by_playlist_id(self, playlist_id):
        if playlist_id is None or playlist_id.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE playlist_id = ?'
        return self.select_data(sql, (playlist_id,))

    def select_by_track_album_id(self, track_album_id):
        if track_album_id is None or track_album_id.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_album_id = ?'
        return self.select_data(sql, (track_album_id,))

    def select_by_track_album_release_date(self, track_album_release_date):
        if track_album_release_date is None or track_album_release_date.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE track_album_release_date = ?'
        return self.select_data(sql, (track_album_release_date,))

    def select_by_instrumentalness(self, instrumentalness):
        if instrumentalness is None or instrumentalness == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE instrumentalness = ?'
        return self.select_data(sql, (instrumentalness,))

    def select_by_playlist_genre(self, playlist_genre):
        if playlist_genre is None or playlist_genre.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE playlist_genre LIKE ?'
        return self.select_data(sql, (f'%{playlist_genre}%',))

    def select_by_playlist_subgenre(self, playlist_subgenre):
        if playlist_subgenre is None or playlist_subgenre.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE playlist_subgenre LIKE ?'
        return self.select_data(sql, (f'%{playlist_subgenre}%',))

    def select_by_mode(self, mode):
        if mode is None or mode == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE mode = ?'
        return self.select_data(sql, (mode,))
    
    def select_by_key(self, key):
        if key is None or key == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE key = ?'
        return self.select_data(sql, (key,))

    def select_by_duration_ms(self, duration_ms):
        if duration_ms is None or duration_ms == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE duration_ms = ?'
        return self.select_data(sql, (duration_ms,))
    
    def select_by_type(self, type_value):
        if type_value is None or type_value.strip() == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE type = ?'
        return self.select_data(sql, (type_value,))

    def select_by_acousticness(self, acousticness):
        if acousticness is None or acousticness == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE acousticness = ?'
        return self.select_data(sql, (acousticness,))

    def select_by_id(self, id_value):
        if id_value is None or id_value == "":
            return ["Nothing found. Try again."]
        sql = 'SELECT * FROM spotify_data WHERE id = ?'
        return self.select_data(sql, (id_value,))
    
    def get_top_tracks(self):
        sql = 'SELECT * FROM spotify_data ORDER BY track_popularity DESC LIMIT 10'
        return self.select_data(sql)
    
    def get_top_artists(self):
        sql = '''SELECT track_artist, AVG(track_popularity) as avg_popularity, COUNT(*) as track_count 
                 FROM spotify_data 
                 GROUP BY track_artist 
                 ORDER BY avg_popularity DESC 
                 LIMIT 10'''
        conn = sqlite3.connect(self.database)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return [{"name": row[0], "count": round(row[1], 2)} for row in results]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return [{"name": "Error", "count": 0}]
        finally:
            conn.close()


# Создаем экземпляр менеджера базы данных
db_manager = DB_Manager(DATABASE)

# Функции форматирования
def format_track_info(track_data):
    """
    Форматирует информацию о треке в читаемый вид
    """
    if not track_data:
        return "No results found."
    
    if isinstance(track_data, list) and len(track_data) > 0 and isinstance(track_data[0], str):
        return track_data[0]
    
    formatted_results = []
    
    for i, track in enumerate(track_data[:10]):  # Показываем максимум 10 результатов
        try:
            formatted_track = f"""🎵 **{track[18]}** by {track[8]}
📀 Album: {track[14]}
📅 Release: {track[19]}
🎯 Popularity: {track[11]}/100
🎼 Genre: {track[4]} ({track[26]})
⏱️ Duration: {format_duration(track[24])}
⚡ Energy: {track[1]} | 🕺 Danceability: {track[3]}
🎶 Tempo: {track[2]} BPM | 🔊 Loudness: {track[5]} dB
───────────────────────────

"""
            formatted_results.append(formatted_track)
        except (IndexError, TypeError):
            formatted_results.append(f"Track {i+1}: Data formatting error\n")
    
    if len(track_data) > 10:
        formatted_results.append(f"... и еще {len(track_data) - 10} результатов")
    
    return "".join(formatted_results)

def format_duration(ms):
    """
    Конвертирует миллисекунды в формат MM:SS
    """
    try:
        seconds = int(ms) // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"
    except:
        return "Unknown"

def format_short_track_info(track_data):
    """
    Короткий формат для больших списков
    """
    if not track_data:
        return "No results found."
    
    if isinstance(track_data, list) and len(track_data) > 0 and isinstance(track_data[0], str):
        return track_data[0]
    
    formatted_results = []
    
    for i, track in enumerate(track_data[:15]):  # Показываем максимум 15 результатов
        try:
            formatted_track = f"{i+1}. 🎵 **{track[18]}** - {track[8]} (Popularity: {track[11]})\n"
            formatted_results.append(formatted_track)
        except (IndexError, TypeError):
            formatted_results.append(f"{i+1}. Track data error\n")
    
    if len(track_data) > 15:
        formatted_results.append(f"... и еще {len(track_data) - 15} результатов")
    
    return "".join(formatted_results)

# Функции-обертки с форматированием
def select_by_energy(energy):
    result = db_manager.select_by_energy(energy)
    return format_track_info(result)

def select_by_tempo(tempo):
    result = db_manager.select_by_tempo(tempo)
    return format_track_info(result)

def select_by_danceability(danceability):
    result = db_manager.select_by_danceability(danceability)
    return format_track_info(result)

def select_by_playlist_genre(playlist_genre):
    result = db_manager.select_by_playlist_genre(playlist_genre)
    return format_track_info(result)

def select_by_loudness(loudness):
    result = db_manager.select_by_loudness(loudness)
    return format_track_info(result)

def select_by_liveness(liveness):
    result = db_manager.select_by_liveness(liveness)
    return format_track_info(result)

def select_by_valence(valence):
    result = db_manager.select_by_valence(valence)
    return format_track_info(result)

def select_by_track_artist(track_artist):
    result = db_manager.select_by_track_artist(track_artist)
    return format_track_info(result)

def select_by_time_signature(time_signature):
    result = db_manager.select_by_time_signature(time_signature)
    return format_track_info(result)

def select_by_speechiness(speechiness):
    result = db_manager.select_by_speechiness(speechiness)
    return format_track_info(result)

def select_by_track_popularity(track_popularity):
    result = db_manager.select_by_track_popularity(track_popularity)
    return format_short_track_info(result)

def select_by_track_href(track_href):
    result = db_manager.select_by_track_href(track_href)
    return format_track_info(result)

def select_by_uri(uri):
    result = db_manager.select_by_uri(uri)
    return format_track_info(result)

def select_by_track_album_name(track_album_name):
    result = db_manager.select_by_track_album_name(track_album_name)
    return format_track_info(result)

def select_by_playlist_name(playlist_name):
    result = db_manager.select_by_playlist_name(playlist_name)
    return format_track_info(result)

def select_by_analysis_url(analysis_url):
    result = db_manager.select_by_analysis_url(analysis_url)
    return format_track_info(result)

def select_by_track_id(track_id):
    result = db_manager.select_by_track_id(track_id)
    return format_track_info(result)

def select_by_track_name(track_name):
    result = db_manager.select_by_track_name(track_name)
    return format_track_info(result)

def select_by_track_album_release_date(track_album_release_date):
    result = db_manager.select_by_track_album_release_date(track_album_release_date)
    return format_track_info(result)

def select_by_instrumentalness(instrumentalness):
    result = db_manager.select_by_instrumentalness(instrumentalness)
    return format_track_info(result)

def select_by_track_album_id(track_album_id):
    result = db_manager.select_by_track_album_id(track_album_id)
    return format_track_info(result)

def select_by_mode(mode):
    result = db_manager.select_by_mode(mode)
    return format_track_info(result)

def select_by_key(key):
    result = db_manager.select_by_key(key)
    return format_track_info(result)

def select_by_duration_ms(duration_ms):
    result = db_manager.select_by_duration_ms(duration_ms)
    return format_track_info(result)

def select_by_acousticness(acousticness):
    result = db_manager.select_by_acousticness(acousticness)
    return format_track_info(result)

def select_by_id(id_value):
    result = db_manager.select_by_id(id_value)
    return format_track_info(result)

def select_by_playlist_subgenre(playlist_subgenre):
    result = db_manager.select_by_playlist_subgenre(playlist_subgenre)
    return format_track_info(result)

def select_by_type(type_value):
    result = db_manager.select_by_type(type_value)
    return format_track_info(result)

def select_by_playlist_id(playlist_id):
    result = db_manager.select_by_playlist_id(playlist_id)
    return format_track_info(result)

def get_top_tracks():
    result = db_manager.get_top_tracks()
    return format_short_track_info(result)

def get_top_artists():
    result = db_manager.get_top_artists()
    if not result:
        return "No artists found."
    
    if isinstance(result[0], dict):
        formatted_results = []
        for i, artist in enumerate(result[:10], 1):
            formatted_results.append(f"{i}. 🎤 **{artist['name']}** (Avg Rating: {artist['count']}/100)\n")
        return "🏆 **TOP ARTISTS:**\n\n" + "".join(formatted_results)
    return str(result)


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()
    print("Database tables created successfully!")