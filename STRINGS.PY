first_name="martin"
last_name="racheal"
# string concatination

print(first_name+"-"+last_name)

# =============================================STRING FORMATTING
husband="martin"
wife="racheal"
formatted="my name is {} and my wife is {}".format(husband,wife)
print(formatted)

# ========================================F-Strings (Python 3.6 and above):
name= "martin"
job="Dev."
formatt=f"my name is {job}{name}."
print(formatt)

#===============================================STRING INDEXING AND SLICING
text = "Python"
# Indexing
first_char = text[0]  # 'P'
second_char = text[1]  # 'y'
# Slicing
substring = text[1:4]  # 'yth'

#  ======================================= String Methods:===========
sentence = "Python programming is fun!"

# Length of the string
length = len(sentence)  # 27

# Convert to uppercase and lowercase
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()

# Count occurrences of a substring
count_python = sentence.count("Python")  # 1

# Find the index of a substring
index_is = sentence.find("is")  # 15

# Replace part of the string
new_sentence = sentence.replace("fun", "awesome")

# ===============================================================string operations========================
# Check if a substring is present
contains_python = "Python" in sentence  # True

# Concatenation
new_text = text + " is powerful!"

# Repetition
repeated_text = text * 3  # 'PythonPythonPython'
