# Habr Article Scraper

## Website
- https://habr.com/ru/feed/

## Database Schema
Articles table:
- id (INTEGER PRIMARY KEY)
- title (TEXT): The article title
- url (TEXT UNIQUE): Full URL to the article
- collected_at (TEXT): ISO format timestamp of when the data was collected

## Technology Stack
- Python 3.x
- Scrapy (web scraping framework)
- SQLite (database)
- CSS Selectors (for parsing HTML)

## Data storage
- SQLite

Saved in file `habr_articles.db`

## Scraping
- Scrapy
