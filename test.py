print(None is None)
print([]== [])
print(bool({}))
print(bool(None))

"""
# ========================
# Day 11 ：测试区域
# ========================
print ("测试1:空库存总列表")
result = calculate_total_stock([])
print ("实际结果:",result)
print ("预期结果: 0")

print("测试2: 空列表总货值")
result = calculate_total_value([])
print ("实际结果:",result)
print ("预期结果: 0")

print("测试3: 空列表综合统计")
result = build_inventory_summary([])
print ("实际结果:",result)

print("测试4: 空列表查找产品")
result = find_product_by_name([],"Valve A")
print ("实际结果:",result)
print ("预期结果: None")

print("测试5: 空列表组合筛选")
result = filter_products([],10,100)
print ("实际结果:",result)
print ("预期结果: []")

print("测试6: None产品展示")
result = show_single_product(None)

print("测试7: 空列表Csv导出")
result = export_products_to_csv([],"test_empty.csv")

"""