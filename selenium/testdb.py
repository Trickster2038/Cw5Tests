#!/usr/bin/env python
# coding: utf-8

import settings
import psycopg2

db = settings.DB

def connect(db):
    global conn
    conn = psycopg2.connect(dbname=db.name, user=db.user, 
                        password=db.password, host=db.host)
    conn.autocommit = True
    global cursor
    cursor = conn.cursor()
    return cursor
def fillFaculties(cur):
    cur.execute("INSERT into beta_facultiest values (0, 'ИУ', 11)")
    cur.execute("INSERT into beta_facultiest values (1, 'ФН', 14)")
    cur.execute("INSERT into beta_facultiest values (2, 'СГН', 11)")
    cur.execute("INSERT into beta_facultiest values (3, 'МТ', 11)")
    cur.execute("INSERT into beta_facultiest values (4, 'РЛ', 11)")
def mockDB(cur):
    # unfilled outgoing
    cur.execute("INSERT into beta_persont values (0, 'Unfilled', 'Фролов', 1, 2,    '0 биография lorem ipsum lorem ipsum lorem ipsum',    false, 0, 0, 'uname0', 2, 1, true, false)")
    
    # outgoing:
    cur.execute("INSERT into beta_persont values (1, 'Даниил', 'Иванов', 1, 2,    '1 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname1', 2, 1, false, false)")
    cur.execute("INSERT into beta_persont values (2, 'Михаил', 'Иванов', 1, 2,    '2 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname2', 2, 1, false, false)")
    
    #incoming
    cur.execute("INSERT into beta_persont values (3, 'Александр', 'Петров', 1, 2,    '3 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname3', 2, 1, false, false)")
    cur.execute("INSERT into beta_persont values (4, 'Анна', 'Петрова', 1, 2,    '4 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname4', 2, 1, true, false)")
    
    #friends safe
    cur.execute("INSERT into beta_persont values (5, 'Николай', 'Тихомиров', 1, 3,    '5 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname5', 2, 2, false, true)")
    cur.execute("INSERT into beta_persont values (6, 'Дмитрий', 'Тихомиров', 1, 3,    '6 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname6', 2, 2, true, true)")
    
    #friends unsafe
    cur.execute("INSERT into beta_persont values (7, 'Виола', 'Сидорова', 1, 4,    '7 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'uname7', 2, 1, false, true)")    
    
    cur.execute("INSERT into beta_persont values (421423205, 'Астахов', 'Сергей', 1, 2,    '8 биография lorem ipsum lorem ipsum lorem ipsum',    true, 0, 0, 'trickster2038', 2, 1, true, false)")
    cur.execute("INSERT into beta_friendst values (4, 421423205, 101, false)")
    cur.execute("INSERT into beta_friendst values (0, 421423205, 1, false)")
    cur.execute("INSERT into beta_friendst values (1, 421423205, 2, false)")
    cur.execute("INSERT into beta_friendst values (2, 3, 421423205, false)")
    cur.execute("INSERT into beta_friendst values (3, 4, 421423205, false)")

def init_test_db():
    cursor = connect(db)
    cursor.execute("truncate beta_persont")
    cursor.execute("truncate beta_friendst")
    cursor.execute("truncate beta_facultiest")
    mockDB(cursor)
    fillFaculties(cursor)




