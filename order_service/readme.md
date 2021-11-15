# API Gateway (listen port 80)

Order Service 

- GET /order_api/orders : 

> To get all the restaurant menu information, include `order_id` , `store_id` , `username` , `menu` , `drinks` , 
> `status` and `order_time`

```bash
curl localhost:80/order_api/orders
```

- GET /order_api/orders/<order_id> : 

> To get specified restaurant menu information ,  include `order_id` , `store_id` , `username` , `menu` , `drinks` , 
> `status` and `order_time`
```bash
curl localhost:80/order_api/orders/1
```

- POST /order_api/orders: 

> To create a new order

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
        "store_id": "c789",
        "username": "bilebara"
    }' \
    localhost:80/order_api/orders
```
- PUT /order_api/orders/<order_id> : 

> To update the order information , include `menu` , `drinks`
> and a `update_time` field will be added 
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
    localhost:80/order_api/orders/4
```
- PATCH /order_api/orders/<order_id> : 

> To update the order status , which can change as `unpaid` , `shipping` , `delivered` and `canceled`
> and a `update_time` field will be added 
```bash
curl -X PATCH -H "Content-Type: application/json" \
    -d '{
        "status": "delivered"
    }' \
    localhost:80/order_api/orders/5
```

- DELETE /order_api/orders/<store_id>

> To delete the order record

```bash
curl -X DELETE localhost:80/order_api/orders/2
```


