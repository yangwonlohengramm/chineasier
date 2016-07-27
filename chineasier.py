import os.path
import datetime
import sys
import textwrap

def check_file():
    if not os.path.isfile("words.txt"):
        f = open("words.txt", "w")
        f.close()

def add(addline):
    if addline.count(" ") != 1:
        print(textwrap.fill("Whoops, it looks like your number of spaces\
 is not equal to one!", width=52))
        return
    elif len(addline.split()) != 2:
        print(textwrap.fill("Are you sure you spaced the words and pinyin\
 correctly?", width=52))
        return

    f = open("words.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("words.txt", "w")
    for line in lines:
        f.write(line)
    today = datetime.date.today()
    f.write(addline+" "+str(today)+" 0"+'\n') # format is 'wwpinyin yyyy-mm-dd rep#'
    f.close()

    print()
    print("----------------------------------------------------")
    print("{:^52}".format("Successfully added."))
    print("----------------------------------------------------")

def print_wordlist_without_pinyin_and_update_date():
    print("Your words to practice today:")
    f = open("words.txt", "r")
    empty = True
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        # date is the last review date, in format yyyy-mm-dd
        word, pinyin, date, repeat = line.split()
        year, month, day = map(int, date.split("-"))
        review_day = datetime.date(year, month, day)
        today = datetime.date.today()
        repeat = int(repeat)
        if today >= review_day + datetime.timedelta(days=fib[repeat]):
            if empty == True:
                print()
                empty = False
            print("   • " + word)
            lines[i] = word + " " + pinyin + " " + str(today) + " " + str(repeat+1) + "\n"
    f.close()

    if empty:
        print()
        print("    Looks like you don't have any practice today!")

    f = open("words.txt", "w")
    for line in lines:
        f.write(line) # should still have a '\n' no?
    f.close()

def print_with_pinyin():
    f = open("words.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        # date is the last review date, in format yyyy-mm-dd
        word, pinyin, date, repeat = line.split()
        year, month, day = map(int, date.split("-"))
        review_day = datetime.date(year, month, day)
        today = datetime.date.today()
        repeat = int(repeat)
        if today >= review_day + datetime.timedelta(days=fib[repeat]):
            print("   • " + word)
    f.close()

def opening_statements():
    print(textwrap.fill("Note: This program assumes you already practiced the day you enter a\
     word, and that you will practice the 2nd day, the 3rd, the 5th, et cetera.\
     So, days 0, 1, 2, 3, 5, 8, etc. However, as long as you don't open the\
     program on a given day, the words for that day will still be displayed\
     when you do open the program at a later date.", width=52))
    print()
    print("####################################################")
    print("# • Enter words and pinyin with a space in         #")
    print("# • between but only one space in total.           #")
    print("# • Enter 'p' or 'practice' for today's word list  #")
    print("# • Deletion is to be performed manually           #")
    print("# • Enter 'exit' to exit the program               #")
    print("####################################################")
    print()

def gen_fib():
    a = 1
    b = 1
    for i in range(100000):
        c = a+b
        fib.append(c)
        a = b
        b = c

# MAIN PROGRAM

fib = [1, 1]
gen_fib()

check_file()

opening_statements()

print_wordlist_without_pinyin_and_update_date()

while True:
    print()
    print(">>> ", end='')
    cmd = input()

    if cmd.lower() == "practice" or cmd.lower() == "p":
        print_with_pinyin()

    elif cmd == "exit":
        sys.exit(0)

    else:
        add(cmd)

        #print("Sorry master, your command was not recognized -desu~")
