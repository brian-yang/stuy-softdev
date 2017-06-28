import sqlite3
import sys

f = "../data/storyteller.db"

db = sqlite3.connect(f)
c = db.cursor()

def create_tables():
    create_users = "CREATE TABLE IF NOT EXISTS users (user STRING NOT NULL, password STRING NOT NULL, story_ids STRING);"
    c.execute(create_users)

    create_stories = "CREATE TABLE IF NOT EXISTS stories (story_id INTEGER NOT NULL, date STRING NOT NULL, title STRING NOT NULL, creator STRING NOT NULL, base_content STRING NOT NULL);"
    c.execute(create_stories)

    create_story_updates = "CREATE TABLE IF NOT EXISTS story_updates (story_id INTEGER NOT NULL, date STRING NOT NULL, user STRING NOT NULL, story_update STRING NOT NULL);"
    c.execute(create_story_updates)

def clear_tables():
    query = "DROP TABLE users;";
    c.execute(query);

    query = "DROP TABLE stories;";
    c.execute(query);

    query = "DROP TABLE story_updates;";
    c.execute(query);

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Format: python admin.py <0/1>"
    elif int(sys.argv[1]) == 0:
        print "Created tables!"
        create_tables()
    elif int(sys.argv[1]) == 1:
        print "Cleared tables!"
        clear_tables()

c.close()

db.commit()
db.close()
