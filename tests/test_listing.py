from entities.factories.listing_factory import ListingFactory
from services.listing_service import ListingService


def test_listing_should_be_read(config, token):
    listing_service = ListingService()
    listed_attribute = "Listed"
    expected_status_code = 200

    # Arrange
    listing = ListingFactory().generate_fake_listing()
    payload = ListingFactory().listing_to_json(listing)
    create_listing = listing_service.create_listing(token, payload, config)
    id = ListingService().extract_id_from_headers(create_listing)

    # Act
    response = listing_service.get_listing(id, token, config)

    # Assert
    assert response.status_code == expected_status_code, f"Status code should be {expected_status_code}"
    assert response.json()["id"] == id, "Id should be equal as extracted"
    assert response.json()["listingStatus"].lower() == listed_attribute.lower(), \
        f"Listing status should be '{listed_attribute}'"


def test_listing_should_be_updated(config, token):
    listing_service = ListingService()
    expected_status_code = 204

    # Arrange
    created_listing = ListingFactory().generate_fake_listing()
    payload = ListingFactory().listing_to_json(created_listing)
    create_listing = listing_service.create_listing(token, payload, config)
    id = ListingService().extract_id_from_headers(create_listing)

    # Act
    updated_listing = ListingFactory().generate_fake_listing()
    payload = ListingFactory().listing_to_json(updated_listing)
    response = listing_service.update_listing(id, token, payload, config)

    # Assert
    assert response.status_code == expected_status_code, f"Status code should be {expected_status_code}"
    assert updated_listing == created_listing


def test_listing_should_be_created(config, token):
    listing_service = ListingService()
    expected_status_code = 201

    # Arrange
    expected_listing = ListingFactory().generate_fake_listing()
    payload = ListingFactory().listing_to_json(expected_listing)

    # Act
    create_listing = listing_service.create_listing(token, payload, config)
    actual_status_code = create_listing.status_code
    id = ListingService().extract_id_from_headers(create_listing)
    response = listing_service.get_listing(id, token, config)
    actual_listing = ListingService().extract_listing_from_response(response)

    # Assert
    assert actual_status_code == expected_status_code, f"Status code should be {expected_status_code}"
    assert actual_listing == expected_listing, "Listing data should be equal as created"


def test_listing_should_be_deleted(config, token):
    listing_service = ListingService()
    expected_status_code = 204

    # Arrange
    listing = ListingFactory().generate_fake_listing()
    payload = ListingFactory().listing_to_json(listing)
    create_listing = listing_service.create_listing(token, payload, config)
    id = ListingService().extract_id_from_headers(create_listing)

    # Act
    response = listing_service.delete_listing(id, token, config)

    # Assert
    assert response.status_code == expected_status_code, f"Status code should be {expected_status_code}"
