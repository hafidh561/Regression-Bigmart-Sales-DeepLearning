from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from model import predict_model

app = Flask(__name__)
api = Api(app)
CORS(app)

api_args = reqparse.RequestParser()
api_args.add_argument('item_weight', type=float,
                      help='Weight of product', required=True)
api_args.add_argument('item_fat_content', type=str,
                      help='Whether the product is low fat or not',
                      required=True)
api_args.add_argument('item_visibility', type=float,
                      help='The % of total display area of all products in a store allocated to \
                      the particular product',
                      required=True)
api_args.add_argument('item_type', type=str,
                      help='The category to which the products belongs',
                      required=True)
api_args.add_argument('item_mrp', type=float,
                      help='Maximum Retail Price (list price) of the products',
                      required=True)
api_args.add_argument('years_established', type=int,
                      help='The year in which store was established',
                      required=True)
api_args.add_argument('outlet_size', type=str,
                      help='The size of the store in terms of ground area covered',
                      required=True)
api_args.add_argument('outlet_location_type', type=str,
                      help='The type of city in which the store is located',
                      required=True)
api_args.add_argument('outlet_type', type=str,
                      help='Whether the outlet is just a grocery store or some sort of \
                      supermarket',
                      required=True)


class Predict(Resource):
    def post(self):
        args = api_args.parse_args()
        predict = predict_model(
            args['item_weight'],
            args['item_fat_content'],
            args['item_visibility'],
            args['item_type'],
            args['item_mrp'],
            args['years_established'],
            args['outlet_size'],
            args['outlet_location_type'],
            args['outlet_type']
        )
        return {'predict': round(float(predict), 2)}, 201


api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run()
