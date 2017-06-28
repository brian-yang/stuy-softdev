#Olivia Gallager & Brian Yang
#Softdev HW 4/20

#With your table buddy:
#YOUR TASK The First:
#Write a function that uses list comprehension to return whether a password meets a minimum threshold: it contains a mixture of upper- and lowercase letters, and at least one number.

#YOUR TASK The Second:
#Write a function that uses list comprehension to return a password's strength rating. This function should return a low integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10)

#Consider these criteria:
# mixture of upper- and lower-case
# inclusion of numerals
# inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *
# submit this under pwchkr in the workshop

# ==============================
# TASK ONE
# ==============================
def min_satisfactory(pw):
    lowercase = [lower for lower in pw if ord(lower) >= 97 and ord(lower) <= 122]
    uppercase = [upper for upper in pw if ord(upper) >= 65 and ord(upper) <= 90]
    numbers = [num for num in pw if ord(num) >= 48 and ord(num) <= 57]

    return len(lowercase) > 0 and len(uppercase) > 0 and len(numbers) > 0

# ==============================
# TASK TWO
# ==============================
# Algo: add two to score if:
# upper
# lower
# numbers
# symbols
# length of password

def pwchkr(s):
    strength = 0
    lower = [ chr(index) for index in range(97,123)]
    upper = [ chr(index) for index in range(65,91)]
    num = [ chr(index) for index in range(48,58)]
    special = [ chr(index) for index in range(33,48)]
    special2 = [ chr(index) for index in range(58,65)]
    special.append(special2)

    score = 0

    #length
    if len(s) >= 8:
        score += 2

    l = [char for char in s]#list of characters

    has_upper = False
    has_lower = False
    has_numbers = False
    has_symbols = False
                
    for i in l:
        if i in lower and not has_lower:
            score += 2
            has_lower = True
        if i in upper and not has_upper:
            score += 2
            has_upper = True
        if i in num and not has_numbers:
            score += 2
            has_numbers = True
        if i in special and not has_symbols:
            score += 2
            has_symbols = True
    
    if has_lower and has_upper:
           score+=1
            
            
    return score
                        
# ==============================
# TESTING
# ==============================

# print pwchkr(" ")
# print pwchkr("12509813956134jk1tnjk G  q3gq34 g~!!@!#%@$^#@%@^@#$@#$%")
# print pwchkr("jktnjk1 qgq g~!!@!#%@$^#@%@^@#$@#$%")
