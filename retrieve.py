
import time
import sys

import argparse

import requests
import browsercookie

def main(args):
    cookie = browsercookie.chrome()

    url_file = open(args.file, 'r')

    for url in url_file:
        if url.strip() == "":
            continue
        print(url)
        r = requests.get(url, cookies=cookie, verify=False)
        with open(args.saveto+"/"+url.split("/")[-1].strip(), 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    parser.add_argument('saveto', type=str)

    args = parser.parse_args()

    main(args)

