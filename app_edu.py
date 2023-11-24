import pandas as pd
import streamlit as st


def run_edu_app():
    st.title('인천광역시 의료기관 현황')
    st.subheader('데이터')
    df=pd.read_csv('./data/incheon.csv',index_col=0, encoding='cp949')
    df=df.drop('Unnamed: 8',axis=1)
    df=df.dropna()
    st.dataframe(df)

    gang=df['군구명']=='강화군'
    ounm=df['군구명']=='옹진군'
    joun=df['군구명']=='중구'
    dong=df['군구명']=='동구'
    mechu=df['군구명']=='미추홀구'
    unesu=df['군구명']=='연수구'
    namdong=df['군구명']=='남동구'
    bupang=df['군구명']=='부평구'
    gaeyuan=df['군구명']=='계양구'
    sugu=df['군구명']=='서구'
    
    local=['강화군','옹진군','중구','동구','미추홀구','연수구','남동구','부평구','계양구','서구']
    
    st.text('군구명을 선택하시오.')
    if st.checkbox('강화군'):
        st.dataframe(df.loc[gang,])
    if st.checkbox('옹진군'):
        st.dataframe(df.loc[ounm,])