import pandas as pd
import streamlit as st
from app_home import run_home_app
from app_edu import run_edu_app

menu=['home','edu','ml']

choice=st.sidebar.selectbox('메뉴',menu)

def main():
    if choice == menu[0]:
       run_home_app()
    if choice == menu[1]:
        run_edu_app()
    if choice == menu[2]:
        pass


if __name__ == '__main__':
    main()