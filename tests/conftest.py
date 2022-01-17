import json

import pytest
import requests

from services.listing_service import ListingService


@pytest.fixture(scope="session")
def config():
    with open("config.json") as config_file:
        config = json.load(config_file)

    return config


@pytest.fixture(scope="session")
def token(config):
    credentials = {
        "content_type": config["content_type"],
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "grant_type": config["grant_type"],
        "username": config["username"],
        "password": config["password"]
    }
    response = requests.post(f"{config['identity_server_url']}/connect/token", credentials)
    ListingService.handle_response_status(response, "getting")

    access_token = response.json()["access_token"]

    return access_token
