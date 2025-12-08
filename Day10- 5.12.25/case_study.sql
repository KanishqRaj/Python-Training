CREATE DATABASE subscription_app;
USE subscription_app;

CREATE TABLE subscriptions (
sub_id INT PRIMARY KEY,
customer_name VARCHAR(50),
start_date DATE,
expiry_date DATE,
created_at DATETIME,
plan_type VARCHAR(20) -- Monthly, Quarterly, Yearly
);

INSERT INTO subscriptions VALUES
(1, 'Aisha Khan', '2025-11-15', '2026-01-15', '2025-11-15 10:30:00', 'Monthly'),
(2, 'Rahul Sharma', '2025-12-03', '2026-02-05', '2025-12-03 09:45:00', 'Monthly'),
(3, 'Imran Ali', '2025-10-10', '2025-11-10', '2025-10-10 14:12:00', 'Monthly'),
(4, 'Meera Iyer', '2025-12-01', '2026-04-01', '2025-12-01 17:05:00', 'Monthly'),
(5, 'Sanjay Patel', '2025-11-20', '2026-03-20', '2025-11-20 13:00:00', 'Quarterly');

update subscriptions set plan_type = 'Yearly' where sub_id = 4;

select sub_id, customer_name , start_date , expiry_date from subscriptions
where datediff(expiry_date,current_date()) between 0 and 45 order by expiry_date asc;

select sub_id, customer_name , start_date , expiry_date from subscriptions
where year(start_date) = year(current_date()) and month(start_date) = month(current_date());

select sub_id, customer_name , start_date , expiry_date from subscriptions
where plan_type = 'Yearly' order by expiry_date asc;

select sub_id, customer_name , start_date , expiry_date, datediff(expiry_date,start_date) as Duration from subscriptions
where datediff(expiry_date,start_date) > 30 order by Duration desc;

select sub_id, customer_name , start_date , expiry_date from subscriptions
where expiry_date < start_date;

