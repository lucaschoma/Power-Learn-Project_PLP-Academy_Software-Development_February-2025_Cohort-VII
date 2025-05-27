SELECT 
    payment_date, 
    SUM(amount) AS total_amount
FROM 
    payments
GROUP BY 
    payment_date
ORDER BY 
    payment_date DESC
LIMIT 5;
