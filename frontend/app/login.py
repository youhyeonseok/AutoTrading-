import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def login():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    # 로그인
    name, authentication_status, username = authenticator.login('Login', 'main')
    # 로그아웃 버튼
    if authentication_status:
        authenticator.logout('Logout', 'main', key='unique_key')
        st.write(f'Welcome *{name}*')
        # st.session_state["id"] = username
        # st.session_state["name"] = name
        # st.session_state["authentication_status"] = authentication_status

    elif authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

    if not authentication_status:
        col = st.columns(3)
        with col[0]:
            if st.button("아이디 찾기"):
                pass
        with col[1]:
            if st.button("비밀번호 찾기"):
                pass

    # # 비밀번호 재설정
    # if authentication_status:
    #     try:
    #         if authenticator.reset_password(username, 'Reset password'):
    #             st.success('Password modified successfully')
    #     except Exception as e:
    #         st.error(e)

    # 비밀번호 분실 위젯
    # try:
    #     username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    #     if username_forgot_pw:
    #         st.success('New password sent securely')
    #         # Random password to be transferred to the user securely
    #     else:
    #         st.error('Username not found')
    # except Exception as e:
    #     st.error(e)

    # if authentication_status:
    #     try:
    #         if authenticator.update_user_details(username, 'Update user details'):
    #             st.success('Entries updated successfully')
    #     except Exception as e:
    #         st.error(e)

    # with open('config.yaml', 'w') as file:
    #     yaml.dump(config, file, default_flow_style=False)