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
  first_name, phone, country
FROM
  users
WHERE
  country != '서울'
  AND phone LIKE '%-51__-%';
