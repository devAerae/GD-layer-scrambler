# main.py
from modules.crypto import encode_level, decode_level
from modules.xml import xml_parse_level
import glob
import random


def main():
    levels = glob.glob('./levels/*.gmd')

    if not levels:
        print("There's no .gmd file(s) in /levels")
        exit()

    for i in range(len(levels)):
        print("{0}. {1}".format(i + 1, levels[i].split('\\')[-1]))

    lvl = int(input("맵을 번호로 선택해주세요: ")) - 1
    group_id = int(input("그룹 아이디를 입력해주세요: "))
    with open(levels[lvl], 'r') as f:
        data = f.readlines()
        level = ''.join(data)
        level_data = xml_parse_level(level)
        object_string = decode_level(level_data, False).split(';')[1:-1]
        str_objs = ""
        for i in object_string:
            obj = {}
            lst = i.split(',')

            # 리스트 -> 오브젝트
            for j in range(0, len(lst), 2):
                key = str(lst[j])  # Key
                value = lst[j + 1]  # Value
                obj[key] = value

            # 특정 그룹 찾은 후 레이어 바꾸기
            if "57" in obj:
                groups = obj["57"].split('.')
                if f"{group_id}" in groups:
                    obj['20'] = "{0}".format(random.randint(10000000, 99999999))
                    groups.remove(f"{group_id}")
                    obj['57'] = "{0}".format('.'.join(groups))
                    if len(groups) == 0:
                        del obj["57"]
            else:
                temp_list = []
                keys = list(obj.keys())
                values = list(obj.values())
                for k in range(len(keys)):
                    temp_list.append(keys[k])
                    temp_list.append(values[k])
                str_objs += ','.join(temp_list) + ";"

            # 오브젝트 -> 리스트 -> 스트링
            temp_list = []
            keys = list(obj.keys())
            values = list(obj.values())
            for k in range(len(keys)):
                temp_list.append(keys[k])
                temp_list.append(values[k])
            str_objs += ','.join(temp_list) + ";"

        gzipped_objs = encode_level(str_objs, False)
        level = level.replace(level_data, gzipped_objs)

        with open(levels[lvl][0:-4] + " new.gmd", 'w') as ff:
            ff.write(level)


if __name__ == '__main__':
    main()
