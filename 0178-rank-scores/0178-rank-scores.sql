# Write your MySQL query statement below
# window function dense_rank
SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS `rank`
FROM Scores;