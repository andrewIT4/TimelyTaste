db.auth('comp3122', '12345')
db = db.getSiblingDB('order_db')
db.createCollection('order');

db.order.insertOne({
    "order_id" : 1,
    "username" : "wonderpp",
    "store_id" : "a123",
    "status" : "delivered",
    "menu": [
        {
            "menu_id": 1,
            "food_name": "Chicken & Egg Burger",
            "price": 15
        }
    ],
    "drinks":[
        {
            "drink_id": 1,
            "drink_name": "Orange Juice",
            "extra_charge": 0
        }
    ],
    "order_time" : new Date().toLocaleString()
});
db.order.insertOne({
    "order_id" : 2,
    "username" : "hahamen",
    "store_id" : "a123",
    "status" : "delivered",
    "menu": [
        {
            "menu_id": 2,
            "food_name": "Chicken Filet",
            "price": 14
        }
    ],
    "drinks":[
        {
            "drink_id": 2,
            "drink_name": "Pepsi Cola",
            "extra_charge": 0
        }
    ],
    "order_time" : new Date().toLocaleString()
});
db.order.insertOne({
    "order_id" : 3,
    "store_id" : "a123"  ,
    "username" : "yoholl",
    "status" : "shipping",
    "menu": [
        {
            "menu_id": 1,
            "food_name": "Chicken & Egg Burger",
            "price": 15
        },
        {
            "menu_id": 3,
            "food_name": "Double CheeseBurger",
            "price": 16
        }
    ],
    "drinks":[
        {
            "drink_id": 1,
            "drink_name": "Orange Juice",
            "extra_charge": 0
        },
        {
            "drink_id": 4,
            "drink_name": "Lemon Tea (Cold)",
            "extra_charge": 3
        }
    ],
    "order_time" : new Date().toLocaleString()
});
db.order.insertOne({
    "order_id" : 4,
    "username" : "bilebara",
    "store_id" : "b456",
    "status" : "cancelled",
    "menu": [
        {
            "menu_id": 1,
            "food_name": "Chinese fried rice",
            "price": 38
        },
        {
            "menu_id": 2,
            "food_name": "Scrambled Eggs with BBQ Pork",
            "price": 38
        }
    ],
    "drinks":[
        {
            "drink_id": 2,
            "drink_name": "Coca Cola",
            "extra_charge": 0
        },
        {
            "drink_id": 3,
            "drink_name": "Lemon Tea",
            "extra_charge": 0
        }
    ],
    "order_time" : new Date().toLocaleString()
});
db.order.insertOne({
    "order_id" : 5,
    "username" : "wword555",
    "store_id" : "b456",
    "status" : "unpaid",
    "menu": [
        {
            "menu_id": 2,
            "food_name": "Scrambled Eggs with BBQ Pork",
            "price": 38
        },
        {
            "menu_id": 3,
            "food_name": "Satay Beef Noodle",
            "price": 32
        }
    ],
    "drinks":[
        {
            "drink_id": 4,
            "drink_name": "Lemon Tea (Cold)",
            "extra_charge": 3
        }
    ],
    "order_time" : new Date().toLocaleString()
});