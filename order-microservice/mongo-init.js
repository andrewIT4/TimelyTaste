db.auth('comp3122', '12345')
db = db.getSiblingDB('order_service')


db.createCollection('cart');

db.cart.insertOne({'entity_id':'1', 'customer_id':'432', 'product_ids':[1, 5, 7, 5]});
db.cart.insertOne({'entity_id':'2', 'customer_id':'658', 'product_ids':[5]});
db.cart.insertOne({'entity_id':'12', 'customer_id':'999', 'product_ids':[7, 9]});

db.createCollection('order');

db.order.insertOne({'entity_id':'1', 'cart_id':'44', 'status':'billing'});
db.order.insertOne({'entity_id':'2', 'cart_id':'78', 'status':'shipping.'});
db.order.insertOne({'entity_id':'3', 'cart_id':'12', 'status':'shipping'});
