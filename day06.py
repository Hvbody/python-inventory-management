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

def calculate_total_stock(products):
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
"""
def calculate_total(products):
    total_stock=0
    total_number=0
    for product in products:
        total_number=total_number+1
        total_stock=total_stock+product["stock"]
    print(f"产品总数：{total_number},库存总量：{total_stock}")
"""

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

def find_product_by_name(products,search_name):
    for product in products:
        if search_name.lower() == product["name"].lower():
            return product
    return None

#功能9的修改库存
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

#功能4的展示
def show_statistics(products):
    total_stock = calculate_total_stock(products)
    total_num = len(products)
    if total_num != 0:
        ave = total_stock / total_num
        print(f"产品总数：{total_num}\n库存总量:{total_stock}\n平均库存:{ave}")
    else:
        print(f"产品总数：{total_num},库存总量：{total_stock}")

#功能10新增库存产品
def Add_product(products):
    product_name = input("输入新产品的名字：").strip()
    if product_name == "":
        print("输入新的名字不能为空")
    else:
        res = find_product_by_name(products,product_name)
        if res is None:
            while True:
                try:
                    price = float(input("请输入单价："))
                    if price <=0:
                        print("单价必须大于0,请重新输入")
                        continue
                    break
                except ValueError:
                    print("输入错误，请输入数字")
            while True:
                try:
                    stock = int(input("请输入库存："))
                    if price <0:
                        print("库存必须大于0,请重新输入")
                        continue
                    break
                except ValueError:
                    print("输入错误，请输入数字")
            new_product = {
                "name"  : product_name,
                "price" : price,
                "stock" : stock
            }
            products.append(new_product)
        else :
            print("输入的产品名称已经存在")
def show_single_product(res):
     print(f"产品名称：{res['name']},单价：{res['price']},库存：{res['stock']}")

def delete_product(products):
    product_name = input("输入需要删除产品的名字：").strip()
    if product_name == "":
        print("输入新的名字不能为空")
    else:
        res = find_product_by_name(products,product_name)
        if res is None:
            print(f"未能找到该产品")
        else:
            products.remove(res)
            print(f"成功删除该产品")


#这个是库存产品价值排序的代码，要加强理解sorted
def get_product_value(product):
    return product["price"]*product["stock"]


def sort_products_by_value(products):
    sorted_products = sorted(products,
                             key=get_product_value,#这个是key是传入方法
                             reverse=True)

    for product in sorted_products:
        value = get_product_value(product)
        print(f"{product['name']}--库存货值：{value}")


text ="""=============库存管理系统=============
1.显示所有产品
2.显示高价产品
3.显示库存不足产品(库存<20)
4.显示库存总量、产品数量、平均库存
5.显示库存最多的产品
6.库存分级
7.计算库存货值
8.按名称查找产品
9.修改库存
10.新增库存产品
11.删除库存产品
12.产品价值排序
0.退出程序
======================================="""

#print(text)  菜单页面的输出放在循环里面
while True:
    print(text)
    choice =input("请输入选项：") 
    choice= choice.strip()
    if choice == "1":
        show_products(products)
    elif choice== "2":
        show_high_price(products)
    elif choice == "3":
        find_low_stock(products,20)
    elif choice == "4":
        show_statistics(products)
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
            show_single_product(res)
    elif choice == "9":
        res1=update_stock(products)
        show_single_product(res1)
    elif choice == "10":
        Add_product(products)

    elif choice == "11":
        delete_product(products)
    elif choice == "12":
        sort_products_by_value(products)
    elif choice =="":
        print(f"输入不能为空！")
    elif choice =="0":
        print(f"退出成功！")
        break
    else: print(f"无效选项，请重新输入")
