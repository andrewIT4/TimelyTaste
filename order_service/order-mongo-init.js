db.auth('comp3122', '12345')
db = db.getSiblingDB('order_service')

db.createCollection('order');
db.order.insertOne({'order_id':'1', 'cart_id':'44', 'status':'unbilled'});
db.order.insertOne({'order_id':'2', 'cart_id':'78', 'status':'billed.'});
db.order.insertOne({'order_id':'3', 'cart_id':'12', 'status':'shipping'});
db.order.insertOne({'order_id':'9', 'cart_id':'11', 'status':'delivered'});
