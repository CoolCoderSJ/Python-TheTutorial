from time import sleep
import sys
import os
from replit import db
from termcolor import colored
import time
time_between_letters = 0.05

##############################################################
#TIME DELAY CODE Block
#for x in string:
#    print(x, end='')
#    sys.stdout.flush()
#    sleep(time_between_letters)
##############################################################
def lvltransfunc():
  global time_between_letters
  lvltrans = "\n\nALL RIGHT!\nGive yourself a pat on the back for finishing this level.\n\n\n"
  for x in lvltrans:
      print(x, end='')
      sys.stdout.flush()
      sleep(time_between_letters)

def hello_tryfunc(logUsername):  
  global time_between_letters 
  hello_try = input("\nAll right, now it's time for you to try! Enter the print command with hello world.\nAs a note, please use single quotes, NOT double quotes.\nEnter --\n\n")
  hello_try.lower()
  if hello_try == "print('hello world')" or hello_try == "print('Hello world')" or hello_try == "print('Hello World')":
    lvltransfunc()
    db[logUsername + "_location"] = 2
    level2(logUsername)
  else:
    hello_fail = "Uh oh\n\n that didn't work =( \nLet's try again."
    for x in hello_fail:
      print(x, end='')
      sys.stdout.flush()
      sleep(time_between_letters)
    hello_tryfunc(logUsername)


def level1(logUsername):
  global time_between_letters
  db[logUsername + "_location"] = 1
  begin = "\nIT IS TIME!\n TIME FOR YOU TO LEARN ONE OF THE GREATEST LANGUAGES.\n\n"
  for x in begin:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  Hello_1 = "A Hello World program is the first program all developers do in a language. Let's learn the Python Syntax.\n\n The first thing to note is that there are no semicolons unlike other languages. The 'Print' Statement prints a line of code into the console/shell (Usually on Terminal, Command Prompt, Repl.it, etc its called the console, but on the Python IDLE its called the shell). Here's the line of code for Hello World -- \n\n"
  for x in Hello_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("print('Hello World') \n\n", "yellow"))
  Hello_2 = "print is a default python function, with the parameter of eithr a string, integer, float, variable, function, math equation, etc. The 'Hello World' is ou string. DO NOT ADD A SEMICOLON.\n\n"
  for x in Hello_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  hello_tryfunc(logUsername)


def level2(logUsername):
  global time_between_letters
  types_1 = "\nThis is more of an info level.\n\n There are 3 types of python values, a String() , int() , and float() string is a string, int is an integer, and float is integers+decimals.\n\n\n\n"
  for x in types_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  lvltransfunc()
  db[logUsername + '_location'] = 3
  level3(logUsername)

def vartryfunc(logUsername):
  global time_between_letters
  vartry = input("\nWe want the variable 'py1' to equal the string, 'hullo' . Please use single quotes. Define it below \n\n")
  if vartry == "py1='hullo'" or vartry == "py1 = 'hullo'" or vartry == "py1= 'hullo'" or vartry == "py1 ='hullo'":
    lvltransfunc()
    db[logUsername + "_location"] = 4
    level4(logUsername)
  else:
    varfail = "\nWhoopy daisy \n Try that again, remember to write the variable, an equal sign, then the value.\n"
    for x in varfail:
      print(x, end='')
      sys.stdout.flush()
      sleep(time_between_letters)
    vartryfunc(logUsername)

def level3(logUsername):
  global time_between_letters
  types_1 = "I BELEIVE\nthat it is now time for you to learn variables.\nYes, the important variables.\nPython is super simple.\nTo define variables, you need neither 'let' nor 'var'. Simply write the 'equation'. \nExample --\n\ntest_var = 'wow' \n\n Variables can equal integers, floats, strings, other integers, math equations, etc. A variable is case sensitive.\nNow you try\n\n"
  for x in types_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  vartryfunc(logUsername)

