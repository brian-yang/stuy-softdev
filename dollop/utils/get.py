import sqlite3

def get_latest_update(story_id):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    latest_update = "SELECT story_update FROM story_updates WHERE story_id=? ORDER BY datetime(date) DESC"
    info = c.execute(latest_update, (story_id,)).fetchone()

    if info is None:
        get_story_info = "SELECT base_content FROM stories WHERE story_id=?"
        info = c.execute(get_story_info, (story_id,)).fetchone()

    c.close()

    db.commit()
    db.close()

    return info[0]

def get_contributed_stories(user):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    # get list of story_ids
    story_ids = "SELECT story_ids FROM users WHERE user=?"
    entry = c.execute(story_ids, (user,)).fetchone()[0]
    if entry is None:
        id_list = []
    else:
        id_list = str(entry).split(",")
        id_list = [int(sid) for sid in id_list]
        id_list.sort()

    # get info regarding each story as well as the base content
    data = []
    for sid in id_list:
        get_story_info = "SELECT title, creator, base_content FROM stories WHERE story_id=?"
        story_info = tuple([sid, c.execute(get_story_info, (str(sid),)).fetchone()])
        data.append(story_info)

    c.close()

    db.commit()
    db.close()

    # return data
    return data

def get_browse_stories(user):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    # get list of stories user has contributed to
    story_ids = "SELECT story_ids FROM users WHERE user=?"
    entry = c.execute(story_ids, (user,)).fetchone()[0]
    if entry is None:
        id_list = []
    else:
        id_list = str(entry).split(",")
        id_list = [int(sid) for sid in id_list]
        id_list.sort()

    # generate list containing all story ids
    get_max_id = "SELECT MAX(story_id) from stories"
    max_id = c.execute(get_max_id).fetchone()[0]
    if max_id is None:
        all_story_ids = []
    else:
        all_story_ids = [sid + 1 for sid in range(max_id)]

    # filter out the stories that the user has contributed to
    new_id_list = []

    for sid in all_story_ids:
        if sid not in id_list:
            new_id_list.append(sid)

    # get info regarding each story, including the latest update
    # if latest update not found, display the base content
    data = []
    for sid in new_id_list:
        get_latest_update = "SELECT story_update FROM story_updates WHERE story_id=? ORDER BY datetime(date) DESC"
        info = c.execute(get_latest_update, (str(sid),)).fetchone()
        if info is None:
            get_story_info = "SELECT base_content FROM stories WHERE story_id=?"
            info = c.execute(get_story_info, (str(sid),)).fetchone()
        latest_update = info[0]
        get_story_info = "SELECT title, creator FROM stories WHERE story_id=?"
        story_info = tuple([sid, c.execute(get_story_info, (str(sid),)).fetchone() + (latest_update,)])
        data.append(story_info)

    c.close()

    db.commit()
    db.close()

    # return data
    return data

def get_complete_story(story_id):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    get_base_content = "SELECT base_content FROM stories WHERE story_id=?"
    base_content = str(c.execute(get_base_content, (story_id,)).fetchone()[0])

    get_updates = "SELECT story_update FROM story_updates WHERE story_id=?"
    updates = c.execute(get_updates, (story_id,))

    for update in updates:
        base_content += str(update[0]) + "\n"

    c.close()

    db.commit()
    db.close()

    return base_content
