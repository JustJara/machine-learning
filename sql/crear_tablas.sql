CREATE TABLE IF NOT EXISTS cluster_data (
    id SERIAL PRIMARY KEY,
    data_text TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cluster_info (
    id SERIAL PRIMARY KEY,
    cluster_text TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clustering_results (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    num_clusters INTEGER NOT NULL,
    cluster_results JSONB NOT NULL
);