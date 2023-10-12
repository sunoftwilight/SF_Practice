-- create
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

.mode csv
.import users.csv users

SELECT rowid, * FROM users;

-- users테이블에서 나이가 어린순으로, 나이가 같다면 잔고가 많은 순으로 정렬하여,
-- 이름, 나이, 잔고를 조회 및 출력하시오. 
SELECT
  first_name, age, balance
FROM
  users
ORDER BY
  age,
  balance DESC;



