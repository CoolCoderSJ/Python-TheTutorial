## Lesson 0, INTRO TO IDEs

Welcome, welcome! This is a bonus lesson, Level0! In this lesson, we're going to talk about IDEs, or Integrated Development Environments. An IDE is where you type your code, possibly install packages, run the code, and manage your files, all in one.
Here's the list of Software we're going to talk about today -
- Sublime Text
- Repl.it
- Notepad++
- TextEdit
- Atom

Let's begin!

___

#### SUBLIME TEXT
Features-
Numerous themes

Package Control, install packages within the IDE

Multiple language Syntax highlighting

Run your code

Cons -

Can be finicky

The Git Support is a bit...weird

___

#### REPL.IT (RECOMMENDED IDE) 
Features -

Github support

Package Manager

Run your code

Free web hosting

Share porjects easily

Save your code with an account

Friendly community

Free easy to use Database

50+ languages

Syntax highlighting for all of them

Live error Linting (Finds errors live)

Debugger

Multiplayer support

Version control

___

#### Notepad++ and TextEdit
NO

DO NOT USE THESE FOR CODING. This is called a text editor, and are the worst things to use for coding because they don't support anything. at all.

___

#### Atom - 
Its made by Github, so deep Git support

looks pretty cool

Cons - 

Cant run code in it.

___

Thats all, I hope this helped you decide which IDE is best for you!

___

## Lesson 1, Hello World!
A Hello World program is the first program all developers do in a language. Let's learn the Python Syntax.

The first thing to note is that there are no semicolons. The `print` Statement prints a line of code into the console/shell (Usually on Terminal, Command Prompt, Repl.it, etc its called the console, but on the Python IDLE its called the shell). Here's the line of code for Hello World -- 

```python
print("Hello world!")
```
`print` is a default python function, with the parameter of eithr a string, integer, float, variable, function, math equation, etc. The 'Hello World' is our string. DO NOT ADD A SEMICOLON.


___

## Lesson 2, Data Types (Mini Lesson)
There are 3 types of python values, a string() , int() , and float() string is a string, int is an integer, and float is integers+decimals

___

## Lesson 3, Variables
I BELEIVE

that it is now time for you to learn variables.

Yes, the important variables.

Python is super simple.\nTo define variables, you need neither `let` nor `var`. Simply write the 'equation'. 

Example --

```python
test_var = 'wow' 
```

Variables can equal integers, floats, strings, other integers, math equations, etc. A variable is case sensitive.

____

## Lesson 4, Conitionals
CONDITIONALS.

Conditionals are an important part of coding. Condtitionals may include things like `if/else` statements. An example of an if statement - 

```python
if user_input == "hi":
  print('big hi')
```

The syntax:\nthere are no () or {}. Define your if statement clearly, and use a colon + new line to define the action. If using a variable/int/float, type out the variable/int/float freely. If using a string, type out the word with "" around the word. In the above example, user_input was a variable.

Elif

If you want to define another possibility, after the first if definition, type elif ---- 

Example --
```python
if user_input == "hi":
  print('big hi')
elif user_input == "no":
  print("yes") 
```

Always remember to define using double equal signs ==  

You can have an unlimited number of if and elif statements.

Else

There can only be one else statement per conditional. Else is like a wildcard, it handles the remaining possibilities. Else usually goes at the bottom, and has no parameters. Example --

```python
if user_input == "hi":
  print('big hi')
elif user_input == "no":
  print("yes")
else:
  print("Hello, I'm Tutorial Bot") 
```

## Lesson 5, User Input
Ever wonder how PythonTutorialBot takes in your answers and reads them?

In this lesson, we're going to learn about user inputs. By the end of this lesson, you will be able to take user input, and use it for various things.

LET US BEGIN

Syntax: An input statement is much like a print statement, only this time, instead of print, type input at the beginning. Example -


```python
input("What's your favorite color?  ")
```

While this syntax is correct, currently, it does nothing. To make this work, assign it to a variable.

```python
fav_color = input("What's your favorite color?  ")
```

Now, we can check the variable `fav_color`'s value  to do certain functions. (You can use usr inputs with conditionals now!!) Treat it like a normal variable. Remember to always add hypens, colons, spaces, etc. at the end of your question to differentiate the question and answer. The input will come in the console/shell, and you will answer by typing there.

___

Level 6, Lists
Lists can store LOTS of things. They store practically everything, even other lists! (These are called 2D lists, you'll learn about them later.)

LET US BEGIN

Syntax: A list is enclosed with brackets, and its value is stored as a variable. Example -

```python
my_list = ["item1", "item2", "item3"]
```
Here, we define a variable, with lots of things inside of it.

Now, if we just print this, we will get this -

```
[item1,tem2,item3]
```

To get an individual value, we have to call it. To call it, we type the variable name, then the location in brackets. \nNOTE: In lists, the first value is 0, not 1. If you call by location 1, you'll get the second value. Heres how to call a value --

```python
list_value_1 = my_list[0]
print(list_value_1)

#or

print(my_list[0])
```
