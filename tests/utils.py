from src.models import Movie, db

def create_movie():
    test_movie = Movie(title='The Dark Knight', director='Christopher Nolan', rating=5)
    db.session.add(test_movie)
    db.session.commit()
    return test_movie