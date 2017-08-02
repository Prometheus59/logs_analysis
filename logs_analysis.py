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
query1 ="""select title, count(*) as count from articles, log
where log.path like concat('%', articles.slug)
group by articles.title order by count desc limit 3"""

# Most Popular article authors
query2 = """select authors.name, count(articles.author) as count from articles,
        log, authors where
        log.path = concat('/article/',articles.slug)
        and articles.author = authors.id
        group by authors.name
        order by count desc"""

# Days where more than 1% of requests led to errors
query3 = ""

Analysis(query1)
