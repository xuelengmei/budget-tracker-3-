# Streamlit 记账本项目 💰📊

这是一个基于 Streamlit + SQLite 的记账本应用，实现了：

- ✅ 用户注册 / 登录（数据持久化保存）
- ✅ 记账功能（支出、收入记录）
- ✅ 统计分析（按分类统计图表）
- ✅ 简洁直观的前端页面
- ✅ 导出为Excel功能

## 🌱 使用方式

### 1. 安装依赖（建议在虚拟环境中）：
pip install -r requirements.txt

### 2. 运行项目
streamlit run main.py

### 3. 文件结构说明

budget-tracker/
```
├── main.py               # 登录页
├── database.py           # 数据库逻辑
├── requirements.txt      # 依赖
├── README.md             # 项目说明
├── .gitignore            # 忽略文件配置
└── pages/
    ├── 记账.py
    └── 统计.py

```    
## 💡 功能细节

数据存储使用 SQLite (data.db)

会自动创建表，无需手动建库

适合学习、练手项目部署

新增导出为Excel功能

欢迎 star ⭐️ 或 fork 🍴！
