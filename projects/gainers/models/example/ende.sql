-- ende.sql
SELECT *
FROM {{ source('kvu2et_raw', 'ende_raw') }}
