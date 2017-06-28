import hashlib

def login_user(username, password):
    with open("data/accounts.csv", "r") as userDatabase:
        return ret_login_message(username, password, userDatabase)
        
def ret_login_message(username, password, userDatabase): 
    accounts = userDatabase.readlines()
    for account in accounts:
        accountInfo = account.strip().rsplit(",", 1)
        if accountInfo[0] == username:
            if accountInfo[1] == hashlib.sha256(password).hexdigest():
                return "Success!"
            else:
                return "Failed to login! Please check your password!"
    return "Failed to login! Username not in database."
    
def register_user(username, password):
    with open("data/accounts.csv", "a+rw") as userDatabase:
        return ret_register_message(username, password, userDatabase)
    
def ret_register_message(username, password, userDatabase):
    accounts = userDatabase.readlines()
    for account in accounts:
        accountInfo = account.rsplit(",", 1)
        if accountInfo[0] == username:
            return "Uh-oh! Looks like that username has been taken!"
    if (username == "" or password == ""):
        return "Username/password field is empty. Please enter a username and password!"
    userDatabase.write(username + "," + hashlib.sha256(password).hexdigest() + '\n')
    return "Registered!"
        
