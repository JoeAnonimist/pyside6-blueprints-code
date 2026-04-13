-- Account Summary Report (September 2025)
SELECT 
    a.account_id, 
    a.account_name, 
    u.username AS owner,
    COALESCE(c.category_name, 'N/A') AS category_name,
    COUNT(t.transaction_id) AS transaction_count,
    COALESCE(SUM(t.amount), 0) AS total_amount,
    COALESCE(AVG(t.amount), 0) AS avg_transaction,
    COALESCE((
        SELECT SUM(t2.amount)
        FROM Transactions t2
        WHERE t2.account_id = a.account_id
          AND t2.transaction_date LIKE '2025-09%'
    ), 0) AS net_balance
FROM 
    Accounts a
    INNER JOIN Users u ON a.user_id = u.user_id
    LEFT JOIN Transactions t ON a.account_id = t.account_id 
        AND t.transaction_date LIKE '2025-09%'
    LEFT JOIN Categories c ON t.category_id = c.category_id
GROUP BY 
    a.account_id, a.account_name, u.username, c.category_name

UNION ALL

-- Per-account totals
SELECT 
    a.account_id, 
    a.account_name, 
    u.username AS owner,
    'Total' AS category_name,
    COUNT(t.transaction_id) AS transaction_count,
    COALESCE(SUM(t.amount), 0) AS total_amount,
    COALESCE(AVG(t.amount), 0) AS avg_transaction,
    COALESCE(SUM(t.amount), 0) AS net_balance
FROM 
    Accounts a
    INNER JOIN Users u ON a.user_id = u.user_id
    LEFT JOIN Transactions t ON a.account_id = t.account_id 
        AND t.transaction_date LIKE '2025-09%'
GROUP BY 
    a.account_id, a.account_name, u.username

UNION ALL

-- Grand total
SELECT 
    NULL AS account_id, 
    'Grand Total' AS account_name,
    NULL AS owner, 
    NULL AS category_name,
    COUNT(t.transaction_id) AS transaction_count,
    COALESCE(SUM(t.amount), 0) AS total_amount,
    COALESCE(AVG(t.amount), 0) AS avg_transaction,
    COALESCE(SUM(t.amount), 0) AS net_balance
FROM 
    Transactions t
WHERE 
    t.transaction_date LIKE '2025-09%'

ORDER BY 
    account_id, category_name;
