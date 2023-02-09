import os
import random
import shutil

r"""
Założyć folder pod adresem C:\Users\barte\PycharmProjects\LearningPython, stworzyć plik tekstowy z napisem "test". Usunąć plik. Usunąć folder
"""

path = r'C:\Users\barte\PycharmProjects\LearningPython'
print(path)
os.chdir(path)
print(f"Jestem w folderze: {os.path.abspath(os.curdir)}")
print(f"Zawartość tego folderu: {os.listdir(path)}")


if os.path.exists("test"):
    print("Folder już istnieje")
    os.chdir(path)
    shutil.rmtree("test")
    print("folder usuinęto")
else:
    os.mkdir("test")

if os.path.exists("test"):
    os.chdir("test")
    f = open("test.txt", "w+")
    letters = "qwertyuiopasdfghjklzxcvbnm"
    letters_list = list(letters)
    letters_list.sort()
   # print(letters_list)
    for char in enumerate(letters_list):
        f.write(f"{char}")
        f.write("\n")
    # generowanie losowego słowa
    word = []
    word_length = random.randint(4, 10)
    print("zakres:", word_length)
    for x in range(0, word_length):
        word.append(letters_list[random.randint(0, len(letters_list)-1)])
    print("".join(word))
    f.write("".join(word))
