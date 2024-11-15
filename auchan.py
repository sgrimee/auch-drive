import os
from typing import List

import httpx
from dotenv import load_dotenv
from loguru import logger


class Product:
    """A product sold by the store."""

    def __init__(self, json_obj):
        self.id = json_obj["id_product"]
        self.name = json_obj["name"]

    def __str__(self):
        return f"Product(name={self.name}, id={self.id})"


class WishList:
    """A list of products."""

    def __init__(self, json_obj):
        self.id = json_obj["id_wishlist"]
        self.name = json_obj["name"]

    def __str__(self):
        return f"List(name={self.name}, id={self.id})"


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = httpx.Client()
        self.json_headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/json",
        }

    def authenticate(self, email: str, password: str):
        """Authenticates with the store API.

        Must be run once before any other method.
        """
        data = {"email": email, "password": password, "submitLogin": "1"}
        r = self.session.post(
            self.base_url + "/connexion", data=data, follow_redirects=True
        )
        r.raise_for_status()

    def get_lists(self) -> List[WishList]:
        """Returns the list of wishlists saved by the user."""
        params = {"action": "getAllWishlist"}
        r = self.session.get(
            self.base_url + "/module/mywishlist/action",
            params=params,
            headers=self.json_headers,
        )
        r.raise_for_status()
        return [WishList(item) for item in r.json()["wishlists"]]

    def create_list(self, name: str) -> WishList:
        """Create a new wishlist."""
        params = {"action": "createNewWishlist", "params[name]": name}
        r = self.session.post(
            self.base_url + "/module/mywishlist/action",
            params=params,
            headers=self.json_headers,
        )
        r.raise_for_status()
        res = r.json()
        assert res["success"]
        return WishList(res["datas"])

    def get_products_in_list(self, list: WishList) -> List[Product]:
        params = {"id_wishlist": str(list.id), "from-xhr": ""}
        r = self.session.get(
            self.base_url + "/module/mywishlist/view",
            headers=self.json_headers,
            params=params,
        )
        r.raise_for_status()
        return [Product(item) for item in r.json()["products"]]

    def add_product_to_list(self, product: Product, list: WishList):
        """Add a product to a wishlist."""
        logger.debug(f"Adding {product} to {list}")
        params = {
            "action": "addProductToWishlist",
            "params[id_product]": product.id,
            "params[idWishList]": list.id,
            "params[quantity]": 1,
            "params[id_product_attribute]": 0,
        }
        r = self.session.post(
            self.base_url + "/module/mywishlist/action",
            params=params,
            headers=self.json_headers,
        )
        r.raise_for_status()
        assert r.json()["success"]


def main():
    # get credentials from the .env file
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    if not email or not password:
        raise ValueError("EMAIL and PASSWORD must be set in the environment variables")

    # authenticate to the API
    client = ApiClient("https://auchandrive.lu/munsbach")
    client.authenticate(email, password)

    # Get products from all lists, merge them removing duplicates
    products = set()
    lists = client.get_lists()
    for list in lists:
        logger.debug(f"Processing list {list}")
        for product in client.get_products_in_list(list):
            products.add(product)

    # Create a new list and add all products to it
    new_list = client.create_list("2024-11-15 merged")
    logger.debug(f"Created new list {new_list}")

    for product in products:
        client.add_product_to_list(product, new_list)


if __name__ == "__main__":
    main()
