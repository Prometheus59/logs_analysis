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

# first create this view
    """CREATE VIEW error_view AS
    SELECT date(time), COUNT(*) AS errors
    FROM log
    WHERE status LIKE '%404%'
    GROUP BY date(time)
    ORDER BY date(time);"""

"""CREATE VIEW full_view AS
SELECT date(time), COUNT(*) AS views
FROM log
GROUP BY date(time)
ORDER BY date(time) """

"""CREATE VIEW error_percentage AS
SELECT full_view.date, (100.0*error_view.errors/full_view.views) AS rate
FROM full_view, error_view
WHERE full_view.date = error_view.date
ORDER BY full_view.date; """

query3 = """SELECT *
    FROM error_percentage
    WHERE error_percentage.rate > 1
    ORDER BY error_percentage.rate DESC; """
"

Analysis(query2)
