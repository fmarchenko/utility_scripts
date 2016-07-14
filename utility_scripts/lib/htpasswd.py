#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Jul 12, 2016"

from sys import argv
from random import choice
from string import ascii_letters, digits
from getpass import getpass
from crypt import crypt

if __name__=="__main__":
        name = argv[1:2]
        if not name:
                print("Введите имя пользователя:")
                name = raw_input()
                if not name:
                        print("ОШИБКА: Введите имя пользователя.")
                        exit(1)
        else:
                name = name[0]

        salt = ''.join(choice(ascii_letters.join(digits)) for char in range(2))

        passwd = getpass(b"Введите пароль: ")
        if not passwd == getpass(b"Введите пароль еще раз: "):
                print("ОШИБКА: Пароль и подтверждение не совпадают.")
                exit(2)

        passwdHash = crypt(passwd, salt)

        print(name + ':' + passwdHash)

        exit(0)
