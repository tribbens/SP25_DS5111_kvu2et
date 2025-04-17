## Entity Relationship Diagram (ERD)

The following diagram represents the relationships between various classes in our stock market gainer processing pipeline:

```mermaid
erDiagram
    GAINER_FACTORY {
        string choice
    }
    GAINER_FACTORY ||--o{ GAINER_DOWNLOAD : uses
    GAINER_FACTORY ||--o{ GAINER_PROCESS : uses
    GAINER_DOWNLOAD {
        string url
        void download()
    }
    GAINER_PROCESS {
        string fname
        string source
        datetime datetime_now
        void normalize()
        void save_with_timestamp()
    }
    GAINER_DOWNLOAD }|--o{ GAINER_DOWNLOAD_YAHOO : is_a
    GAINER_DOWNLOAD }|--o{ GAINER_DOWNLOAD_WSJ : is_a
    GAINER_DOWNLOAD }|--o{ GAINER_DOWNLOAD_SA : is_a
    GAINER_PROCESS }|--o{ GAINER_PROCESS_YAHOO : is_a
    GAINER_PROCESS }|--o{ GAINER_PROCESS_WSJ : is_a
    GAINER_PROCESS }|--o{ GAINER_PROCESS_SA : is_a
    GAINER_DOWNLOAD_YAHOO {
        string url
    }
    GAINER_DOWNLOAD_WSJ {
        string url
    }
    GAINER_DOWNLOAD_SA {
        string url
    }
    GAINER_PROCESS_YAHOO {
        string source
    }
    GAINER_PROCESS_WSJ {
        string source
    }
    GAINER_PROCESS_SA {
        string source
    }
