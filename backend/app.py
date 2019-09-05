from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify([
        {
            'name': 'Veggie Paradise',
            'price': 100,
            'location': 'Pune',
            'rating': 4.5,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/db6ae6846c4faafc625d6f109fabcbf1-full.jpg'
        },
        {
            'name': 'Veg Extravagenza',
            'price': 200,
            'location': 'Bengaluru',
            'rating': 5,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/0993d6f5df010715468f590207696b53-full.jpg'
        },
        {
            'name': 'Mixed Veg',
            'price': 500,
            'location': 'Nagpur',
            'rating': 3.5,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/8222c36cd027940cf6b819ac91d7c67b-full.jpg'
        },
        {
            'name': 'Veg Cheese Pizza',
            'price': 120,
            'location': 'Mumbai',
            'rating': 1.5,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/eb2fead96e43709d91996d15b26117b1-full.jpg'
        },
        {
            'name': 'Mix Veg Cheese',
            'price': 160,
            'location': 'Solapur',
            'rating': 1.2,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/c64858da5c02f0fa7e1b225d685239ea-full.jpg'
        },
        {
            'name': 'Chicken Pizza',
            'price': 850,
            'location': 'Delhi',
            'rating': 4.2,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/40eeaf13596f35facec09442a50bc759-full.jpg'
        },
        {
            'name': 'Veg Ausse Pizza',
            'price': 130,
            'location': 'Goa',
            'rating': 3.5,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/c64858da5c02f0fa7e1b225d685239ea-full.jpg'
        },
        {
            'name': 'Veg Margarita',
            'price': 160,
            'location': 'Nagpur',
            'rating': 2.7,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/0993d6f5df010715468f590207696b53-full.jpg'
        },
        {
            'name': 'Veg Farmhouse',
            'price': 140,
            'location': 'Indore',
            'rating': 2.8,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/f6a282f5131b1dd4bb68a747980d7fae-full.jpg'
        },
        {
            'name': 'Veg Supreme',
            'price': 190,
            'location': 'Hyderabad',
            'rating': 3.1,
            'image': 'https://cdn1.imggmi.com/uploads/2019/9/4/22d97cd50a46b2127482212ae5a6dd8e-full.jpg'
        }
    ])

if __name__ == '__main__':
    app.run(debug=True)