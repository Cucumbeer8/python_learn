import sqlite3

conn = sqlite3.connect('yan.db')
cursor = conn.cursor()

query = """
WITH task_counts AS (
    SELECT
        w.worker_id,
        w.name,
        COUNT(t.task_id) AS tasks
    FROM
        workers w
    LEFT JOIN
        tasks t ON w.worker_id = t.worker_id
    GROUP BY
        w.worker_id, w.name
)

SELECT
    name,
    tasks
FROM
    task_counts
ORDER BY
    tasks DESC
LIMIT 3

UNION ALL

SELECT
    name,
    tasks
FROM
    task_counts
WHERE
    tasks = 0;
"""

cursor.execute(query)

results = cursor.fetchall()

conn.close()

print("name | tasks")
for row in results:
    print(f"{row[0]} | {row[1]}")
