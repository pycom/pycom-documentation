import os
import sys
# import urllib.request
import os.path
import mistune
import xml.etree.ElementTree as ET
from lxml import etree
from io import StringIO
from shutil import copyfile
import re

weights = { '': 10 } # per level weight in toc
prev_ident = ""
SUMMARY="content/SUMMARY.md"
KEY_SEP="@"
SRC_URL = '/' # 'https://development.pycom.io/'

def _list_content():
    import glob
    from pathlib import Path
    return [f for f in Path('content').glob('**/*.md')] + [f for f in Path('content').glob('**/*.html')]

def _parse_file(filename):
    text = ""
    with open(filename) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           line = _parse_line(filename, fp.readline())
           cnt += 1
           text += line
    return text

def _make_index(src):
    dst = './content/' + '/'.join(src.split('/')[:-1]) + '/_index.md'
    src = './content/' + src
    #  print('# copy:', src , '-->' ,dst)
    try:
        copyfile(src, dst)
    except Exception as e:
        print('# ', e)


def _make_key(url):
    if url.endswith('README.md') or url.endswith('introduction.md'):
        _make_index(url)
        return KEY_SEP.join(url.split('/')[:-1])
    else:
        return KEY_SEP.join(url.split("/")).replace(".md","")


def _make_parent(key, level):
    return KEY_SEP.join(key.split(KEY_SEP)[-2 - level:-1])

w = 10
prev_level = 1

def _traverse(root, nodes, last_h2):
        global weights
        weight = 10
        parent = root

        for node in nodes:
            # w = w + 10
            if node.text:
                if node.attrib.has_key('href'):
                    url = node.attrib['href']
                    key = _make_key(url)
                    name = root.text + '>' + node.text
                    name = node.text
                    if node.text == "Introduction":
                        name = last_h2
                    else:
                        name = node.text
                        # last_h2=node.text

                    parent = _make_parent(key, _traverse.level)
                    # print(etree.tostring(root, pretty_print=True).decode())

                    weight_key = parent
                    if weight_key in weights:
                        weights[weight_key] = weights[weight_key] + 10
                    else:
                        weights[weight_key] = 10
                    url =SRC_URL + url.replace('introduction.md', '/').replace('README.md', '/').replace('.md', '/')
                    # print('#', traverse.level * ' ',weights[weight_key] , '>',key,  node.text)
                    # print('#', traverse.level * ' ',weights[traverse.level] , traverse.level, root.text, '>', node.text,'[', url,']')
                    print(_write_toc(key, name, url, parent, weights[weight_key]))

                else:
                    if node.tag == 'h2':
                        w= 0
                        last_h2 = node.text
                        print('# ***', last_h2)

            _traverse.level += 1


            _traverse(parent, list(node), last_h2)
            # weights[traverse.level]= 10
            if node.text:
                parent = node
            _traverse.level -= 1


def _write_toc(key, name, url, parent, weight):
    toc =""
    toc += "[[menu.main]]\n"
    toc += "    name = \"%s\"\n" % name.replace("\\","") # remove escapes
    toc += "    url = \"%s\"\n" % url
    toc += "    identifier = \"%s\"\n" % key
    if parent:
        toc += "    parent = \"%s\"\n" % parent
    toc += "    weight = %s\n" % weight
    return toc

def _override_file(f, text):
    file = open(f,"w")
    file.write(text)
    file.close()

def _parse_line(f, line):

    if "{% page-ref " in line:
        # {% page-ref page="development/wipy2.md" %}
        #    -->
        #     {{< refname "development/wipy2.md" >}}
        line = line.replace("{% page-ref page=", "{{% refname ")
        line = line.replace("%}", "%}}")

    if "{% hint" in line:
        line = line.replace("{%", "{{%")
        line = line.replace("%}", "%}}")

    if "endhint" in line:
        # {% endhint %} --> {{% /hint %}}
        line = line.replace("endhint", "/hint")
        line = line.replace("{%", "{{<")
        line = line.replace("%}", ">}}")

    if ".md)" in line:
        line = line.replace(".md)", ")")

    return line

def _find_title(filename):
    with open(SUMMARY) as fp:
       line = fp.readline()
       cnt = 1
       print(filename)
       while line:
           # filename was a python3 POSIXFile object
           filename = str(filename).replace("_index.md", "README.md")

           if str(filename)[8:].replace('.md','') in line:
                # result is beetween []
                result = re.search('\[(.*)\]', line)
                if result is not None:
                    return result.group(1).replace("\\","")
           line = fp.readline()
    print("title not found for", filename)

    return ""


