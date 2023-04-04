from flask import Flask, request, json
import db
import repository
import services

app = Flask(__name__)

mysql_db = db.connect_my_sql()
laptop_repository = repository.LaptopBestSellerRepository(mysql_db)
laptop_service = services.LaptopBestSellerService(laptop_repository)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/laptop', methods=["POST"])
def create():
    req = request.json
    return laptop_service.create_laptop(req)


@app.route('/api/laptop/<id_laptop>', methods=["PUT"])
def edit_laptop(id_laptop):
    req = request.json
    return laptop_service.edit_laptop(req, id_laptop)


@app.route('/api/laptop/<id_laptop>', methods=["DELETE"])
def delete_laptop(id_laptop):
    return laptop_service.delete_laptop(id_laptop)


@app.route('/api/laptop', methods=["GET"])
def list_laptop():
    return laptop_service.list_laptop()


app.run()
