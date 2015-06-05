#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = 'Jun 05, 2015 '
__author__ = 'mkfsn'


import os
import sys
import requests


def main():

    url = "http://cdn.akb48.co.jp/cache/image/?path=sousenkyo2015_members/%s_%s.png"
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
            'E': 17
        },
        'NMB': {
            'N': 16,
            'M': 18,
            'B2': 17
        },
        'HKT': {
            'H': 20,
            'K4': 18
        }
    }

    for group, teams in groups.items():
        for team, num in teams.items():
            print "Fectcing %s Team%s ..." % (group, team),
            sys.stdout.flush()
            for i in range(1, num + 1):
                target = url % (team, i)
                r = requests.get(target)
                if r.status_code == 200:
                    filename = "data/%s_%s_%d.png" % (group, team, i)
                    if os.path.isfile(filename):
                        continue
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(1024):
                            f.write(chunk)
                else:
                    break
            print "Done"


if __name__ == '__main__':
    main()
