import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    Takes a json song file and inserts records into the song table and artist table.
    
    Keyword arguements:
    cur -- cursor used to insert files into psycopg tables
    filepath -- file path for the json file
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    cols = ['song_id', 'title', 'artist_id', 'year', 'duration']
    df['year'] = df['year'].astype(int)
    df['duration'] = df['duration'].astype(float)
    song_data = df[cols].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    cols = ['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']
    artist_data = df[cols].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Loads a json file for a session and inserts the record into the time, user, and songplay tables.
    
    Keyword arguements:
    cur -- cursor used to insert files into psycopg tables
    filepath -- file path for the json file
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')
    
    # insert time data records
    time_data = (t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    cols = ['userId', 'firstName', 'lastName', 'gender', 'level']
    user_df = df[cols]
    #user_df = user_df[user_df['userId'] != '']

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Gets all the files to be processed by the process_song_file and process_log_file functions.
    
    Keyword arguements:
    cur -- cursor used to insert files into psycopg tables
    conn -- connection to psycopg2
    filepath -- file path for the json file
    func -- function previously defined for processing log and song files
    
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()