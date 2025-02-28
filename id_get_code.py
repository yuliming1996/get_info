import streamlit as st
import pandas as pd

# 读取数据
data_file = "info.csv"  # CSV文件格式："姓名,身份证号,密码"
df = pd.read_csv(data_file)

st.title("获取密码")

name = st.text_input("姓名")
id_number = st.text_input("身份证号")

if st.button("查询"):
    user = df[(df["姓名"] == name) & (df["账号"] == id_number)]
    if not user.empty:
        password = user["密码"].values[0]
        st.success(f"密码：{password}")
    else:
        st.error("未找到匹配信息，请检查输入是否正确。")

