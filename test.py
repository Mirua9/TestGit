#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet(sname, name):
    print (' '.join(('Hello',sname, name)))



def main():

    sname = str(input("Quel est votre prénom : "))
    name = str(input("Quel est votre nom : "))
    greet (sname,name)

if __name__ == "__main__":
    main()
