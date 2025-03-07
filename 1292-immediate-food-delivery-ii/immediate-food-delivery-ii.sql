# Write your MySQL query statement below
SELECT 
    ROUND(AVG(ORDER_DATE = customer_pref_delivery_date)*100,2) AS immediate_percentage 
FROM DELIVERY
WHERE (CUSTOMER_ID, ORDER_DATE) IN (
    SELECT 
        CUSTOMER_ID,
        MIN(ORDER_DATE) AS ORDER_DATE
    FROM DELIVERY
    GROUP BY CUSTOMER_ID
)