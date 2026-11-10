Python Inventory Management System

一个基于 Python 开发的简单库存管理系统，用于管理商品信息、查询库存、统计商品价值以及导出库存数据。

本项目是 Python 编程学习过程中的实战项目，主要用于练习 Python 基础语法、函数封装、列表与字典操作、异常处理、文件读写以及 Git 版本管理。

1. 项目简介（Introduction）

本项目实现了一个基于命令行交互的库存管理系统。

用户可以通过菜单选择不同的操作，对商品信息进行管理，并查看库存统计结果。

项目采用 Python 编写，目前使用列表和字典存储商品数据。

2. 功能介绍（Features）

目前实现的主要功能：

* 商品管理
    * 添加商品
    * 删除商品
    * 修改商品信息
    * 查询商品信息
* 库存查询
    * 查看全部商品
    * 根据商品名称进行搜索
    * 根据库存数量筛选商品
* 库存统计
    * 统计商品总库存
    * 计算商品总价值
    * 查询库存最高的商品
    * 根据商品库存进行排序
* 数据筛选
    * 根据最低库存数量筛选
    * 根据商品价值进行组合筛选
* 数据导出
    * 将库存数据导出为 CSV 文件
* 程序健壮性
    * 输入合法性检查
    * 异常处理
    * 空数据处理

3. 技术栈（Tech Stack）

技术	用途
Python	核心开发语言
List / Dictionary	商品数据存储
Functions	功能模块封装
CSV	数据导出
Git	版本管理

4. 项目结构（Project Structure）

ai-practice/
│
├── inventory_management.py   # 库存管理系统主程序
├── test.py                   # 测试程序
├── .gitignore                # Git 忽略配置
└── README.md                 # 项目说明文档

5. 运行环境（Requirements）

* Python 3.x
* Visual Studio Code（推荐）

本项目目前使用 Python 内置模块，不需要额外安装第三方依赖。

6. 如何运行（Getting Started）

Step 1：克隆项目

git clone 你的GitHub仓库地址

Step 2：进入项目目录

cd python-inventory-management

Step 3：运行程序

python inventory_management.py

程序启动后，根据命令行菜单提示输入对应数字，即可使用各项功能。

7. 学习收获（What I Learned）

通过本项目，我进一步练习和掌握了：

* Python 列表、字典等数据结构的使用
* 函数的定义、调用与返回值
* 条件判断与循环结构
* 异常处理与用户输入验证
* CSV 文件读写
* 代码重构与函数模块化
* 使用 Git 进行版本管理

8. 后续计划（Future Improvements）

后续计划继续完善项目：

* 使用 JSON 或数据库实现数据持久化
* 优化项目代码结构
* 增加更完善的自动化测试
* 增加图形化操作界面
* 尝试使用 AI 技术扩展库存管理功能

9. 作者说明（About）

这是一个个人 Python 实战学习项目，后续会持续更新和完善。