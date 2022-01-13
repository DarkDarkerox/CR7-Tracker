from os import execlp, fspath
from sqlite3.dbapi2 import SQLITE_ANALYZE
import time
from datetime import datetime
import sqlite3
from instaloader import Instaloader, Profile, exceptions


def get_data(username):
  
    try:
        profile = Profile.from_username(loader.context, target_user)
    except exceptions.ProfileNotExistsException:
        print('This account does not exist.')
        exit()
        
    # Initialize my temp variables
    temp_followers = profile.followers
    temp_following = profile.followees

    # Get current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    print(f'Consulta realizada con exito a las {current_time}')
    return temp_followers, temp_following, current_time, current_date

    # print(f"""
    #   Cuenta: {username}
    #   Followers: {temp_followers}
    #   Following: {temp_following}
    #   Date: {current_date}
    #   Time: {current_time}
    #   """)
    
def create_table(user):
    query = f"""
    CREATE TABLE IF NOT EXISTS {user}_data(
	    "followers"	INTEGER NOT NULL,
	    "following"	INTEGER NOT NULL,
	    "date"	INTEGER NOT NULL,
	    "time"	INTEGER NOT NULL
    )
    """

    with sqlite3.connect('instadb.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, ())
        conn.commit()
    
    
if __name__ == '__main__':
    
    target_user = 'cristiano' 
    loader = Instaloader()

    while True:
        total_followers, total_following, ctime, cdate = get_data(target_user)    
        with sqlite3.connect('instadb.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(
                f"INSERT INTO {target_user}_data(followers, following, date, time) VALUES(?, ?, ?, ?)",
                (total_followers, total_following , cdate, ctime)
            )
            conn.commit()
        time.sleep(5)
        
    
    
    
    