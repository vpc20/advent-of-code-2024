import os
# import shutil
# from zipfile import ZipFile

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects\AdventOfCode2024\AdventOfCode2024'):
    for filename in filenames:
        if filename.startswith('aoc') and filename.endswith('test_data2.txt'):
            print(filename)
            new_filename = filename.replace('test_data2.txt', '_test_data2.txt')
            print(new_filename)
            # os.renamexxx(filename, new_filename)


# print('\nPython files copied to C:\\temp\\PycharmProjects')