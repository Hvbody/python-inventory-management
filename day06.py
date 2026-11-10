import csv

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
    if len(products)==0:
        print("当前没有产品,无法查找库存最大值")
        return None
    max_product=products[0]
    for product in products:
        if max_product["stock"]<product["stock"]:
            max_product=product
    return max_product

def show_high_price(products):
    for product in products:
        if product["price"]>=120:
            print(f"产品名称：{product['name']},单价：{product['price']}")

def show_difference_stocklevel(products):
    for product in products:
        if product["stock"]<20:
            print(f"产品名称：{product['name']},库存等级：紧缺")
        elif product["stock"]>=20 and product["stock"]<=35:
            print(f"产品名称：{product['name']},库存等级：正常")
        else :
            print(f"产品名称：{product['name']},库存等级：充足") 

#新增计算总价值的算法            
def calculate_total_value(products):
    total_value = 0
    for product in products:
        total_pricestock= get_product_value(product)
        total_value = total_pricestock +total_value
    return total_value


def show_total_price(products):
    total_pricestock=0
    for product in products:
        total_price = get_product_value(product)
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
        return None
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
    while True:
        product_name = input("输入新产品的名字：").strip()
        if product_name == "break":
            break
        elif product_name == "":
            print("输入新的名字不能为空,若不新增请输入break")
            continue
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
                        if stock <0:
                            print("库存必须不小于0,请重新输入")
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
                print("新增加的产品：")
                show_single_product(new_product)
                break
            else :
                print("输入的产品名称已经存在,请输入新名称,若退出输入break")
                continue

def show_single_product(res):
    if res is None:
        print(f"没有可以展示的产品")
        return  
    else:  
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
"""
def inventory_report(products):
    print("库存综合报告：")
    show_statistics(products)
    show_total_price(products)
    max_stock =  find_max_stock_product(products)
    max_value =  find_max_price_product(products)
"""
def inventory_report(products):
    print("库存综合报告：")
    new_prouduct = build_inventory_summary(products)
    for i,j in new_prouduct.items():
        print(f"{i} : {j}")
    
#寻找最大价值
def find_max_price_product(products):
    if len(products)==0:
        return None
    max_product=products[0]
    for product in products:
        if get_product_value(max_product)<get_product_value(product):
            max_product=product
    return max_product


#day09--新增组合筛选功能
def filter_products(products,min_stock,min_value):
    leg_products = [ ]
    for product in products:
        if product["stock"] >= min_stock :
            if get_product_value(product) >= min_value:
                leg_products.append(product)
    return leg_products

#day10任务1：建立统一的统计数据函数，未解决返回值None的问题
def build_inventory_summary(products):
    product_count = len(products)
    total_stock  = calculate_total_stock(products)
    if product_count ==0:
        average_stock=0
    else:
        average_stock = total_stock / product_count
    total_value = calculate_total_value(products)
    max_stock_product = find_max_stock_product(products)
    max_value_product = find_max_price_product(products)
    new_static_product = {
        "product_count" : product_count,
        "total_stock" :total_stock,
        "average_stock" : average_stock,
        "total_value": total_value,
        "max_stock_product": max_stock_product,
        "max_value_product" : max_value_product
    }
    return new_static_product


def export_products_to_csv(products,filename):
    try :
        with open(filename,"w",newline="",encoding="utf-8-sig") as file:
            writer =csv.writer(file)
            writer.writerow(["name","price","stock","value"])
            for product in products:
                value = get_product_value(product)
                writer.writerow([
                    product["name"],
                    product["price"],
                    product["stock"],
                    value
                ])
        print(f"成功导出{len(products)}条产品数据到{filename}")
    except OSError as e:
        print(f"文件导出失败：{e}") 

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
13.生成综合库存分析报告
14.组合筛选产品
15.生成CSV的报告
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
        if max_stock is not None:
            print(f"库存最多产品：{max_stock['name']},库存数量：{max_stock['stock']}")
        else :
             print("当前没有产品,无法查找库存最高价值")
    elif choice == "6":
        show_difference_stocklevel(products)
    elif choice == "7":
        show_total_price(products)
    elif choice == "8":
        search_name = input("输入产品名称：")
        res = find_product_by_name(products,search_name)
        if res is None:
            print(f"未能找到该产品")
        else:
            show_single_product(res)
    elif choice == "9":
        res1=update_stock(products)
        if res1 is not None:
            show_single_product(res1)
    elif choice == "10":
        Add_product(products)

    elif choice == "11":
        delete_product(products)
    elif choice == "12":
        sort_products_by_value(products)
    elif choice == "13":
        inventory_report(products)
    elif choice == "14":
        while True:
            try:
                min_stock = int(input("输入最低库存："))                    
                if min_stock <0:
                    print("库存必须是非负整数,请重新输入")
                    continue
                break
            except ValueError:
                print("输入错误，请输入数字")
        while True:
            try:
                min_value = float(input("输入最低价值："))                    
                if min_value <0:
                    print("价值必须不能小于0,请重新输入")
                    continue
                break
            except ValueError:
                print("输入错误，请输入数字")
        products_filter =filter_products(products,min_stock,min_value)
        if len(products_filter) !=0:
            show_products(products_filter)
        else :
            print(f"没有符合条件的产品")
    elif choice == "15":
        while True:
            filename = input("请输入文件名：").strip()
            if filename == "":
                print(f"文件名输入不能为空！")  
                continue
            break
        if not filename.lower().endswith(".csv"):
            filename +=".csv"
        export_products_to_csv(products,filename)

    elif choice =="":
        print(f"输入不能为空！")
    elif choice =="0":
        print(f"退出成功！")
        break
    else: print(f"无效选项，请重新输入")


#测试使用
#export_products_to_csv(products,"inventory_export.csv")