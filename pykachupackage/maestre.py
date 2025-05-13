from faker import Faker

def generate_fake_profile():
    fake = Faker()
    name = fake.name()
    job = fake.job()
    email = fake.email()
    address = fake.address()

    print ("\n===== Profile =====")
    print(f"Name: {name}")
    print(f"Job: {job}")
    print(f"Email: {email}")
    print(f"Address: {address}")   