def cond_tryfunc(logUsername):
  global time_between_letters
  cond_nowutry = """\n\nNow you try!\nWe have the variable "num" already defined,\n\n"""
  for x in cond_nowutry:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("num = 5+5", "yellow"))
  cond_utry2 = """We want the console to print "ok" if num == 10.\nType out the if statement here. Use 4 spaces in place of the tab on Line 2\nDue to application errors, for new lines, type a |  right after the first line, and pretend all space after that is a new line."""
  for x in cond_utry2:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  cond_try = input(colored("Enter--\n\n", "yellow"))
  if cond_try == """if num == 10:|    print("ok")""" or cond_try == """if num == 10:|    print('ok')""":
    lvltransfunc(logUsername)
    db[logUsername + "_location"] = 5
    #level5()
  else:
    print("Uh oh! PythonTutorBot thinks that's wrong. =(\n(If you think this is a mistake, please ping @CoolCoderSJ on te official Repl Talk Post.\n\n")
    cond_tryfunc(logUsername)
    


def level4(logUsername):
  global time_between_letters
  cond_1 = """CONDITIONALS.\nConditionals are an important part of coding. Condtitionals may include things like  if/else    statements. An example of an if statement\n\n"""
  for x in cond_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("""if user_input == "hi":\n    print('big hi')""", "yellow"))
  cond_2 = """\n\nThe syntax:\nthere are no () or {}. Define your if statement clearly, and use a colon + new line to define the action. If using a variable/int/float, type out the variable/int/float freely. If using a string, type out the word with "" around the word. In the above example, user_input was a variable.\n\nElif\nIf you want to define another possibility, after the first if definition, type elif ---- \n\n Example --\n\n"""
  for x in cond_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("""if user_input == "hi":\n    print('big hi')\nelif user_input == "no":\n    print("yes") """, "yellow"))
  cond_3 = """\n\nAlways remember to define using double equal signs ==  \nYou can have an unlimited number of if and elif statements.\nElse\nThere can only be one else statement per conditional. Else is like a wildcard, it handles the remaining possibilities. Else usually goes at the bottom, and has no parameters. Example --\n\n"""
  for x in cond_3:
      print(x, end='')
      sys.stdout.flush()
      sleep(time_between_letters)
  print(colored("""if user_input == "hi":\n    print('big hi')\nelif user_input == "no":\n    print("yes")\nelse:\n    print("Hello, I'm Tutorial Bot") """, "yellow"))
  cond_tryfunc(logUsername)


def usrinpututryfunc(logUsername):
  usrinpututry = input("\n\nNow it's time for you to try out the input method! Please keep the variable as    usrinput     . You may put whatever question you want!\n\n")
  if usrinpututry.startswith("usrinput=input") or usrinpututry.startswith("usrinput =input") or usrinpututry.startswith("usrinput= input") or usrinpututry.startswith("usrinput = input"):
    print("""\n\nWhoa..\n""")
    lvltransfunc()
    db[logUsername + "_location"] = 6
    #level6()
  else:
    print("\n\nWhoopy daisy.\nTry that again.\n\n")
    usrinpututryfunc(logUsername)


def level5(logUsername):
  global time_between_letters
  usrinput1 = """Ever wonder how PythonTutorialBot takes in your answers and reads them?\nIn this lesson, we're going to learn about user inputs. By the end of this lesson, you will be able to take user input, and use it for various things.\nLET US BEGIN\n\nSyntax: An input statement is much like a print statement, only this time, instead of print, type input at the beginning. Example -\n\n"""
  for x in usrinput1:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("""input("What's your favorite color?  ")""", "yellow"))
  usrinput2 = """\n\nWhile this syntax is correct, currently, it does nothing. To make this work, assign it to a variable.\n\n"""
  for x in usrinput2:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  print(colored("""fav_color = input("What's your favorite color?  ")""", "yellow"))
  usrinput3 = """\n\nNow, we can check the variable fav_color's value  to do certain functions. (You can use usr inputs with conditionals now!!) Treat it like a normal variable. Remember to always add hypens, colons, spaces, etc. To differentiatw the question and answer. The input will come in the console/shell."""
  for x in usrinput3:
    print(x, end='')
    sys.stdout.flush()
    sleep(time_between_letters)
  usrinpututryfunc(logUsername)


def begin(logUsername):
  db[logUsername + "_location"] = 1
  global time_between_letters
  credits = "All credits for this tutorial go to CoolCoderSJ/Shuchir Jain. Let's begin!\n"

  for x in credits:
      print(x, end='')
      sys.stdout.flush()
      sleep(0.05)


  time_between_letters = float(input("\nPlease enter the time you want to have between each letter being printed (IN SECONDS) (The speed used above was 0.05, as in a 0.05 second delay): \n\n"))
  level1(logUsername)




