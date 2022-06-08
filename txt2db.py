#!/usr/bin/env python

import os
from sys import argv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Methy.settings")

import django

if django.VERSION >= (1, 7):
    django.setup()


def main():
    from cohort.models import cohort
    #infile = 'D:/PhD_Project/Methy_Database/methSample/homelink/blood_age_sample.xls'
    infile = argv[1]
    d_key = []
    d = {}
    with open(infile, 'r') as f1:
        for line in f1:
            val = line.strip().split('\t')
            if val[0] == 'ID':
                d_key = val
            else:
                for i, k in enumerate(d_key):
                    d[k] = val[i]
                new_item = cohort()
                new_item.ids = d['ID']
                new_item.count = d['Samples']
                new_item.tissue = d['Tissues']
                new_item.annotation = d['Attributes']
                new_item.array = d['Array']
                new_item.note = d['Note']
                new_item.save()


if __name__ == "__main__":
    main()
    print('Done!')
