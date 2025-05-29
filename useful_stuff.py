import random

meters_in_kilometers = 1000
cats = ["Mochi", "Kenny", "Lotti"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)