# main.py
from modules.crypto import encode_level, decode_level, encrypt_data, decrypt_data
from modules.xml import xml_parse_level
import os
import glob


def main():
    levels = glob.glob('./levels/*.gmd')

    if not levels:
        print("There's no .gmd file(s) in /levels")
        exit()

    for i in range(len(levels)):
        print("{0}. {1}".format(i + 1, levels[i]))

    lvl = int(input("맵을 번호로 선택해주세요: "))
    with open(levels[lvl]) as f:
        data = f.readlines()
        level = ''.join(data)
        level_data = xml_parse_level(level)
        object_string = decode_level(level_data, False).split(';')[1:-1]
        objects = []
        for i in object_string:
            obj = {}
            lst = i.split(',')
            for j in range(0, len(lst), 2):
                key = str(lst[j])  # Key
                value = lst[j + 1]  # Value
                obj[key] = value
            objects.append(obj)

