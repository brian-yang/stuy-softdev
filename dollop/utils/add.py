import sqlite3
from time import strftime

def add_new_story(title, creator, base_content):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    # get the max_id
    get_max_id = "SELECT MAX(story_id) from stories"
    cur_max_id = c.execute(get_max_id).fetchone()[0]
    if cur_max_id is None:
        story_id = 1
    else:
        story_id = cur_max_id + 1

    # add story to the next row
    add_story = "INSERT INTO stories (story_id, date, title, creator, base_content) VALUES(?, ?, ?, ?, ?)"
    c.execute(add_story, (story_id, get_time(), title, creator, base_content))

    # add story_id to list of story_ids in users table
    story_ids = "SELECT story_ids FROM users WHERE user=?"
    entry = c.execute(story_ids, (creator,)).fetchone()[0]
    if entry is None:
        id_list = str(story_id)
    else:
        id_list = str(entry) + "," + str(story_id)

    update_story_ids = "UPDATE users SET story_ids=? where user=?"
    c.execute(update_story_ids, (id_list, creator))

    c.close()

    db.commit()
    db.close()

def get_time():
    return strftime("%Y-%m-%d %H:%M:%S")

def store_updates(story_id, user, update):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    # add update
    add_update = "INSERT INTO story_updates (story_id, date, user, story_update) VALUES(?, ?, ?, ?)"
    c.execute(add_update, (story_id, get_time(), user, update))

    # add story_id to list of story_ids in users table
    story_ids = "SELECT story_ids FROM users WHERE user=?"
    entry = c.execute(story_ids, (user,)).fetchone()[0]
    if entry is None:
        id_list = str(story_id)
    else:
        id_list = str(entry) + "," + str(story_id)

    update_story_ids = "UPDATE users SET story_ids=? where user=?"
    c.execute(update_story_ids, (id_list, user))

    c.close()

    db.commit()
    db.close()

# def is_duplicate_story(title, creator):
#     f = "data/storyteller.db"
#     db = sqlite3.connect(f)
#     c = db.cursor()

#     check_duplicates = "SELECT story_id FROM stories WHERE title=? AND creator=?"
#     row = c.execute(check_duplicates, (title, creator)).fetchone()
#     if row is None:
#         is_duplicate = False
#     else:
#         is_duplicate = True

#     c.close()

#     db.commit()
#     db.close()

#     return is_duplicate
