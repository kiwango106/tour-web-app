from flask import Blueprint

itinerary = Blueprint('itinerary', __name__)

from app.itinerary import routes