# def _find_title(filename):
#     with open(SUMMARY) as fp:
#        line = fp.readline()
#        cnt = 1
#        while line:
#            if line.startswith('#'):
#                print(filename, line)
#                return line.replace('#', '').strip()
#            line = fp.readline()
#     print("title not found for", filename)
#     # sys.exit(1)
#     return ""

def _remove_front_matters(file_path):
    file = open(file_path, "r")
    line = file.readline()
    # check if first line contains '---'
    if not line.startswith("---"):
        print("no front matter in file")
        return
    i = 0
    line = ""
    # skip until next '---'
    while not line.startswith('---'):
        line = file.readline()
        i = i + 1
    # recopy content
    output_path = '%s.output' % file_path
    with open(output_path, 'wb') as out_file:
        out_file.write(line.encode())
        while line:
            line = file.readline()
            out_file.write(line.encode())
    # move to original filemame
    os.rename(output_path, file_path)

def _make_front_matters(title, urls):
    fm =""
    fm+= "---\n"
    fm += "title: \"%s\"\n" % title.replace("\\","") # remove escapes if any
    #
    fm += "aliases:\n"
    for url in urls:
        fm += "    - %s\n" % url
    fm += "---\n"
    print(fm)
    return fm

import json
def _write_front_matters(file_path, title, urls):
    # remove possible existing front matters tags
    _remove_front_matters(file_path)
    # load the gitbook redirects.json
    # open a tmp file
    output_path = '%s.output' % file_path
    with open(output_path, 'wb') as out_file:
        # write the front matter tags in blank file
        out_file.write(_make_front_matters(title, urls).encode())
        # recopy the rest of the file
        with open(file_path, 'r') as in_file:
            out_file.write(in_file.read().encode())
    # delete tmp file and place new one
    os.rename(output_path, file_path)


# callable public methods

def load_sumary():
    markdown = mistune.Markdown()
    f = open(SUMMARY)
    parser = etree.HTMLParser()
    tree =  etree.parse(StringIO(markdown(f.read())), parser)
    uls = tree.xpath("//body/*")
    _traverse.level = 1
    _traverse(tree.xpath("//body/*")[0], uls,'')
    return tree

def parse_files():
    text = ""
    for f in _list_content():
        text = _parse_file(f)
        _override_file(f, text)

def _make_urls(file_path, redirects):
    urls = []
    if not (str(file_path).endswith("_index.md") or str(file_path).endswith("README.md")):
        urls.append(str(file_path)[8:].replace(".md", ".html"))
        urls.append(str(file_path)[8:])
    for r in redirects['redirects']:
        if 'to' in r:
            r['to'] = r['to'].replace(".html", "") #[2:]
            r['to'] = r['to'].replace(".html", "")
            file_path = str(file_path).replace(".md", "") #[8:]

            if r['to'][2:] == file_path[8:]:
                print("compare %s %s" % (r['to'], file_path))
                urls.append(r["from"])
    return urls

def write_all_front_matters():
    with open("redirects.json", "r") as read_file:
        redirects = json.load(read_file)
    for f in _list_content():
        urls = _make_urls(f, redirects)
        title = _find_title(f)
        _write_front_matters(f, title, urls)



load_sumary()
parse_files()
write_all_front_matters()

# ({{% ref page="../dashboard.md" %}})
# {% content "fifth" %}
# {% content "first" %}
# {% content "forth" %}
# {% content "second" %}
# {% content "third" %}
# {% endhint %}
# {% endtabs %}
# {% hint style="danger" %}
# {% hint style="info" %}
# {% hint style="warning" %}
# {% page-ref page="../../pymakr/installation/atom.md" %}
# {% tabs first="Exp Board 2.0", second="Exp Board 3.0" %}
# {% tabs first="Exp Board 2.0", second="Exp Board 3.0", third="Pytrack/Pysense/Pyscan", forth="USB UART Adapter", fifth="WiFi" %}
# {% tabs first="Exp Board 2.0", second="Exp Board 3.0", third="Pytrack/Pysense/Pyscan", fourth="USB UART Adapter", fifth="WiFi" %}
# {% tabs first="Exp Board 2.0", second="Exp Board 3.0", third="Pytrack/Pysense/Pyscan", fourth="USB UART Adapter", fifth="Wifi" %}
# {{% /hint %}}
# {{% hint style="info" %}}
