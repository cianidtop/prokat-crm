import pygal
import psycopg2
from pygal.style import Style
from datetime import date, time
import time


def last_client():
    con = psycopg2.connect(database="prokat",
                              user="cianid",
                              password="Fam13051998",
                              host="localhost",
                              port="5432")

    cur = con.cursor()

    query = f"""select phone_number, first_name, last_name from client_client cc
                order by start_time desc
                limit 1"""

    cur.execute(query)
    rows = cur.fetchall()

    # rows = [(date(2020,6,1), 1233), (date(2020,7,1), 231)]

    row = rows[0]

    return row
