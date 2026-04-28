import os

DB_CONFIG = {
    "host":     os.getenv("DB_HOST",     "localhost"),
    "port":     int(os.getenv("DB_PORT", 5432)),
    "dbname":   os.getenv("DB_NAME",     "phonebook"),
    "user":     os.getenv("DB_USER",     "arman"),
    "password": os.getenv("DB_PASSWORD", "ARbt7274FWG"),
}

PAGE_SIZE = 5