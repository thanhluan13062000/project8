CREATE SCHEMA IF NOT EXISTS {{schema}};
CREATE TABLE IF NOT EXISTS {{schema}}.raw_users (
    id SERIAL PRIMARY KEY, 
    raw_data JSONB NOT NULL, 
    ingested_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    batch_id UUID DEFAULT gen_random_uuid() 
);