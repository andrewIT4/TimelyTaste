db.auth('comp3122', '12345')
db = db.getSiblingDB('menu_db')
db.createCollection('menu');

db.menu.insertOne({
    "store_id": "a123",
    "menus":[
        {
            "menu_id": 1,
            "food_name": "Chicken & Egg Burger",
            "price": 15
        },
        {
            "menu_id": 2,
            "food_name": "Chicken Filet",
            "price": 14
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
            "drink_id": 2,
            "drink_name": "Pepsi Cola",
            "extra_charge": 0
        },
        {
            "drink_id": 3,
            "drink_name": "Lemon Tea",
            "extra_charge": 0
        },
        {
            "drink_id": 4,
            "drink_name": "Lemon Tea (Cold)",
            "extra_charge": 3
        }
    ]

});
db.menu.insertOne({
    "store_id": "b456",
    "menus":[
        {
            "menu_id": 1,
            "food_name": "Chinese fried rice",
            "price": 38
        },
        {
            "menu_id": 2,
            "food_name": "Scrambled Eggs with BBQ Pork",
            "price": 38
        },
        {
            "menu_id": 3,
            "food_name": "Satay Beef Noodle",
            "price": 32
        },
    ],
    "drinks":[
        {
            "drink_id": 1,
            "drink_name": "Coffee",
            "extra_charge": 0
        },
        {
            "drink_id": 2,
            "drink_name": "Coca Cola",
            "extra_charge": 0
        },
        {
            "drink_id": 3,
            "drink_name": "Lemon Tea",
            "extra_charge": 0
        },
        {
            "drink_id": 4,
            "drink_name": "Lemon Tea (Cold)",
            "extra_charge": 3
        }
    ]
});
db.menu.insertOne({
    "store_id": "c789",
    "menus":[
        {
            "menu_id": 1,
            "food_name": "Har Gow",
            "price": 20
        },
        {
            "menu_id": 2,
            "food_name": "Pork Siu Mai",
            "price": 20
        },
        {
            "menu_id": 3,
            "food_name": "Sweet Tofu",
            "price": 16
        },
    ],
    "drinks":[
        {
            "drink_id": 1,
            "drink_name": "Scented Tea",
            "extra_charge": 10
        },
        {
            "drink_id": 2,
            "drink_name": "Tieguanyin",
            "extra_charge": 12
        },
        {
            "drink_id": 3,
            "drink_name": "Sowmee Tea",
            "extra_charge": 11
        }
    ]
});
