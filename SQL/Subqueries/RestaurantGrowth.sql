-- Table: Customer

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | customer_id   | int     |
-- | name          | varchar |
-- | visited_on    | date    |
-- | amount        | int     |
-- +---------------+---------+
-- In SQL,(customer_id, visited_on) is the primary key for this table.
-- This table contains data about customer transactions in a restaurant.
-- visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
-- amount is the total paid by a customer.


-- You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

-- Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

-- Return the result table ordered by visited_on in ascending order.

-- get the sum of each date first using with: https://dev.mysql.com/doc/refman/8.0/en/with.html
-- window function, how you order: https://dev.mysql.com/doc/refman/8.0/en/window-functions-usage.html
-- exclude those ;ess than 6 days
with
    cte as (
        select
            visited_on,
            sum(amount) as amount
        from
            Customer
        group by
            visited_on
    )

select
    *
from (
    select
        visited_on,
        sum(amount) over (order by visited_on ROWS 6 PRECEDING) as amount,
        round(avg(amount) over (order by visited_on ROWS 6 PRECEDING), 2) as average_amount
    from
        cte
) as temp
where
    date_sub(visited_on, interval 6 day) IN (select visited_on from cte)
order by visited_on asc

-- passed
-- Runtime 804 ms Beats 21.18% of users with MySQL
-- should be more familiar with the window function


