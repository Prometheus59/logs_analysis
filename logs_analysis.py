import psycopg2


# Analysis Function
def Analysis(query):
    dbname = "news"
    database = psycopg2.connect(database=dbname)
    c = database.cursor()
    c.execute(query)
    rows = c.fetchall()
    print rows
    database.close()


# Most Popular articles, DESCending order
query1 = """SELECT title, COUNT(*) AS count
FROM articles, log
WHERE log.path LIKE concat('%', articles.slug)
GROUP BY articles.title
ORDER BY count DESC
LIMIT 3"""

# Most Popular article authors
query2 = """SELECT authors.name, COUNT(articles.author) AS count
        FROM articles,
        log, authors WHERE
        log.path = concat('/article/',articles.slug)
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY count DESC"""

# Days WHERE more than 1% of requests led to errors

query3 = """SELECT *
    FROM error_percentage
    WHERE error_percentage.rate > 1
    ORDER BY error_percentage.rate DESC; """


Analysis(query1)
Analysis(query2)
Analysis(query3)
