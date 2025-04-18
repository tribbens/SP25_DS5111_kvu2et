# Entity Relationship Diagram for Daily Stock Gainer List Analysis

## ERD (in Mermaid.js)

```mermaid
erDiagram
    %% Raw data ingested daily
    RAW_GAINER_RECORDS {
        VARCHAR symbol
        DATE   date
        FLOAT  high
        FLOAT  low
        FLOAT  open
        FLOAT  close
        BIGINT volume
    }
    %% Dimension tables
    SYMBOLS {
        VARCHAR symbol PK
    }
    DATES {
        DATE   date PK
        INT    week_number
        DATE   week_start
    }
    %% Intermediate aggregates
    DAILY_COUNTS {
        VARCHAR symbol FK
        DATE    date FK
        INT     appearance_count
    }
    DAILY_STATS {
        VARCHAR symbol FK
        DATE    date FK
        FLOAT   avg_high
        FLOAT   avg_low
        FLOAT   avg_open
        FLOAT   avg_close
        BIGINT  total_volume
    }
    %% Final weekly summaries
    WEEKLY_SUMMARY {
        VARCHAR symbol FK
        DATE    week_start FK
        INT     weekly_appearances
        BIGINT  weekly_volume
        FLOAT   avg_weekly_price_range
    }

    %% Relationships
    RAW_GAINER_RECORDS }o--|| SYMBOLS       : "belongs to"
    RAW_GAINER_RECORDS }o--|| DATES         : "occurs on"
    SYMBOLS           ||--o{ DAILY_COUNTS  : "aggregated in"
    DATES             ||--o{ DAILY_COUNTS  : "aggregated by"
    SYMBOLS           ||--o{ DAILY_STATS   : "aggregated in"
    DATES             ||--o{ DAILY_STATS   : "aggregated by"
    SYMBOLS           ||--o{ WEEKLY_SUMMARY: "summarized in"
    DATES             ||--o{ WEEKLY_SUMMARY: "week of"
