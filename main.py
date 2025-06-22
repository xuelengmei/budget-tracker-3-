import streamlit as st
from database import init_db, register_user, validate_login

init_db()

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if st.session_state.logged_in_user:
    st.success(f"欢迎回来，{st.session_state.logged_in_user}！🎉")

    if st.button("退出登录"):
        st.session_state.logged_in_user = None
        st.rerun()

else:
    st.title("用户登录")
    username = st.text_input("用户名", key="login_user")
    password = st.text_input("密码", type="password", key="login_pass")

    if st.button("登录"):
        if validate_login(username, password):
            st.session_state.logged_in_user = username
            st.success("登录成功！")
            st.rerun()
        else:
            st.error("用户名或密码错误")

    st.markdown("---")
    st.subheader("没有账号？注册一个：")

    new_username = st.text_input("新用户名", key="register_user")
    new_password = st.text_input("新密码", type="password", key="register_pass")

    if st.button("注册"):
        if register_user(new_username, new_password):
            st.success("注册成功！请返回上方登录")
        else:
            st.warning("用户名已存在，请换一个")
