# modules/xml.py
import xml.etree.ElementTree as eTree


def xml_parse(string: str) -> list:
    levelsData = []
    tree = eTree.fromstring(string)
    levels = tree.find('./dict').find('./d').findall('./d')

    for level in levels:
        level_dict = {}
        levelName = levelString = ''
        has_k88 = False
        i = 0

        for key in level.findall('./k'):
            if key.text == 'k88':
                has_k88 = True

        for s in level.findall('./s'):
            if has_k88:
                if i == 1:
                    levelName = s.text
                elif i == 2:
                    levelString = s.text
            else:
                if i == 0:
                    levelName = s.text
                elif i == 1:
                    levelString = s.text

            i += 1

        level_dict['levelName'] = levelName
        level_dict['levelString'] = levelString
        levelsData.append(level_dict)

    return levelsData


def xml_parse_level(string: str) -> str:
    tree = eTree.fromstring(string)
    level = tree.findall('./s')

    return level[2].text
