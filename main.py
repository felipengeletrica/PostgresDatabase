#!/usr/bin/env python
#-*- coding: latin-1 -*-

import sys,os
import signal
import binascii
import time
import datetime

from postgres import postgres



if __name__ == "__main__":

    #execute only if run as a script
    print "Init Database manager"

    #Instance class
    postgres_producao = postgres('localhost', 'test', 'root', 'root')
    postgres_producao2 = postgres('localhost', 'test2', 'root', 'root')

    postgres_producao.connect()
    postgres_producao2.connect()
   
    while True:

        try:
            time.sleep(0.1)

        except Exception as error:

            postgres_register.connect()
            postgres_producao.connect()
            postgres_producao2.connect()
            print "Mas bah tchê! erro de banco Error" + str(error)
