import requests  # Библиотека для запросок в API
from bs4 import BeautifulSoup  # Визуальное улучшение парсинга данных
import sqlite3


class BlogArticle:
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def to_dict(self) -> dict:
        return {'title': self.title, 'text': self.text}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['title'], data['text'])
    
class BlogParser:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0"
        }

    def get_article_links(self) -> list[str]:
        response = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            if  '/articles/' in a['href']:
                full_url = a['href']
                if not full_url.startswith('http'):
                    full_url = "https://msk.top-academy.ru" + full_url
                if full_url not in links:
                    links.append(full_url)
        return links

    def parse_article(self, url: str) -> BlogArticle | None: 
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            card_body = soup.find(class_='styles_cardBody__qP0jN')
            if card_body: 
                title = (card_body.find('h1').get_text(strip=True) 
                         if card_body.find('h1') 
                         else "Без заголовка")
                paragraph = card_body.find_all('p')
                text = " ".join([p.get_text(strip=True) for p in paragraph])
                return BlogArticle(title, text)
        except Exception as e:
            print(f'Error: {e}')
            return None

class DatabaseManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            query = """
                CREATE TABLE IF NOT EXISTS articles (
                id integer primary key autoincrement,
                title text unique,
                text text
                );
            """

            conn.execute(query)
            conn.commit()

    def save_articles(self, articles: list[BlogArticle]) -> int:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            saved_count = 0

            for art in articles:
                try: 
                    cursor.execute(
                        """
                        insert into articles (title, text)
                        values (?, ?);
                    """, (art.title, art.text)
                    )
                    if cursor.rowcount > 0:
                        saved_count += 1
                    
                except Exception as e:
                    print(f'Error BD: {e}')
            conn.commit()
            return saved_count
        
    def get_top_articles(self, limit: int=5) -> list[tuple]:
        with sqlite3.connect(self.db_name) as conn: 
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT title, text FROM articles
                ORDER BY id DESC LIMIT (?);
            """, (limit, )
            )

            return cursor.fetchall()


def main():
    
    url = 'https://msk.top-academy.ru/blog'
    print(f'Парсинг страницы {url}')
    parser = BlogParser(url)
    db_name = 'top_academy_blog.db'
    db = DatabaseManager(db_name)
    links = parser.get_article_links()
    articles_data = []
    
    for link in links:
        article = parser.parse_article(link)
        articles_data.append(article)
    print(f'Найдено {len(articles_data)} статей.')

    print(f'\nСохранение в базу данных...')
    saved_count = db.save_articles(articles_data)
    print(f'Добавлено {saved_count} статей.')

    print(f'\n Последние 5 добавленных статей:')
    articles = db.get_top_articles()

    for i, (title, text) in enumerate(articles, 1):
        short_text = text[:100] + '...' if len(text) > 100 else text
        print(f'{i:2}. Заголовок: "{title}"')
        print(f'{'':3} Текст: "{short_text}"\n')


if __name__ == '__main__':
    main()
    