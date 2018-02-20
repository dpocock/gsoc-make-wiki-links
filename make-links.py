#!/usr/bin/python
# -*- coding: latin-1 -*-

import csv
import datetime
import urllib
import sys

if __name__ == '__main__':
    body_file = open("message.txt", "rt")
    body = urllib.quote(body_file.read())
    body_file.close()
#    print body
    with open("topics.csv", "rb") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            messageID = urllib.quote(row[0])
            recipient = row[1]
            _cc = ""
            cc = row[2]
            if len(cc) > 0:
                _cc = "cc=%s&" % (cc,)
            subject = row[3]
            _subject = urllib.quote(subject)

            print subject
            print "mailto:%s?%sin-reply-to=%s&Subject=%s&Body=%s|click here, complete all details, make sure you are subscribed to the relevant mailing lists before posting" % (recipient, _cc, messageID, _subject, body)
            print ""

