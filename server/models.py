from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_in_stock = db.Column(db.Boolean, default=True)  # Default to True if not provided

    # Optional: Add a custom serialization field
    serialize_only = ('id', 'name', 'image', 'price', 'is_in_stock')

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'

# Create the database and tables
def create_database(app):
    with app.app_context():
        db.create_all()
