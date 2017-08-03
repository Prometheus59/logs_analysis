import psycopg2
# For problem 3
from datetime import date


# Analysis Function - Takes "query" as a parameter, executes the query, and
# returns the results


def analysis(query):
    dbname = "news"
    database = psycopg2.connect(database=dbname)
    c = database.cursor()
    c.execute(query)
    rows = c.fetchall()
    database.close()
    return rows


# Most Popular articles, descending order -- PROBLEM 1
def popular_articles():

    query = """ SELECT title, COUNT(*) AS count
                FROM articles, log
                WHERE log.path LIKE concat('%', articles.slug)
                GROUP BY articles.title
                ORDER BY count DESC
                LIMIT 3"""
    articles_popularity = analysis(query)

    # Printing results for problem 1
    print(" ")
    print("*** MOST POPULAR 3 ARTICLES OF ALL TIME ***")
    print(" ")

    for i in articles_popularity:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
        print(" ")


# Most Popular article authors -- PROBLEM 2

def popular_authors():

    query = """ SELECT authors.name, COUNT(articles.author) AS count
                FROM articles,
                log, authors WHERE
                log.path = concat('/article/',articles.slug)
                AND articles.author = authors.id
                GROUP BY authors.name
                ORDER BY count DESC"""
    author_popularity = analysis(query)

    # Printing results for problem 2
    print(" ")
    print("*** MOST POPULAR AUTHORS OF ALL TIME ***")
    print(" ")

    for i in author_popularity:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
        print(" ")


# Days WHERE more than 1% of requests led to errors -- PROBLEM 3
def more_errors():

    query = """ SELECT *
                FROM error_percentage
                WHERE error_percentage.rate > 1
                ORDER BY error_percentage.rate DESC; """
    most_errors = analysis(query)

    # Printing results for problem 3
    print(" ")
    print("*** DAYS WHERE MORE THAN " + "1% " + "OF REQUESTS LED TO ERRORS ***")
    print(" ")

    for i in most_errors:
        print(i[0].strftime('%B %d, %Y') +
              " -- " + str(round(i[1], 2)) + "%" + " errors")
        print(" ")


popular_articles()
popular_authors()
more_errors()
