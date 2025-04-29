-- 1. Basic SELECT with Wildcards and WHERE
SELECT * FROM Expenses
WHERE description LIKE '%food%';

-- 2. Using Comparison Operators
SELECT * FROM Expenses
WHERE amount > 100;

-- 3. Combining Filters with Logical Operators
SELECT * FROM Expenses
WHERE category = 'Travel' OR amount > 500;
SELECT * FROM Expenses
WHERE NOT (category = 'Bills' AND amount < 50);

-- 4. Ordering the Results
SELECT * FROM Expenses
WHERE YEAR(expense_date) = 2024
ORDER BY amount DESC;

