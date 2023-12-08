import streamlit as st
import pandas as pd
import os
import random
import numpy as np
from st_on_hover_tabs import on_hover_tabs
from init import *
from login import *
from register import *
import warnings
# 경고 메시지 무시 설정
warnings.filterwarnings("ignore", message="I don't know how to infer vegalite type from 'empty'.*")

###############실행 방법################
#
#   command 창에 streamlit run 파일이름 --server.maxUploadSize 업로드 용량(MB)
#   실행을 원하는 파일이름을 적고 뒤에 업로드 용량을 적으셔야지 용량이 큰 파일도 업로드가 됩니다.
#   ex)
#   streamlit run main.py --server.maxUploadSize 2000
#   -> main.py를 실행하고 2GB의 데이터까지 업로드 할 수 있는 서버환경 구축됨
# 
#####################################

def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

def session_state_ck():
    for key, _ in st.session_state.items():
        if key == "initCk":
            return True
    return False

def run():
    
    seed_everything(42)
    st.set_page_config(layout="wide")

    if not session_state_ck():
        initSetting()

    st.header("가상화폐 자동매매 플랫폼")
    st.markdown('<style>' + open('../css/style.css').read() + '</style>', unsafe_allow_html=True)


    with st.sidebar:
        tabs = on_hover_tabs(tabName=["Home","회원가입","로그인&로그아웃", "모의 매매", "개인정보","데이터 가시화","제어게인 최적화","제어게인 최적화2","제어게인 최적화3"], 
                            iconName=["Home",'Load', 'Scaling', 'Modeling','Plot','Optimization','Optimization2','Optimization3'], default_choice=0)
    if tabs == "Home":
        pass
    elif tabs == "회원가입":
        register()

    elif tabs == "로그인&로그아웃":
        login()

    elif tabs == "기계학습 모델링":
        pass

    elif tabs == "데이터 가시화":
        pass

    elif tabs == "제어게인 최적화":
        pass

    elif tabs == "제어게인 최적화2":
        pass

    elif tabs == "제어게인 최적화3":
        pass

if __name__ == "__main__":
    run()