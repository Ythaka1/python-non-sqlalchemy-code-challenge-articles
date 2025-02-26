
class Article:
    all = []  

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author._articles.append(self)  
        magazine._articles.append(self)


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Author name cannot be changed")  

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)  

    def topic_areas(self):
        if not self._articles:
            return None  
        return list(set(article.magazine.category for article in self._articles if article.magazine))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise TypeError("Both name & category must be strings ")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")        
        if len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Magazine category must be a string")
        if len(new_category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self._category = new_category


    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def add_article(self, author, title):
        return Article(author, self, title)  

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    
    
   
