from app import db

EMOTIONS = [
    'anxious',
    'angry',
    'joy',
    'sadness',
    'confusion',
    'disappointment',
    'jealous',
    'ashamed',
    'excited',
    'hopeless',
    'inspired'
]


class Mood(db.Model):
    __tablename__ = 'moods'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    summary = db.Column(db.String(255))
    primary_emotion = db.Column(db.String(255))
    secondary_emotion = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, *args, **kwargs):
        self.title = kwargs['title']
        self.summary = kwargs['summary']
        self.primary_emotion = kwargs['primary_emotion']
        self.secondary_emotion = kwargs['secondary_emotion']

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_moods():
        return Mood.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Mood: {}>".format(self.title)