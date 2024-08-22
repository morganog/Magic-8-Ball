# Morgan Anderson: @morganog GitHub Account

import random

# These are my responses I created in a separate file so that my code would
# be more clean

# They are sepeared by positive, neutral, and negative responses
# The last function called magicball_all() just conjoins them and picks a random response

# I also implemented a function called: replace_punct ! It will filter out all special characters. 
# I paired this with my main program code with ignore_punct.lower() to ignore capitals as well.

def magicball_pos():
    pos_resp = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes"
    ]
    return (pos_resp)

def magicalball_neut():

    neut_resp = [
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again"
    ]
    return (neut_resp)

def magicalball_neg():

    neg_resp = [
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]
    return (neg_resp)

def magicball_all():
    all_resp = [
        magicball_pos,
        magicalball_neut,
        magicalball_neg
    ]
    random_func = random.choice(all_resp)
    return random_func()

def replace_punct(text):
  ignore_punct = str.maketrans(" ", " ", "!,.?")
  return text.translate(ignore_punct)
