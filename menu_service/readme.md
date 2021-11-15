# API Gateway (listen port 80)

Menu Service 

- GET /menu_api/menus : 

> To get all the restaurant menu information, include `store_id` , `menus` , `drinks`

```bash
curl localhost:80/menu_api/menus
```

- GET /menu_api/menus/<store_id> : 

> To get specified restaurant menu information , include `store_id` , `menus` , `drinks`

```bash
curl localhost:80/menu_api/menus/a123
```

- POST /menu_api/menus: 

> To create a new restaurant menu information 

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{
        "drinks": [
            {
                "drink_id": 1,
                "drink_name": "Scented Tea",
                "extra_charge": 10
            }
        ],
        "menus": [
            {
                "food_name": "Har Gow",
                "menu_id": 1,
                "price": 20
            }
        ],
        "store_id": "c789"
    }' \
    localhost:80/menu_api/menus
```
- PUT /menu_api/menus/<store_id> : 

> To update the restaurant information , include `menus` and `drinks`

```bash
curl -X PUT -H "Content-Type: application/json" \
    -d '{
        "drinks": [
            {
                "drink_id": 4,
                "drink_name": "Lemon Tea",
                "extra_charge": 10
            }
        ],
        "menus": [
            {
                "food_name": "Pizzeria Mozza",
                "menu_id": 1,
                "price": 60
            }
        ]
    }' \
    localhost:80/menu_api/menus/a123
```
- DELETE /menu_api/menus/<store_id>

> To delete the restaurant menu information

```bash
curl -X DELETE localhost:80/menu_api/menuss/a123
```


