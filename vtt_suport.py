import os
import re
from cy_translation import tranlate


def get_file(filepath):
    lines = []
    with open(filepath, encoding='utf-8') as file:
        lines = file.readlines()

    items = []
    item = None

    for line in lines:
        line = line.replace('\n', '')
        match = re.match(r'^\d*$', line)
        if match and match.end() > 0:
            if item:
                items.append(item)
            print(item)
            item = {"line_number": line, "content": ""}
            continue

        match = re.match(r'^\d{2}:\d{2}', line)
        if match and match.start() == 0 and match.end() > 0 and item:
            item["time"] = line
            continue

        if line.strip() and item and 'line_number' in item:
            if item["content"]:
                line = " " + line
            item["content"] = item["content"] + line

    return items


def translation_new_file(filepath, trs):
    result = get_file(filepath)
    (path, f) = os.path.split(filepath)
    newfile = os.path.join(path, str(f).split(',')[0] + '_translation' + '.vtt')
    print(newfile)

    with open(newfile, mode='w', encoding='utf-8') as nf:
        nf.write('WEBVTT\n\n')
        transSources = []
        for res in result:
            transSources.append(res['content'])
        transTarget = trs(transSources)

        for index, res in enumerate(result):
            print(index)
            nf.write(res['line_number'])
            nf.write('\n')
            nf.write(res['time'])
            nf.write('\n')
            nf.write(res['content'])
            nf.write('\n')
            nf.write(transTarget[index])
            nf.write('\n')
            nf.write('\n')


def cy_translation(org_str):
    return '中文'


filepath = 'C:/Users/ljs/Videos/nand/1.vtt'
translation_new_file(filepath, tranlate)
