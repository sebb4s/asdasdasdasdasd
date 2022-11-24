from flask import Flask, jsonify
from flask_cors import CORS

from models.food_shift import FoodShift

app = Flask(__name__)

CORS(app)

@app.route('/api/food-stores/sales', methods = ['GET'])
def get_food_stores():
    "GET Method of the specified endpoint"
    proof_bread:FoodShift = FoodShift(
        title="ENSALADA",
        image="https://imagenes.elpais.com/resizer/EEtfvydYVpLOLHfVjh5wJv-5N4U=/980x980/cloudfront-eu-central-1.images.arcpublishing.com/prisa/FMTJOADPX5GQZHWKQP6JMRBXVU.jpg",
        description="""Las ensaladas encabezan el puesto de mayor comidas desechadas en hoteles, sumando una cifra de 30 toneladas por año""")

    bio_company:FoodShift = FoodShift(
        title="FRUTAS",
        image= "https://www.publico.es/uploads/2017/12/13/5a31519a2f0ec.jpg",
        description = "")

    denns_bio:FoodShift = FoodShift(
        title="PASTAS",
        image="https://www.lavanguardia.com/files/og_thumbnail/uploads/2018/09/23/5fa4504cb604d.jpeg",
        description="""Las pastas es la tercer comida más desechada en hoteles, siendo una cantidad de 15 toneladas de pasta desperdiciada por año""")
    food_stores:tuple = (proof_bread, bio_company, denns_bio)

    return jsonify([item.serialize() for item in food_stores])


if __name__ == '__main__':
    app.run()