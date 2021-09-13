import pygal
import psycopg2
from pygal.style import Style
from datetime import date

def create_chart():
    con = psycopg2.connect(database="prokat",
                              user="cianid",
                              password="Fam13051998",
                              host="localhost",
                              port="5432")

    cur = con.cursor()

    query = f"""select start_time::date as s_date, sum(cena) from ride_ride
                group by s_date
                order by s_date """

    cur.execute(query)
    rows = cur.fetchall()

    # rows = [(date(2020,6,1), 1233), (date(2020,7,1), 231)]

    custom_style = Style(
      colors=('#FFCF46', '#421E47'))

    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "По дням"
    for i in rows:
        b_chart.add(str(i[0]), i[1])
    result = b_chart.render_data_uri()

    return result


def render_pie():
    con = psycopg2.connect(database="prokat",
                              user="cianid",
                              password="Fam13051998",
                              host="localhost",
                              port="5432")

    cur = con.cursor()

    query = f"""select place_from as s_date, sum(cena) from ride_ride
                group by s_date
                order by s_date """

    cur.execute(query)
    rows = cur.fetchall()
    # rows = [('Искра', 1233), ('Набережная', 231)]

    custom_style = Style(
        colors=('#FFCF46', '#421E47'))
    pie_chart = pygal.Pie(style=custom_style)
    pie_chart.title = 'По точкам'
    for i in rows:
        pie_chart.add(str(i[0]), i[1])

    result = pie_chart.render_data_uri()

    return result

def render_months():
    con = psycopg2.connect(database="prokat",
                           user="cianid",
                           password="Fam13051998",
                           host="localhost",
                           port="5432")

    cur = con.cursor()

    query = f"""select to_char(start_time, 'YYYY-MM') as months, sum(cena) from ride_ride
                group by months
                order by months"""

    cur.execute(query)
    rows = cur.fetchall()

    custom_style = Style(
        colors=('#FFCF46', '#421E47'))

    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "По месяцам"
    for i in rows:
        b_chart.add(str(i[0]), i[1])
    result = b_chart.render_data_uri()

    return result

def render_pie_tech():
    con = psycopg2.connect(database="prokat",
                              user="cianid",
                              password="Fam13051998",
                              host="localhost",
                              port="5432")

    cur = con.cursor()

    query = f"""SELECT tech, sum(cena) FROM public.ride_ride
                where to_char(now() , 'YYYY-MM') = to_char(start_time, 'YYYY-MM')
                group by tech"""

    cur.execute(query)
    rows = cur.fetchall()
    # rows = [('Искра', 1233), ('Набережная', 231)]

    pie_chart = pygal.Pie()
    pie_chart.title = 'По технике за месяц'
    for i in rows:
        pie_chart.add(str(i[0]), i[1])

    result = pie_chart.render_data_uri()

    return result



def create_cars_chart():
    con = psycopg2.connect(database="prokat",
                              user="cianid",
                              password="Fam13051998",
                              host="localhost",
                              port="5432")

    cur = con.cursor()

    query = f"""select start_time::date as s_date, sum(cena) from ride_ride
                where tech = 'Машинка'
                group by s_date
                order by s_date """

    cur.execute(query)
    rows = cur.fetchall()

    # rows = [(date(2020,6,1), 1233), (date(2020,7,1), 231)]

    custom_style = Style(
      colors=('#FFCF46', '#421E47'))

    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "По дням машинки"
    for i in rows:
        b_chart.add(str(i[0]), i[1])
    result = b_chart.render_data_uri()

    return result

def render_months_cars():
    con = psycopg2.connect(database="prokat",
                           user="cianid",
                           password="Fam13051998",
                           host="localhost",
                           port="5432")

    cur = con.cursor()

    query = f"""select to_char(start_time, 'YYYY-MM') as months, sum(cena) from ride_ride
                where tech = 'Машинка'
                group by months
                order by months"""

    cur.execute(query)
    rows = cur.fetchall()

    custom_style = Style(
        colors=('#FFCF46', '#421E47'))

    b_chart = pygal.Bar(style=custom_style)
    b_chart.title = "По месяцам машинки"
    for i in rows:
        b_chart.add(str(i[0]), i[1])
    result = b_chart.render_data_uri()

    return result
