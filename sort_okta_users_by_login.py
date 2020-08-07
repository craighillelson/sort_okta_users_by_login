"""
Open 'OktaPasswordHealth.csv' and sort users by last login in descending order.
"""

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

with open("OktaPasswordHealth.csv") as f:
    F_CSV = csv.reader(f)
    HEADERS = [re.sub('[^a-zA-Z_]', '_', h) for h in next(F_CSV)]
    ROW = namedtuple('ROW', HEADERS)
    for r in F_CSV:
        row = ROW(*r)
        USERS[datetime.strptime(row.Last_Login,
                                "%Y-%m-%d %H:%M:%S.%f")] = row.Login

print(RTN())

for last_login, login in sorted(USERS.items(), reverse=True):
    print(last_login, login)

file_name = "users_sorted_by_last_login.csv"

with open(file_name, "w") as out_file:
    OUT_CSV = csv.writer(out_file)
    OUT_CSV.writerow(OUT_HEADERS)
    for last_login, login in sorted(USERS.items(), reverse=True):
        keys_values = (login, last_login)
        OUT_CSV.writerow(keys_values)

print(f"\n{file_name} exported successfully\n")
