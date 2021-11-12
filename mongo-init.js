db.auth('comp3122', '12345')

db = db.getSiblingDB('user_account')

db.createCollection('user');
db.customer.insertOne({'username':'wonderpp', 'firstname':'andrew', 'lastname':'ying', 'location':'polyU', 'credit_no':'20053025', 
'password':'123456789', 'role':'customer'});
db.customer.insertOne({'username':'hahamen', 'firstname':'joe', 'lastname':'chan', 'location':'home', 'credit_no':'2532532523', 
'password':'werrrtwerrt', 'role':'customer'});
db.customer.insertOne({'username':'yoholl', 'firstname':'jack', 'lastname':'wong', 'location':'Central', 'credit_no':'6436365326532', 
'password':'opop12345', 'role':'customer'});
db.customer.insertOne({'username':'bilebara', 'firstname':'Alton', 'lastname':'Tai', 'location':'Hung Hom', 'credit_no':'011224242445', 
'password':'qazplm2389', 'role':'customer'});
db.customer.insertOne({'username':'wword555', 'firstname':'Law', 'lastname':'Lo', 'location':'Earth', 'credit_no':'13143124135315', 
'password':'kkk5000', 'role':'customer'});
db.customer.insertOne({'username':'admin1', 'firstname':'admin1', 'lastname':'admin1', 'location':'admin1', 'credit_no':'1', 
'password':'admin1', 'role':'admin'});
db.customer.insertOne({'username':'admin2', 'firstname':'admin2', 'lastname':'admin2', 'location':'admin2', 'credit_no':'2', 
'password':'admin2', 'role':'admin'});


db = db.getSiblingDB('order_service')

db.createCollection('cart');
db.cart.insertOne({'entity_id':'1', 'customer_id':'432', 'product_ids':[1, 5, 7, 5]});
db.cart.insertOne({'entity_id':'2', 'customer_id':'658', 'product_ids':[5]});
db.cart.insertOne({'entity_id':'12', 'customer_id':'999', 'product_ids':[7, 9]});

db.createCollection('order');
db.order.insertOne({'entity_id':'1', 'cart_id':'44', 'status':'billing'});
db.order.insertOne({'entity_id':'2', 'cart_id':'78', 'status':'shipping.'});
db.order.insertOne({'entity_id':'3', 'cart_id':'12', 'status':'shipping'});