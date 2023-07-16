class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def __str__(self):
        return '{} by {} ({} stars)'.format(self.title, self.author, self.rating)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __hash__(self):
        return hash((self.title, self.author))
    
    def __lt__(self, other):
        return self.title < other.title
    
    def __gt__(self, other):
        return self.title > other.title
    
    def __le__(self, other):
        return self.title <= other.title
    
    def __ge__(self, other):
        return self.title >= other.title