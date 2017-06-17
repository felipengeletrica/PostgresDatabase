#!/usr/bin/env python
#-*- coding: latin-1 -*-

import sys,os
import signal
import binascii
import time
import datetime

from postgres import postgres


def getmac(serial):


    LSB = ":%0.2X" % ((serial >> 0) & 0xff)
    MIDLE = ":%0.2X" % ((serial >> 8) & 0xff)
    MSB = ":%0.2X" % ((serial >> 16) & 0xff)

    MAC = "1C:65:9D:"
    MAC += MSB + MIDLE + LSB

    return MAC


if __name__ == "__main__":

    #execute only if run as a script
    print "Init Database manager"

    #Instance class
    postgres_register = postgres('localhost', 'postgres', 'root', '653410')
    postgres_producao = postgres('localhost', 'producao', 'root', '653410')
    postgres_producao2 = postgres('localhost', 'producao', 'root', '653410')

    postgres_register.connect()
    postgres_producao.connect()
    postgres_producao2.connect()

    a = 0

    MAC = ""

    while True:

        try:


            time.sleep(0.1)

            Consult = postgres_producao.query("SELECT * FROM tb_macs order by timestamp desc LIMIT 15;")
            print '\n\n' + str(datetime.datetime.now())

            for cont in Consult:
                print str(cont)

            ########################################################
            a += 1
            MAC = getmac(a)

            username = "FELIPE.ALBRECHT"

            Query = "INSERT INTO tb_macs (mac, serialnumber, username) " \
                    "VALUES('" \
                    + MAC + "','" \
                    + str(a) + "','" \
                    + username + "') " \
                    "RETURNING id;"
            Lastindex = postgres_producao.insert(Query)
            Lastindex2 = postgres_register.insert(Query)

            a += 1
            MAC = getmac(a)

            username = "FELIPE.VARGAS"

            Query = "INSERT INTO tb_macs (mac, serialnumber, username) " \
                    "VALUES('" \
                    + MAC + "','" \
                    + str(a) + "','" \
                    + username + "') " \
                    "RETURNING id;"

            Lastindex3 = postgres_producao2.insert(Query)

            print "Fake MAC: " + MAC

            print "Index of insertion 1                 : " + str(Lastindex)
            print "Index of insertion 1.1 - concorencie : " + str(Lastindex3)

            print "Index of insertion 2                 : " + str(Lastindex2)

        except Exception as error:

            postgres_register.connect()
            postgres_producao.connect()
            postgres_producao2.connect()
            print "Mas bah tchê! erro de banco Error" + str(error)