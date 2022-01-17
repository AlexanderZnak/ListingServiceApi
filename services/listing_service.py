import requests
from requests import Response, HTTPError

from models.listing import Listing


class ListingService:

    @staticmethod
    def extract_id_from_headers(response: Response):
        return response.headers.get("Location").split("listings/id/")[1]

    @staticmethod
    def create_rest_request(method, url, headers, payload=None):
        if payload is not None:
            return requests.request(method=method, url=url, headers=headers, data=payload)
        else:
            return requests.request(method=method, url=url, headers=headers)

    @staticmethod
    def handle_response_status(response, action):
        if response.ok is False:
            raise HTTPError(
                f"An error occurred while {action} listing. Reason: {response.reason}, status code : "
                f"{response.status_code}")

    def create_listing(self, token, listing, config):
        response = self.create_rest_request("POST", f"{config['listing_server_url']}/listings/",
                                            {"Authorization": f"Bearer {token}"}, listing)
        self.handle_response_status(response, "creating")

        return response

    def get_listing(self, id, token, config):
        response = self.create_rest_request("GET", f"{config['listing_server_url']}/listings/id/{id}",
                                            {"Authorization": f"Bearer {token}"})
        self.handle_response_status(response, "getting")

        return response

    def update_listing(self, id, token, listing, config):
        response = self.create_rest_request("PUT", f"{config['listing_server_url']}/listings/id/{id}",
                                            {"Authorization": f"Bearer {token}"}, listing)
        self.handle_response_status(response, "creating")

        return response

    def delete_listing(self, id, token, config):
        response = self.create_rest_request("DELETE", f"{config['listing_server_url']}/listings/id/{id}",
                                            {"Authorization": f"Bearer {token}"})
        self.handle_response_status(response, "deleting")

        return response

    @staticmethod
    def extract_listing_from_response(response: Response):
        listing = Listing(**response.json())
        return listing
