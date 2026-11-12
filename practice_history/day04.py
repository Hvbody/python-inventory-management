product_a ={
    "name" : "Valve A",
    "stock": 20,
    "price": 100
}

product_b ={
    "name": "Valve B",
    "price": 200,
    "stock":15
}

product_c ={
    "name": "Valve C",
    "price": 150,
    "stock":30
}

product_d ={
    "name": "Valve D",
    "price": 80,
    "stock": 50
}

products = [
    product_a,
    product_b,
    product_c,
    product_d
]


def show_products(products):
    for product in products:
        print(f"产品名称：{product['name']},单价：{product['price']},库存：{product['stock']}")

def calculate_tatal_stock(products):
    total_stock_a=0
    for product in products:
        total_stock_a=total_stock_a+product["stock"]
    return total_stock_a

def find_low_stock(products,threshold):
    for product in products:
        if product["stock"]<threshold:
            print(f"产品名称：{product['name']},库存：{product['stock']}---库存不足")

def find_max_stock_product(products):
    max_product=products[0]
    for product in products:
        if max_product["stock"]<product["stock"]:
            max_product=product
    print(f"库存最多产品：{max_product['name']},库存数量：{max_product['stock']}")
    return max_product

def show_high_price(products):
    for product in products:
        if product["price"]>=120:
            print(f"产品名称：{product['name']},单价：{product['price']}")

def calculate_total(products):
    total_stock=0
    total_number=0
    for product in products:
        total_number=total_number+1
        total_stock=total_stock+product["stock"]
    print(f"产品总数：{total_number},库存总量：{total_stock}")


def show_difference_stocklevel(products):
    for product in products:
        if product["stock"]<20:
            print(f"产品名称：{product['name']},库存等级：紧缺")
        elif product["stock"]>=20 and product["stock"]<=35:
            print(f"产品名称：{product['name']},库存等级：正常")
        else :
            print(f"产品名称：{product['name']},库存等级：充足") 

def calculate_total_price(products):
    total_pricestock=0
    for product in products:
        total_price = product["stock"]*product["price"]
        total_pricestock = total_pricestock +total_price
        print(f"产品名称：{product['name']},货物价值：{total_price}")
    print(f"货物总价值：{total_pricestock}")

"""
def search_name(products):
    searchna = input("输入产品名称：")
    found= False
    for product in products:
        if searchna == product["name"]:
            print(f"产品名称：{product['name']},单价：{product['price']},库存：{product['stock']}")
            found = True
            break
    if found == False:
        print(f"未能找到该产品")

"""

def find_product_by_name(products,search_name):
    for product in products:
        if search_name.lower() == product["name"].lower():
            return product
    return None

"""
.loewr() 全部转为小写
.upper() 全部转为大写
"""

def update_stock(products):
    search_name = input("输入产品名称：")
    res = find_product_by_name(products,search_name)
    if res is None:
        print(f"未能找到该产品")
    else:
        while True:
            number = input("输入新的库存数量：")
            try:
                num =int(number)
                if num >=0:
                    break
                else:
                    print(f"输入的是：{number}，这个是负数")
            except ValueError:
                print(f"输入的是：{number}，这个是不是合法数字")
        res["stock"] = num
    return res


    

text ="""=============库存管理系统=============
1.显示所有产品
2.显示高价产品
3.显示库存不足产品(库存<20)
4.显示库存总量和产品数量
5.显示库存最多的产品
6.库存分级
7.计算库存货值
8.按名称查找产品
9.修改库存
0.退出程序
=======================================
请输入你的选择： """

print(text)
while True:
    choice =input("请输入选项：") #可以写成 choice =input("请输入选项：").strip()
    choice= choice.strip()
    if choice == "1":
        show_products(products)
    elif choice== "2":
        show_high_price(products)
    elif choice == "3":
        find_low_stock(products,20)
    elif choice == "4":
        calculate_total(products)
    elif choice == "5":
        max_stock = find_max_stock_product(products)
    elif choice == "6":
        show_difference_stocklevel(products)
    elif choice == "7":
        calculate_total_price(products)
    elif choice == "8":
        search_name = input("输入产品名称：")
        res = find_product_by_name(products,search_name)
        if res is None:
            print(f"未能找到该产品")
        else:
            print(f"产品名称：{res['name']},单价：{res['price']},库存：{res['stock']}")
    elif choice == "9":
        res1=update_stock(products)
        """
        for product in products:
            if product["name"] == res1["name"]:
                product["stock"] = res1["stock"]
                print(f"产品名称：{product['name']},库存：{product['stock']}")
                #在一开始修改的就是字典里面的数据，不需要再次复制
                """
        show_products(products)
    elif choice =="":
        print(f"输入不能为空！")
    elif choice =="0":
        print(f"退出成功！")
        break
    else: print(f"无效选项，请重新输入")
