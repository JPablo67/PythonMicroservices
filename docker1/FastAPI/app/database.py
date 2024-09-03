from dotenv import load_dotenv
from peewee import *
from datetime import date

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


class OrderModel(Model):
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='orders', on_delete='CASCADE')
    item_id = IntegerField()
    total_amount = FloatField()
    status = CharField(max_length=50)
    date = DateField(default=date.today)

    class Meta:
        database = database
        table_name = "orders"


class MovieModel(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    director = CharField(max_length=100)
    release_year = IntegerField()
    genre = CharField(max_length=50)
    rating = FloatField(null=True)  # Allow null for optional rating

    class Meta:
        database = database
        table_name = "movies"


class CarModel(Model):
    id = AutoField(primary_key=True)
    make = CharField(max_length=50)
    model = CharField(max_length=50)
    year = IntegerField()
    vin = CharField(max_length=50, unique=True)
    color = CharField(max_length=50, null=True)  # Allow null for optional color

    class Meta:
        database = database
        table_name = "cars"


class BookModel(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    isbn = CharField(max_length=50, unique=True)
    published_year = IntegerField()
    genre = CharField(max_length=50, null=True)  # Allow null for optional genre

    class Meta:
        database = database
        table_name = "books"


class AddressModel(Model):
    id = AutoField(primary_key=True)
    street = CharField(max_length=100)
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    zip_code = CharField(max_length=20)
    country = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "addresses"