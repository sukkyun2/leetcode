# Write your MySQL query statement below
-- 두가지 방법 존재

SELECT 
    DISTINCT L1.NUM AS ConsecutiveNums
FROM LOGS L1
LEFT JOIN LOGS L2 ON L1.ID+1 = L2.ID
LEFT JOIN LOGS L3 ON L1.ID+2 = L3.ID
WHERE L1.NUM = L2.NUM && L2.NUM = L3.NUM
