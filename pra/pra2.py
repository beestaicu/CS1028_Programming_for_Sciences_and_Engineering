# -----------------------------------------------
# Practical 2 - CS1028
# -----------------------------------------------


# --------------------------------------------------
# You do not need a running Python environment to be able to answer the following questions.
# You should be able to do this from looking at the previous week’s lecture slides.
# For programming answers, you can either write a Python program, or you can write pseudocode.
# --------------------------------------------------------



# ---------------------------------------------------------
# 1. Compose a program that writes the Hello, World message five times
# Answers:
# for i in range(5):
#     print("Hello, World")
#     i += 1
# ------------------------------------------------
# 2. Tell us what happens if you miss the following in helloworld.py:
# a) import Answer: NameError: name 'stdio' is not defined
# b) stdio  Answer: SyntaxError: invalid syntax
# c) import stdio   Answer: NameError: name 'stdio' is not defined
# --------------------------------------------------
# 3. Tell us what happens if you misspell these:
# a) iport  Answer: SyntaxError: invalid syntax
# b) sdio   Answer: ModuleNotFoundError: No module named 'sdio'
#                   NameError: name 'sdio' is not defined
# c) wite   Answer: AttributeError: module 'stdio' has no attribute 'wite'
# d) witeln Answer: AttributeError: module 'stdio' has no attribute 'witeln'
# --------------------------------------------------
# 4. Tell us what happens if you miss these from helloworld.py:
# a) the first ‘    Answer: SyntaxError: EOL while scanning string literal
# b) the second ‘   Answer: SyntaxError: EOL while scanning string literal
# c) the stdio.writeln() statement  Answer: Not print anything
# --------------------------------------------------
# 5. Describe what happens if you try to execute useargument.py with each of the following:
# a) python useargument.py python   Answer: Hi, python. How are you?
# b) python useargument.py 1234 Answer: Hi, 1234. How are you?
# c) python useargument.py Bob  Answer: Hi, Bob. How are you?
# d) useargument.py Bob Answer: It will open the useargument.py file
# ---------------------------------------------------
# 6. Suppose that a and b are integers. What does the following sequence of statements
# do? Draw an object level trace of this computation.
# t = a
# b = t
# a = b
#########
# a = 1 #
# b = 2 #
# t = 1 #
# b = 1 #
# a = 1 #
#########
# ------------------------------------------
# 7. Suppose that a and b are booleans. Show that the expression:
# (not (a and b) and (a or b)) or ((a and b) or not (a or b))
# evaluates to True
# Answers:
# a=1   b=1 result=1
# a=0   b=0 result=1
# a=1   b=0 result=1
# a=0   b=1 result=1
# ------------------------------------------------
# 8. Simplify the following expression:
# (not (a < b) and not (a > b))
# Answer:
# a = b
# ---------------------------------------------------
# 9. What does stdio.writeln((1.0 + 2 + 3 + 4) / 4) write?
# Answer:   2.5
# ----------------------------------------------------
# 10. Suppose that a is 3.14159. What do each of these statements write?
# stdio.writeln(a)
# stdio.writeln(a + 1.0)
# stdio.writeln(8 // int(a))
# stdio.writeln(8.0 / a)
# stdio.writeln(int(8.0 / a))
# Explain each outcome
# Answers:
# on the text file:
# import stdio
# a = 3.14159
# stdio.writeln(a)
# stdio.writeln(a + 1.0)
# stdio.writeln(8 // int(a))
# stdio.writeln(8.0 / a)
# stdio.writeln(int(8.0 / a))
# on the terminal:
# 3.14159
# 4.14159
# 2
# 2.5464812403910124
# 2
# --------------------------------------------------------------



# ----------------------------------------------------------------
# Once you have completed Section 1, you should now be getting familiar with the basic concepts,
# and you will now be ready to create your Python programming environment.
# You will need this to be able to work on all the subsequent course materials.
# The first thing you will need to do is to get yourself a proper text editor,
# so that you can work on more than one file quickly, and in bulk, as required.
# The standard text editor is not up to this task.
# You cannot use a program like Word either.
# For Windows machines, a program such as Notepad ++,
# or Edit Pad Lite will allow you to open multiple web page files
# simultaneously in order to edit several at the same time. \
# A program such as Gedit or Geany for Linux based systems would be ideal for this task.
# ------------------------------------------------------------------------