while True:
  time.sleep(2)
  print("\033c")
  print(colored("Please make an account to save your progress. (Passwords can only be accessed by you). Otherwise, choose to manually pick your starting point. (helpful if you want to go back, since accounts don't let you go backwards)\n\n", "green"))
  print(colored("[1]New Account", "blue"))
  print(colored("[2]Log In", "blue"))
  print(colored("[3]Delete your account (NOT REVERSIBLE)", "blue"))
  print(colored("[4]Pick a Level Manually", "blue"))
  action = input()
  time.sleep(0.5)
  if(action == "1"):
    print("\033c")
    username = input(colored("What is your username: ", "blue"))
    time.sleep(0.5)
    password = input(colored("What password do you want to save: ", "blue"))
    if username in db:
      print(colored("Account already exists.", "red"))
      time.sleep(1)
      print("\033c")
    else:
      db[username] = password
      print(colored("Great! Your username is "+username+" and your password is "+password+" Don't worry, only you can access these passwords and usernames, and all data is encrypted. You're going to be redirected to the main page now, Login with your new credentials to gt started.", "green"))
      time.sleep(1)
      print("\033c")
  elif(action == "2"):
    print("\033c")
    logUsername = str(input(colored("Enter your username: ", "yellow")))
    time.sleep(0.5)
    userValue = str(input(colored("Enter your password: ", "yellow")))
    if logUsername in db:
      if userValue == db[logUsername]:
        print("Logged In! Now redirecting you to te last place you left off...")
        if logUsername + "_location" in db:
          if db[logUsername + "_location"] == 1:
            level1(logUsername)
          elif db[logUsername + "_location"] == 2:
            level2(logUsername)
          elif db[logUsername + "_location"] == 3:
            level3(logUsername)
          elif db[logUsername + "_location"] == 4:
            level4(logUsername)
          elif db[logUsername + "_location"] == 5:
            level5(logUsername)
        elif logUsername+"_location" not in db:
          db[logUsername + "_location"] = 0
          begin(logUsername)
      else:
        print("Uh oh wrong password")
        time.sleep(1)
        print("\033c")
    else:
      print("Not a valid user.")
      time.sleep(1)
      print("\033c")


  elif action == "3":
    print("\033c")
    user = input(colored("What is your username? ", "yellow"))
    passw = input(colored("What is your password? ", "yellow"))
    if user in db:
      if db[user] == passw:
        confirmdel = input(colored("WARNING!\nTHIS ACTION IS NOT REVERSIBLE. ALL DATA ASSOCIATED WITH THIS ACCOUNT WILL BE DELETED PERMANENTLY. DO YOU WISH TO CONTINUE? y/n: ", "red"))
        if confirmdel == "y":
          del db[user]
          del db[user + "_location"]
          print(colored("Account successfully deleted.", "red"))
          time.sleep(1)
          print("\033c")
        else:
          print(colored("Account deletion cancelled.", "green"))
          time.sleep(1)
          print("\033c")
      else:
        print(colored("INCORRECT PASSWORD", "red"))
        time.sleep(1)
        print("\033c")
    else:
      print(colored("Not a valid user.", "red"))
      time.sleep(1)
      print("\033c")


  elif action == "4":
    print("\033c")
    logUsername = str(input(colored("Enter your username: ", "yellow")))
    time.sleep(0.5)
    userValue = str(input(colored("Enter your password: ", "yellow")))
    if userValue == db[logUsername]:
      print("Manuel Level  Picker\n\n")
      manlvl = int(input("[1]Level 1\n[2]Level 2\n[3]Level 3\n[4]Level 4\n[5]Level 5\n"))
      if manlvl == 1:
        level1(logUsername)
      elif manlvl == 2:
        level2(logUsername)
      elif manlvl == 3:
        level3(logUsername)
      elif manlvl == 4:
        level4(logUsername)
      elif manlvl == 5:
        level5(logUsername)
      else:
        print("Invalid Level")
        time.sleep(1)
        print("\033c")
  else:
    print(colored("Invalid Choice", "red"))
    time.sleep(1)
    print("\033c")
  