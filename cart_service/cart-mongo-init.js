db.auth('comp3122', '12345')
db = db.getSiblingDB('cart_service')

db.createCollection('cart');
db.cart.insertOne({'cart_id':'1', 'customer_id':'432', 'product_ids':['1', '5', '7', '5']});
db.cart.insertOne({'cart_id':'2', 'customer_id':'658', 'product_ids':['5']});
db.cart.insertOne({'cart_id':'12', 'customer_id':'999', 'product_ids':['7', '9']});

