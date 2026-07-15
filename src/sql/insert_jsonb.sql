INSERT INTO {{schema}}.raw_users (raw_data, batch_id, ingested_at)
SELECT 
    to_jsonb(t), 
    CAST(:batch_id AS UUID), 
    CAST(:ingested_at AS TIMESTAMPTZ)
FROM {{schema}}.{{temp_table}} t;