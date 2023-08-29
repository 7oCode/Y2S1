class Books():

    def __init__(self,isbn, title, category, publisher, year_published):
        self.__title = title
        self.__category = category
        self.__publisher = publisher
        self.__year_published = year_published
        self.__isbn = isbn

    # Set methods

    def set_title(self, title):
        self.__title = title

    def set_category(self,category):
        self.__category = category

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_year_published(self,yearpublished):
        self.__year_published = yearpublished

    # Get

    def get_title(self):
        return self.__title

    def get_category(self):
        return self.__category

    def get_publisher(self):
        return self.__publisher

    def get_year_published(self):
        return self.__year_published

    def get_isbn(self):
        return self.__isbn
