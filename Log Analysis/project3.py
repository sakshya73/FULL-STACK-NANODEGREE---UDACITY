#!/usr/bin/env python

import psycopg2

DBNAME = "NEWS"


def execut(query):
    # To connect to the database
    conn = psycopg2.connect(database=DBNAME)
    # To perform database operations
    curs = conn.cursor()
    # To execute the entered query
    curs.execute(query)
    # To fetch the result from the entered query
    result = curs.fetchall()
    # To close the connection with database
    conn.close()
    return result


# For more than 1 % error
def percentageError():
    query = """
        select totl.day,
        ((allErrors.firstError*100)/totl.secondError)as p
          from(
          select date_trunc('day', time) "day",
          count(*) as firstError
          from log
          where status
          like '404%'
          group by day) as allErrors
          join(
          select date_trunc('day',time) "day",
          count(*) as secondError
          from log
          group by day) as totl
          on totl.day =  allErrors.day
          where (
          ((allErrors.firstError*100)/totl.secondError)>1)
          order by p desc;
            """
    all_ = execut(query)
    print("\nDATE WITH MORE THAN 1 % ERROR:")
    for one in all_:
        d = one[0].strftime("%B %d, %Y")
        err = str(one[1])
        print(d + " had " + err + " % " + "errors.")


# For most popular author
def popularAuthor():
    query = """
        select authors.name,
        count(*) as count
        from
        authors join articles
        on
        authors.id = articles.author join log
        on log.path
        like concat('/article/%',articles.slug)
        group by authors.name
        order by count desc
        limit 3;
            """
    all_ = execut(query)
    i = 1
    print("\n MOST POPULAR AUTHORS ")
    for one in all_:
        num = str(i)
        title = one[0]
        view = str(one[1])
        print(num + ' . ' + title + '  =  ' + view + " views ")
        i += 1


# For most popular article
def popularArticle():
    query = """
        select articles.title,
        count(*) as count
        from
        articles join log
        on log.path
        like
        concat('/article/%',articles.slug)
        group by articles.title
        order by count desc
        limit 3;
            """
    all_ = execut(query)
    i = 1
    print(" MOST POPULAR ARTICLES ")
    for one in all_:
        num = str(i)
        title = one[0]
        view = str(one[1])
        print(num + ' . ' + title + "  =  " + view + " views ")
        i += 1

popularArticle()
popularAuthor()
percentageError()
