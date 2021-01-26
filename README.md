# Regression Bigmart Sales DeepLearning

Hello everyone, iam make machine learning to predict **Item Outlet Sales** for **Bigmart Sales DeepLearning**. Iam use `Python` and some library to make this machine learning. You can try this model in this website [Bigmart Sales](www.google.com). Iam deploy this model use `FLASK Restful-API` in `Heroku`.  
_Note: The response API took too long, be patient please_

---

## Tutorial Install Model

1. First you must have install `Python` and `Python Package Index` in your computer
2. After that, open directory [deploy_ml](./deploy_ml/) in your terminal
3. You can use virtual environments, if you want
4. Type in your terminal `pip install -r requirements.txt -y` and wait untill done
5. After that, type in your terminal `python app.py`

---

## Tutorial Use API

Connect in [Bigmart Sales Api](https://bigmartsalesapi.herokuapp.com/) and use `POST METHOD`. Send data:

1. `item_weight` Weight of product
2. `item_fat_content` Whether the product is low fat or not  
   **Use This Options**
   - Regular
   - Low Fat
3. `item_visibility`: The % of total display area of all products in a store allocated to the particular product
4. `item_type` The category to which the products belongs  
   **Use This Options**
   - Dairy
   - Soft Drinks
   - Meat
   - Fruits and Vegetables
   - Household
   - Baking Goods
   - Snack Foods
   - Frozen Foods
   - Breakfast
   - Healh and Hygiene
   - Hard Drinks
   - Canned
   - Breads
   - Starchy Foods
   - Seafood
   - Others
5. `item_mrp` Maximum Retail Price (list price) of the products
6. `years_established` The year in which store was established
7. `outlet_size` The size of the store in terms of ground area covered  
   **Use This Options**
   - Small
   - Medium
   - High
8. `outlet_location_type` The type of city in which the store is located  
   **Use This Options**
   - Tier 1
   - Tier 2
   - Tier 3
9. `outlet_type` Whether the outlet is just a grocery store or some sort of supermarket  
   **Use This Options**
   - Grocery Store
   - Supermarket Type 1
   - Supermarket Type 2
   - Supermarket Type 3

---

## Screenshots

- **Homepage**

![Index](./screenshots/index.png 'Homepage')

- **Predict Appear**

![Predict](./screenshots/after_predict.png 'Predict Appear')

---

### License

[MIT](./LICENSE)

### Changelog

- **1.0 Regression Bigmart Sales DeepLearning Release**

© Developed by [hafidh561](https://github.com/hafidh561).
