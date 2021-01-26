import tensorflow as tf
import pandas as pd
import pickle
import datetime


def predict_model(item_weight, item_fat_content,
                  item_visibility, item_type,
                  item_mrp, years_established,
                  outlet_size, outlet_location_type,
                  outlet_type):
    # Load All Variable
    label_encoder_item_fat_content = pickle.load(
        open('./saved_model/label_encoder_item_fat_content.pickle', 'rb'))
    label_encoder_item_type = pickle.load(
        open('./saved_model/label_encoder_item_type.pickle', 'rb'))
    label_encoder_outlet_location_type = pickle.load(
        open('./saved_model/label_encoder_outlet_location_type.pickle', 'rb'))
    label_encoder_outlet_type = pickle.load(
        open('./saved_model/label_encoder_outlet_type.pickle', 'rb'))
    scaler = pickle.load(
        open('./saved_model/scaler.pickle', 'rb')
    )
    model = tf.keras.models.load_model('./saved_model/bigmart_sales_model.h5')
    now = datetime.datetime.now()

    # Make dataframe
    data = {
        'item_weight': [item_weight],
        'item_fat_content': [item_fat_content],
        'item_visibility': [item_visibility],
        'item_type': [item_type],
        'item_mrp': [item_mrp],
        'years_established': [years_established],
        'outlet_size': [outlet_size],
        'outlet_location_type': [outlet_location_type],
        'outlet_type': [outlet_type]
    }
    df = pd.DataFrame(data=data)
    
    # Preprocessing data
    df['item_fat_content'] = label_encoder_item_fat_content.transform(
        df['item_fat_content'])
    df['item_type'] = label_encoder_item_type.transform(df['item_type'])
    df['outlet_size'] = 0 if df['outlet_size'][0] == 'Small' else 1 if df['outlet_size'][0] == 'Medium' else 2
    df['outlet_location_type'] = label_encoder_outlet_location_type.transform(
        df['outlet_location_type'])
    df['outlet_type'] = label_encoder_outlet_type.transform(
        df['outlet_type'])
    df['years_established'] = now.year - int(df['years_established'])

    df = scaler.transform(df)
    predict = model.predict(df)

    return predict[0][0]
