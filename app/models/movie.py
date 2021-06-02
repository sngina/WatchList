class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_avarage,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.vote_average = vote_avarage
        self.vote_count = vote_count #we have defined a movie class  and then we create an __init__ method and pass in six prameters we want inside our movie objects..

        
