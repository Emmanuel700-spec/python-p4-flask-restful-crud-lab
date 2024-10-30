#!/usr/bin/env python3

from app import app
from models import db, Plant

if __name__ == '__main__':
    with app.app_context():
        # Start the interactive debugger
        import ipdb; ipdb.set_trace()

        # You can now run commands in this context
        # For example, you can query the database:
        plants = Plant.query.all()  # Fetch all plants
        print(plants)  # This will print the list of plant objects

        # Or check for a specific plant by ID:
        plant_id = 1
        plant = Plant.query.filter_by(id=plant_id).first()
        print(plant)  # Print the specific plant object

        # Feel free to add more code here to explore the app context
