# API Gateway (listen port 80)

Restaurant Service 

- GET /store_api/stores : 

> To get all the restaurant information , include `store_id` and `store_name` 

```bash
curl localhost:80/store_api/stores
```

- GET /store_api/stores/<store_id> : 

> To get specified restaurant information , include `store_id` and `store_name` 

```bash
curl localhost:80/store_api/stores/a123
```

- POST /store_api/stores : 

> To create a new restaurant information 

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{
        "store_id": "f147",
        "store_name": "freddy fazbear pizza"
    }' \
    localhost:80/store_api/stores
```
- PUT /store_api/stores/<store_id> : 

> To update the restaurant information , include `store_name`

```bash
curl -X PUT -H "Content-Type: application/json" \
    -d '{
        "store_name": "Airplane Dish"
    }' \
    localhost:80/store_api/stores/a123
```
- DELETE /store_api/stores/<store_id>

> To delete the restaurant information

```bash
curl -X DELETE localhost:80/store_api/stores/a123
```


