-- create
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT
  first_name, country
FROM
  users
WHERE
  first_name='건우'
  AND country='경기도';


SELECT
  first_name, age, country
FROM
  users
WHERE
  country NOT IN ('경기도', '강원도')
  AND age BETWEEN 20 AND 30
ORDER BY
  age;
