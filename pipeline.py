import tensorflow as tf 
import pandas as pd 
import numpy as np

import models

model = models.get_model()
model.load_weights('model-training/final_model.h5')

product_details = pd.read_csv('model-training/product_details.csv')

def get_recommendation(user_id, page_views, session_time, products=product_details, model=model):
    products = products.copy()
    user_ids = [user_id] * len(products)
    page_views = [page_views] * len(products)
    session_time = [session_time] * len(products)

    input_ = pd.DataFrame({'product_id': list(products.product_id), 
                           'user_id': user_ids,
                           'page_views': page_views,
                           'session_time': session_time,
                           'price': list(products.price),
                           'category_id': list(products.category_id)})
    
    results = model([input_['product_id'], 
                     input_['user_id'],
                     input_['page_views'].values.reshape(-1, 1),
                     input_['session_time'].values.reshape(-1, 1),
                     input_['price'].values.reshape(-1, 1),
                     input_['category_id']
                    ]).numpy().reshape(-1)
    
    products['purchase_proba'] = pd.Series(results, index=products.index)
    products = products.sort_values('purchase_proba', ascending=False)
    
    return products