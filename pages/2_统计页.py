import streamlit as st
import pandas as pd
import altair as alt

# 页面配置和全局样式
st.set_page_config(page_title="📊 统计分析", page_icon="📈")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: "Microsoft YaHei", sans-serif;
    }
    .stButton>button {
        background-color: #00BFC4;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 16px;
        transition: 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #009ca6;
        transform: scale(1.02);
    }
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# 登录校验
if "logged_in_user" not in st.session_state or not st.session_state.logged_in_user:
    st.info("请先注册或登录后再使用此功能~")
    st.stop()

# 数据准备
records_dict = st.session_state.get("records", {})
records = records_dict.get(st.session_state.logged_in_user, [])

st.title("📊 账单统计分析")

if not records:
    st.info("暂无记录，快去添加记账信息吧！")
    st.stop()

df = pd.DataFrame(records, columns=["日期", "类型", "分类", "金额", "备注"])
df["日期"] = pd.to_datetime(df["日期"], errors="coerce")
df = df.dropna(subset=["日期"])
df["月份"] = df["日期"].dt.to_period("M").astype(str)

# 原始数据展示 + 下载
st.subheader("📋 全部记账数据")
df.index = df.index + 1
df.index.name = "序号"


if "show_full_table" not in st.session_state:
    st.session_state.show_full_table = False

if st.session_state.get("show_full_table", False):
    st.dataframe(df)
    if st.button("🔼 收起记录", key="collapse_btn"):
        st.session_state["show_full_table"] = False
        st.rerun()
else:
    st.dataframe(df.head(5))
    if len(df) > 5:
        if st.button("🔽 展开查看更多", key="expand_btn"):
            st.session_state["show_full_table"] = True
            st.rerun()
    else:
        st.caption("📌 当前记录较少，无需展开")



excel_file = "我的记账.xlsx"
df.to_excel(excel_file, index=False)

with open(excel_file, "rb") as f:
    st.download_button(
        label="📥 导出为 Excel 文件",
        data=f,
        file_name=excel_file,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# 月份选择
selected_month = st.selectbox("📆 选择月份", sorted(df["月份"].unique(), reverse=True))
df = df[df["月份"] == selected_month]

# 💰 收支比例图
with st.expander("💰 收支比例图", expanded=False):
    if not df.empty:
        total_by_type = df.groupby("类型")["金额"].sum().reset_index()

        pie_chart = alt.Chart(total_by_type).mark_arc(innerRadius=60, outerRadius=120).encode(
            theta=alt.Theta(field="金额", type="quantitative"),
            color=alt.Color(field="类型", type="nominal", scale=alt.Scale(scheme="set2")),
            tooltip=["类型", "金额"]
        ).properties(
            width=450,
            height=350,
            title="本月收支占比"
        ).configure_title(
            fontSize=18,
            anchor="middle"
        )
        st.altair_chart(pie_chart, use_container_width=True)
    else:
        st.warning("暂无数据，无法生成饼图，请先添加记录哦～")

# 📊 分类分布图
with st.expander("📊 分类分布图", expanded=False):
    selected_type = st.radio("选择查看类型", ["支出", "收入"], horizontal=True)
    filtered_df = df[df["类型"] == selected_type]
    if filtered_df.empty:
        st.info(f"该月没有 {selected_type} 的记录")
    else:
        category_sum = filtered_df.groupby("分类")["金额"].sum().reset_index()
        bar_chart = alt.Chart(category_sum).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
            x=alt.X("分类", sort="-y", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("金额", title="金额 (元)"),
            color=alt.Color("分类", scale=alt.Scale(scheme="pastel1")),
            tooltip=["分类", "金额"]
        ).properties(
            width=500,
            height=350,
            title=f"{selected_type} 分类统计"
        ).configure_title(
            fontSize=18,
            anchor="middle"
        )
        st.altair_chart(bar_chart, use_container_width=True)

# 📈 收入支出趋势图
with st.expander("📈 收入支出趋势图", expanded=False):
    df_recent = df[df["日期"] >= pd.Timestamp.now() - pd.Timedelta(days=30)]
    if df_recent.empty:
        st.info("近30天暂无记录，无法绘制趋势图~")
    else:
        trend = df_recent.groupby(["日期", "类型"])["金额"].sum().reset_index()
        line_chart = alt.Chart(trend).mark_line(point=alt.OverlayMarkDef(filled=True, size=60)).encode(
            x=alt.X("日期:T", axis=alt.Axis(title="日期")),
            y=alt.Y("金额:Q", axis=alt.Axis(title="金额 (元)")),
            color=alt.Color("类型:N", scale=alt.Scale(scheme="dark2")),
            tooltip=["日期", "类型", "金额"]
        ).properties(
            width=600,
            height=350,
            title="近30天收支趋势"
        ).configure_title(
            fontSize=18,
            anchor="middle"
        )
        st.altair_chart(line_chart, use_container_width=True)

# 页脚
st.markdown("""
<hr>
<div style="text-align: center; font-size: 14px;">
    🛠️ 项目由 <b>蔚之</b> 构建 ｜ <a href="https://github.com/xuelengmei/budget-tracker-3-" target="_blank">GitHub 源码</a>
</div>
""", unsafe_allow_html=True)
