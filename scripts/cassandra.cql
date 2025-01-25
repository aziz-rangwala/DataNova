CREATE KEYSPACE datanova WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE datanova;
CREATE TABLE events (
    user_id UUID PRIMARY KEY,
    event_type TEXT,
    timestamp TIMESTAMP,
    metadata TEXT
);
