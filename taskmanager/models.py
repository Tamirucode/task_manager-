
from taskmanager import app, db


class User(db.Model):
    # schema for the Userdata model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(10), unique=True, nullable=False)
    pass_word = db.Column(db.String(10), unique=True, nullable=False)
    last_name = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(10), unique=True, nullable=False)
    contact_number = db.Column(db.Integer, primary_key=True)
    tabledatas = db.relationship("Tabledata", backref="user", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.id, self.user_name, self.pass_word, self.last_name, self.email


class Tabledata(db.Model):
    # schema for the table model
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.Text, nullable=False)
    number_people = db.Column(db.Integer, nullable=False)
    book_date = db.Column(db.Date, nullable=False)
    book_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.id, self.table_name, 


class Admindata(db.Model):
    # schema for the Admindata model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(10), unique=True, nullable=False)
    pass_word = db.Column(db.String(10), unique=True, nullable=False)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name, self.pass_word
        