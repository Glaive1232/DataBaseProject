import requests
import random
from faker import Faker

fake = Faker()
BASE_URL = "http://localhost:8000"

# Функция для создания заказчиков (Customers)
def create_customers(num_customers):
    for _ in range(num_customers):
        customer_data = {
            "name": fake.company(),
            "total_budget": round(random.uniform(10000, 1000000), 2),
            "additional_info": fake.text(max_nb_chars=100),
        }
        response = requests.post(f"{BASE_URL}/customers/", json=customer_data)
        if response.status_code == 200:
            print(f"Created customer: {response.json()['name']}")
        else:
            print(f"Failed to create customer: {response.text}")

# Функция для создания объектов (Construction Objects)
def create_construction_objects(num_objects, customer_ids):
    for _ in range(num_objects):
        object_data = {
            "name": fake.word().capitalize(),
            "type": fake.word(),
            "cost": round(random.uniform(50000, 500000), 2),
            "start_date": fake.date_this_decade(),
            "end_date": fake.date_this_decade(),
            "customer_id": random.choice(customer_ids),
        }
        response = requests.post(f"{BASE_URL}/construction_objects/", json=object_data)
        if response.status_code == 200:
            print(f"Created construction object: {response.json()['name']}")
        else:
            print(f"Failed to create construction object: {response.text}")

# Функция для создания подрядчиков (Contractors)
def create_contractors(num_contractors, construction_object_ids):
    for _ in range(num_contractors):
        contractor_data = {
            "name": fake.name(),
            "specialization": fake.job(),
            "num_employees": random.randint(5, 50),
            "equipment_level": fake.word(),
            "tools_level": fake.word(),
        }
        response = requests.post(f"{BASE_URL}/contractors/", json=contractor_data)
        if response.status_code == 200:
            contractor = response.json()
            print(f"Created contractor: {contractor['name']}")

            # Добавляем связи подрядчика с объектами
            for _ in range(random.randint(1, 3)):
                object_id = random.choice(construction_object_ids)
                link_response = requests.post(
                    f"{BASE_URL}/contractors/{contractor['id']}/link_object/",
                    json={"object_id": object_id},
                )
                if link_response.status_code == 200:
                    print(f"Linked contractor {contractor['id']} with object {object_id}")
                else:
                    print(f"Failed to link contractor: {link_response.text}")
        else:
            print(f"Failed to create contractor: {response.text}")

def main():
    num_customers = 10
    create_customers(num_customers)

    customers_response = requests.get(f"{BASE_URL}/customers/")
    customer_ids = [customer["id"] for customer in customers_response.json()]

    num_objects = 20
    create_construction_objects(num_objects, customer_ids)

    objects_response = requests.get(f"{BASE_URL}/construction_objects/")
    construction_object_ids = [obj["id"] for obj in objects_response.json()]

    num_contractors = 15
    create_contractors(num_contractors, construction_object_ids)


if __name__ == "__main__":
    main()
