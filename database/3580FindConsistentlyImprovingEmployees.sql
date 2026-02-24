# Write your MySQL query statement below
with a as(select employee_id,count(review_id) as reviews
from performance_reviews
group by employee_id having count(review_id)>=3)
, b as (
    select a.employee_id,review_date,rating,row_number() over(partition by employee_id order by review_date) as rn from a left join performance_reviews p on a.employee_id=p.employee_id
     )
     , c as(
        select * , row_number() over(partition by employee_id order by review_date desc) as rev_rn from b
        )
        , d as (
            select * from c where rev_rn between 1 and 3

        )
        , e as (
            select employee_id, max(case when rev_rn=1 then review_date end) as review_date_1,
            max(case when rev_rn=1 then rating end) as rating_1,
            max(case when rev_rn=2 then review_date end) as review_date_2,
            max(case when rev_rn=2 then rating end) as rating_2,
            max(case when rev_rn=3 then review_date end) as review_date_3,
            max(case when rev_rn=3 then rating end) as rating_3
            from d group by employee_id order by employee_id
        )
        select e.employee_id, name, rating_1-rating_3 as improvement_score 
        from e left join employees em on e.employee_id=em.employee_id
        where rating_1> rating_2 and rating_2>rating_3
        order by rating_1-rating_3 desc, name asc