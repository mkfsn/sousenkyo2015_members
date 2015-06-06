#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = 'Jun 05, 2015 '
__author__ = 'mkfsn'


import os
import sys
import requests
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("sousenkyo2015_members")


def download(group, team, num):
    url = (
        "http://cdn.akb48.co.jp/cache/image/?path="
        "sousenkyo2015_members/%s_%s.png"
    )
    filename = "data/%s_%s_%d.png" % (group, team, num)
    if os.path.isfile(filename):
        return 0

    target = url % (team, num)
    r = requests.get(target)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return r.status_code
    else:
        return r.status_code


def main():
    groups = {
        'AKB': {
            'A': 17,
            'K': 16,
            'B': 14,
            '4': 17,
            '8': 46
        },
        'SKE': {
            'S': 15,
            'K2': 17,
            'E': 17,
            'SK': 16 # No 10
        },
        'NMB': {
            'N': 16,
            'M': 18,
            'B2': 17
        },
        'HKT': {
            'H': 20,
            'K4': 18,
            'HK': 7
        }
    }

    for group, teams in groups.items():
        for team, num in teams.items():
            logger.debug("Fectcing %s Team%s ..." % (group, team))
            if num == 1:
                fail = 0
                while fail <= 3:
                    r = download(group, team, num)
                    if r not in [0, 200]:
                        msg = "[%d] %s - Team%s : %d" % (r, group, team, num)
                        logger.debug(msg)
                        fail += 1
                    else:
                        fail = 0
                    num += 1
            else:
                for i in range(1, num + 1):
                    download(group, team, i)


if __name__ == '__main__':
    main()
