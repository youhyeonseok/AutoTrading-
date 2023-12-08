import streamlit as st
import time
import pandas as pd
import mplfinance as fplt

def homePage():
    # st.set_page_config(page_title="Plotting Demo", page_icon="📈")

    st.title("Open Automated Trading Platform Cobok")
    st.write(
        """Hello, this is Cobok, an open automated trading platform. 
        We are an AI-powered automated trading system that can provide 
        substantial profits without requiring you to have specialized 
        knowledge or actively manage investments. 
        For more details, please refer to the information section."""
    )
    initIdx = 100
    i = 0
    data = st.session_state["data"]
    data.index = pd.to_datetime(data.index)

    placeholder = st.empty()
    while True:
        new_rows = data.iloc[i:initIdx + i + 1]
        fig,ax = fplt.plot(
            new_rows,
            type='candle',
            style='charles',
            title='BitCoin Real Chart',
            ylabel='Price ($)',
            volume=True,
            figsize = (25,9),
            show_nontrading=True,
            returnfig = True
            )
        
        placeholder.empty()
        with placeholder.container():
            st.pyplot(fig)
            
        i += 1
        time.sleep(0.1)