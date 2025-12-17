from faker import Faker

fake = Faker(locale="ru_Ru")

print(f"{fake.locales=}")

print(f"{fake.last_name_male()=}")
print(f"{fake.first_name_male()=}")
print(f"{fake.middle_name_male()=}")
print(f"{fake.email()=}")
print(f"{fake.sentence()=}")
print(f"{fake.random_int(1, 10)=}")
print(f"{fake.text()=}")
print(f"{fake.uuid4(cast_to=None)=}, {type(fake.uuid4(cast_to=None))=}")
print(f"{fake.uuid4()=}, {type(fake.uuid4())=}")
print(f"{fake.password()=}")


user_data = {"name": fake.name_male(), "email": fake.email(), "address": fake.address()}

print(f"{user_data=}")
