# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user_"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay(songplay_id varchar, start_time date, user_id int, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_(user_id int, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song(song_id varchar, title varchar, artist_id varchar, year int, duration float)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist(artist_id varchar, name varchar, location varchar, latitude double precision, longitude double precision)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time date, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO user_(user_id, first_name , last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO song(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artist(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""SELECT song_id, A.artist_id FROM song A JOIN artist B ON A.artist_id=B.artist_id
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]