product_a ={
    "name": "Value A",
    "price": 100,
    "stock":20
}

product_b ={
    "name": "Value B",
    "price": 200,
    "stock":15
}

product_c ={
    "name": "Value C",
    "price": 150,
    "stock":30
}

product_d ={
    "name": "Value D",
    "price": 80,
    "stock": 50
}

products = [
    product_a,
    product_b,
    product_c,
    product_d
]
"""
for product in products:
    print (f"产品名称: {product['name']}, 单价 :{product['price']},  库存 :{product['stock']}")

for product in products:
    if product['price'] >=120:
         print (f"产品名称: {product['name']}, 单价 :{product['price']}")
"""

total_stock =0
for product in products:
    total_stock = total_stock+ product["stock"]
print(f"库存总量为：{total_stock}")

for product in products:
    if product['stock'] <20:
         print (f"产品名称: {product['name']}, 库存 :{product['stock']}")

total_number=0
for product in products:
    total_number = total_number+1
print(f"产品数量为：{total_number}")

print(len(products))

name_stock=products[0]['name']
max_stock=products[0]['stock']
for product in products:
    if max_stock<product['stock']:
        max_stock=product["stock"]
        name_stock=product["name"]
print(f"库存最多：{name_stock},\n库存数量：{max_stock}")
# \n在这里依旧是换行符 max_stock=products[0]['stock']代表第一个元素的stock