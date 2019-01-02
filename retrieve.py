
import time
import sys

import argparse

import requests
from requests.auth import HTTPBasicAuth

import browsercookie

def main(args):
    cookie = None
    if args.cookie_from.strip() != "":
        cookie = eval("browsercookie.{}()".format(args.cookie_from))

    url_file = open(args.file, 'r')

    for url in url_file:
        url = url.strip()
        if url.strip() == "":
            continue
        print(url)
        auth = None
        if args.user != "":
            auth = HTTPBasicAuth(args.user, args.password)
        r = requests.get(url, cookies=cookie, verify=False, auth=auth)
        if r.status_code != 200:
            print('failed with {}'.format(r.status_code))
        else:
            with open(args.saveto+"/"+url.split("/")[-1].strip(), 'wb') as f:
                f.write(r.content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-user', default="", type=str)
    parser.add_argument('-password', default="", type=str)
    parser.add_argument("-cookie-from", default="", type=str)
    parser.add_argument('file', type=str)
    parser.add_argument('saveto', type=str)

    args = parser.parse_args()

    main(args)

