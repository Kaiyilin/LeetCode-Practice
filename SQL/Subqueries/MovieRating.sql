-- Table: Movies

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | title         | varchar |
-- +---------------+---------+
-- movie_id is the primary key (column with unique values) for this table.
-- title is the name of the movie.
 

-- Table: Users

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | name          | varchar |
-- +---------------+---------+
-- user_id is the primary key (column with unique values) for this table.
 

-- Table: MovieRating

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | movie_id      | int     |
-- | user_id       | int     |
-- | rating        | int     |
-- | created_at    | date    |
-- +---------------+---------+
-- (movie_id, user_id) is the primary key (column with unique values) for this table. 
-- This table contains the rating of a movie by a user in their review.
-- created_at is the user's review date. 
 

-- Write a solution to:

-- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
-- The result format is in the following example.


(

select
    name as results
from (
    select
        u.name,
        count(u.name) as max_count
    from
        MovieRating as mr
    inner join Users as u
    on mr.user_id = u.user_id
    group by u.name
    order by max_count desc, u.name asc
) as temp
limit 1
)

union all

(
select
    m.title as results
from MovieRating as mr
inner join Movies as m
on mr.movie_id = m.movie_id
where mr.created_at like "2020-02-%"
group by m.title
order by avg(mr.rating) desc, m.title asc
limit 1
)

-- passed, Runtime 2223 ms Beats 71.00% of users with MySQL
-- is it possible to optimise it ?