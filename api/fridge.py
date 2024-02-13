import requests


class FridgeApi:
    def __init__(self, domain):
        self.url = f"{domain}/api/fridge"

    def get_fridges_list(self):
        response = requests.get(self.url)
        list_of_existing_fridges = response.json()
        return list_of_existing_fridges

    def create_fridge(self):
        response = requests.post(self.url)
        return response

    def get_food_in_fridge(self, fridge_id):
        food_url = f"{self.url}/{fridge_id}/food"
        response = requests.get(food_url)
        return response

    def add_food_to_fridge(self, fridge_id, food_name, quantity, expires_in):
        food_url = f"{self.url}/{fridge_id}/food"
        response = requests.put(
            food_url,
            json={
                "food_name": food_name,
                "quantity": str(quantity),
                "expires_in": str(expires_in)
            }
        )
        return response
