""" __doc__ """

import csv
import re
from collections import namedtuple
from datetime import datetime

RTN = lambda: "\n"

USERS = {}
OUT_HEADERS = [
    "login",
    "last_login",
    ]

# open file, populate a dictionary with last login timestamp and login name
with open('OktaPasswordHealth.csv') as f:
    F_CSV = csv.reader(f)
    HEADERS = [re.sub('[^a-zA-Z_]', '_', h) for h in next(F_CSV)]
    ROW = namedtuple('ROW', HEADERS)
    for r in F_CSV:
        row = ROW(*r)
        USERS[datetime.strptime(row.Last_Login,
                                "%Y-%m-%d %H:%M:%S.%f")] = row.Login

print(RTN())

# output users sorted by last login
for last_login, login in sorted(USERS.items(), reverse=True):
    print(last_login, login)

# write users and last logins to csv
with open("users_sorted_by_last_login.csv", "w") as out_file:
    OUT_CSV = csv.writer(out_file)
    OUT_CSV.writerow(OUT_HEADERS)
    for last_login, login in USERS.items():
        keys_values = (login, last_login)
        OUT_CSV.writerow(keys_values)

print(RTN())

# update user
print("'users_sorted_by_last_login.csv' exported successfully")

print(RTN())
