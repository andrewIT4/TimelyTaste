db.auth('comp3122', '12345')
db = db.getSiblingDB('delivery_db')
db.createCollection('delivery');

db.delivery.insertOne({
    "delivery_id" : "1",
	"name": "jajaTang",
    "status": "free"
});
db.delivery.insertOne({
    "delivery_id" : "2",
	"name": "Tom Wong",
    "status": "busy"
});
db.delivery.insertOne({
    "delivery_id" : "3",
	"name": "Andy Lo",
    "status": "busy"
});
db.delivery.insertOne({
    "delivery_id" : "4",
	"name": "Bob Chan",
    "status": "free"
});
db.delivery.insertOne({
    "delivery_id" : "5",
	"name": "Anson Li",
    "status": "free"
});

