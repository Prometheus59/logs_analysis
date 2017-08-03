## Views that need to be created

CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log
WHERE status LIKE '%404%'
GROUP BY date(time)
ORDER BY date(time);

CREATE VIEW full_view AS
SELECT date(time), COUNT(*) AS views
FROM log
GROUP BY date(time)
ORDER BY date(time);

CREATE VIEW error_percentage AS
SELECT full_view.date, (100.0*error_view.errors/full_view.views) AS rate
FROM full_view, error_view
WHERE full_view.date = error_view.date
ORDER BY full_view.date;
