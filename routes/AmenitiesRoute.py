from flask import Blueprint
from controllers.AmenitiesController import AmenitiesController

amenities_bp = Blueprint('amenities_bp', __name__)

@amenities_bp.route('/amenities', methods=['GET'])
def get_amenities():
    return AmenitiesController.get_all_amenities()

@amenities_bp.route('/amenities', methods=['POST'])
def create_amenity():
    return AmenitiesController.create_amenity()

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    return AmenitiesController.update_amenity(amenity_id)

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    return AmenitiesController.delete_amenity(amenity_id)

@amenities_bp.route('/bulk', methods=['POST'])
def insert_bulk_amenities():
    return AmenitiesController.insert_bulk_amenities()