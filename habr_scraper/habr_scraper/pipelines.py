import sqlite3

class SQLitePipeline:
    def __init__(self):
        self.conn = sqlite3.connect('habr_articles.db')
        self.curr = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        self.curr.execute("""
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT UNIQUE,
            collected_at TEXT
        )
        """)
        
    def process_item(self, item, spider):
        self.curr.execute("""
        INSERT OR IGNORE INTO articles (title, url, collected_at)
        VALUES (?, ?, ?)
        """, (
            item['title'],
            item['url'],
            item['collected_at']
        ))
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.conn.close()