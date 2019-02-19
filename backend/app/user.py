from app import db 

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.email = kwargs['email']

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return User.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.username)