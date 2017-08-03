# Logs Analysis Project - Udacity Full Stack Nanodegree

This is an internal reporting tool that uses information from the database to discover what kind of articles the site's readers like.

## The assignment requires 3 questions to be answered:

1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which day(s) did more than 1% of requests lead to errors?

## Instructions

1. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from udacity
2. Clone this repository to your personal machine:
  `git clone https://github.com/Prometheus59/logs_analysis`
3. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
4. Install [Vagrant](https://www.vagrantup.com/)
5. Place logs_analysis.py & Udacity's database in the same directory as the VM
6. Start the virtual machine by entering the following in the terminal where
   the virtual machine is located:
   1. `vagrant up`
   2. `vagrant ssh`
7. Setup the database with the following command
` psql -d news -f newsdata.sql; `
8. Make the required views by entering the following into your terminal

### Views that are used in this project
- error_view

```
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log
WHERE status LIKE '%404%'
GROUP BY date(time)
ORDER BY date(time);
```

- full_view

```
CREATE VIEW full_view AS
SELECT date(time), COUNT(*) AS views
FROM log
GROUP BY date(time)
ORDER BY date(time);
```

- error_percentage

```
CREATE VIEW error_percentage AS
SELECT full_view.date, (100.0*error_view.errors/full_view.views) AS rate
FROM full_view, error_view
WHERE full_view.date = error_view.date
ORDER BY full_view.date;
```

9. Run the program by entering the following in the terminal:
` python logs_analysis.py `

## Example Output
```
*** MOST POPULAR 3 ARTICLES OF ALL TIME ***
"Candidate is jerk, alleges rival" -- 1693235 views
"Bears love berries, alleges bear" -- 1269005 views
"Bad things gone, say good people" -- 850490 views


*** MOST POPULAR AUTHORS OF ALL TIME ***
"Ursula La Multa" -- 12689850 views
"Rudolf von Treppenwitz" -- 10586425 views
"Anonymous Contributor" -- 4252450 views
"Markoff Chaney" -- 2113925 views


*** DAYS WHERE MORE THAN 1% OF REQUESTS LED TO ERRORS ***
July 17, 2016 -- 2.26% errors
```
