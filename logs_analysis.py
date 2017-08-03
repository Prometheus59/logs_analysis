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


# Most Popular articles, descending order
query1 = """select title, count(*) AS count
from articles, log
where log.path like concat('%', articles.slug)
group by articles.title
order by count desc
LIMIT 3"""

# Most Popular article authors
query2 = """select authors.name, count(articles.author) AS count from articles,
        log, authors where
        log.path = concat('/article/',articles.slug)
        and articles.author = authors.id
        group by authors.name
        order by count desc"""

# Days where more than 1% of requests led to errors

# first create this view
    """CREATE VIEW error_view AS
    select date(time), count(*) AS errors
    from log
    where status like '%404%'
    group by date(time)
    ORDER by date(time);"""

"""CREATE VIEW full_view AS
select date(time), count(*) AS views
from log
group by date(time)
order by date(time) """

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
