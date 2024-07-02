#!/bin/python3

import sys
import requests
import re

def scan_links(link):
    try:
        contents = requests.get(link).text

        regex = re.compile(r'(?i)\b((?:https?|ftp):\/\/(?:www\.)?[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|])')

        return regex.findall(contents)
    except:
        return ""

def scan_all(url, depth, itteration):
    if itteration == 0:
        print(f"┌ {url}")
    index = 0
    links = scan_links(url)

    for link in links:
        index += 1
        if index == len(links):
            if itteration < depth:
                print(f"{" "*itteration}└┌─ {"".join(link)}")
            else:
                print(f"{" "*itteration}└─ {"".join(link)}")
            #itteration += 1
        else:
            if itteration < depth:
                print(f"{" "*itteration}├┌─ {"".join(link)}")
            else:
                print(f"{" "*itteration}├─ {"".join(link)}")
        for i in range(depth):
            scan_all("".join(link),0, itteration+1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments given.")
        print("Type \"linkrecurse --help\".")
        exit(0)

    url = ""
    depth = 0
    get_id = 0
    help_ = 0

    for arg in sys.argv:
        if arg == "--url":
            get_id = 1
            continue
        if arg == "--depth":
            get_id = 2
            continue
        if arg == "--help":
            help_ = 1
            break
        if get_id == 1:
            url = arg
            get_id = 0
        if get_id == 2:
            depth = int(arg)
            get_id = 0
    if help_:
        print("Usage: linkrecurse --url \"[url]\" --depth [depth]")
        print("[url] is the full url of the webpage to be scanned.")
        print("[depth] is the recursion depth of scanning, 0 only shows the direct links on the page, 1 or more scans the links on the page recursivly.")
        exit(0)
    else:
        scan_all(url, depth, 0)
