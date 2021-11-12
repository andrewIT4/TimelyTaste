db.auth('comp3122', '12345')
db = db.getSiblingDB('store_db')
db.createCollection('store');


db.store.insertOne({
    "store_id": "a123",
    "store_name": "Store ANT",
});
db.store.insertOne({
    "store_id": "b456",
    "store_name": "Store BEE",
});
db.store.insertOne({
    "store_id": "c789",
    "store_name": "Store CAT",
});
