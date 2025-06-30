# 💰📊 Streamlit 记账本项目

一个基于 **Streamlit + SQLite** 构建的简洁记账应用，适合快速部署与使用。

---

## ✨ 项目功能

- ✅ 用户注册 / 登录（数据持久化）
- ✅ 添加支出 / 收入记录
- ✅ 按月查看图表统计（饼图、柱状图、趋势图）
- ✅ 支持 Excel 导出数据
- ✅ 多页面结构（Streamlit Pages）
- ✅ UI 美化：同色系按钮样式、表格折叠、专属页脚

---

## 🚀 快速开始

### 1. 安装依赖（建议使用虚拟环境）

pip install -r requirements.txt

### 2. 启动项目

streamlit run main.py

## 📁 项目结构

```
budget-tracker/
├── main.py               # 登录页（主页）
├── database.py           # 数据库交互逻辑
├── requirements.txt      # 依赖清单
├── README.md             # 项目说明文件
├── .gitignore            # Git 忽略规则
└── pages/
    ├── 记账页.py           # 记账页面
    └── 统计页.py           # 数据分析页
```


## 💡 特色亮点

#### 📅 月份筛选：切换任意月份查看记录

#### 📈 图表分析：自动生成分类占比图、收支趋势图

#### 📥 Excel 导出：支持一键下载账单数据

#### 🎨 UI 优化：同色系设计、按钮美化、可折叠表格、页脚设计

## ⭐️ 欢迎交流

如果你喜欢这个项目，欢迎点个 ⭐️ star 或 fork 🍴！

#### 项目作者：@蔚之