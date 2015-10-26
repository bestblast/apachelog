__author__ = 'artem'

import re
import mysql.connector

DB_HOST = "127.0.0.1"
# DB_BASE = "db_log"
# DB_USER = "db_log_user"
# DB_PASS = "db_log_pass"
DB_BASE = "apachelog"
DB_USER = "root"
DB_PASS = "root"

file_log = "./files/portal.log"

# line = '185.46.89.10 - - [26/Oct/2015:20:10:17 +0200] "GET / HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"'
# line = '185.46.88.1 - - [26/Oct/2015:20:10:18 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8"'
# line = '213.160.140.67 - - [26/Oct/2015:20:10:49 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "-"'
# line = '213.160.140.67 - - [26/Oct/2015:20:10:51 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "-"'
# line = '185.46.88.1 - - [26/Oct/2015:20:10:53 +0200] "GET / HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"'
# line = '185.46.89.10 - - [26/Oct/2015:20:10:55 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8"'
# line = '185.46.88.1 - - [26/Oct/2015:20:11:18 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8"'
# line = '185.46.89.10 - - [26/Oct/2015:20:11:19 +0200] "GET / HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"'
# # line = '185.46.88.1 - - [26/Oct/2015:20:11:54 +0200] "GET / HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"'
# line = '185.46.89.10 - - [26/Oct/2015:20:11:56 +0200] "GET /news/show HTTP/1.0" 200 6627 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8"'
# #
# # line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
# regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.*?) "(.*?)" "(.*?)"'
#
# print re.match(regex, line).groups()
#
# with open(file_log) as f:
# for line in f:
# print "INSERT INTO table" . re.match(regex, line).groups()
# # if 'str' in line:
# #     break
#



import apachelog, sys

# Format copied and pasted from Apache conf - use raw string + single quotes

cnx = mysql.connector.connect(user=DB_USER, database=DB_BASE, host=DB_HOST, password=DB_PASS)
cursor = cnx.cursor()
db_insert_line = ("INSERT INTO httpd"
                  "(`l`,`status`,`host`,`user_agent`,`b`,`referer`,`u`,`time`,`request`)"
                  "VALUES (%(%l)s, %(%>s)s, INET_ATON(%(%h)s), %(%{User-Agent}i)s, %(%b)s, \
                  %(%{Referer}i)s, %(%u)s, %(%t)s, %(%r)s)")

format = r'%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"'

p = apachelog.parser(format)
for line in open(file_log):
    try:
        data = p.parse(line)
       # print data
    except:
        sys.stderr.write("Unable to parse %s" % line)
    cursor.execute(db_insert_line, data)
cnx.commit()