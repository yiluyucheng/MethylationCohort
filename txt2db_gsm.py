#!/usr/bin/env python

import os
from sys import argv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Methy.settings")

import django

if django.VERSION >= (1, 7):
    django.setup()


def main():
    from cohort.models import GsmInfo
    #infile = 'D:/PhD_Project/Methy_Database/methSample/homelink/blood_age_sample.xls'
    infile = argv[1]
    d_key = []
    d = {}
    with open(infile, 'r') as f1:
        for line in f1:
            val = line.strip().split('\t')
            if val[0] == 'Sample':
                d_key = val
            else:
                for i, k in enumerate(d_key):
                    d[k] = val[i]
                new_item = GsmInfo()
                new_item.ids = d['Sample']
                new_item.age = d['Age']
                new_item.gender = d['Gender']
                new_item.source_date = d['Date']
                new_item.race = d['Race']
                new_item.source = d['Source_name']
                new_item.group = d['Sample_group']
                new_item.disease = d['Disease_status']
                new_item.series = d['GSE_id']
                new_item.save()


if __name__ == "__main__":
    main()
    print('Done!')
