import psycopg2

# Most Popular articles, descending order

# Analysis Function


def Analysis(query):
    dbname = "news"
    database = psycopg2.connect(database=dbname)
    c = database.cursor()
    c.execute(query)
    rows = c.fetchall()
    print rows
    database.close()

query1 = "select title, count(ip) as count from articles, log group by title order by count desc limit 3 offset 1"

query2 = ""

query3 = ""

Analysis(query1)
