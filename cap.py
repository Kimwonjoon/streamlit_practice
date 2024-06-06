import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def main():
    st.set_page_config(layout="wide")
    with st.sidebar:
        choice = option_menu("Menu", ['동별 노인 인구수','유년기, 노년기 인구 변화',
                                    '안양시 전체 등락','안양시 종합 지도'],
                            icons=['bi bi-graph-up-arrow', 'bi bi-people',
                                'bi bi-map', 'bi bi-globe-americas'],
                            menu_icon="bi bi-app-indicator", default_index=0,
                            styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        })
    if choice == '동별 노인 인구수':
        st.header("안양시 동별 노인 인구수")
        col1, col2 = st.columns(2)
        df = pd.read_csv('안양_65세이상_동별_2023.csv').iloc[:,1:]
        df2 = df.sort_values(by = '계', ascending = False).reset_index(drop = True)
        with col1:
            st.header("동별 노인 인구수 CSV")
            st.write(df2)
        with col2:
            st.header("동별 노인 인구수 Bar Chart")
            fig = plt.figure(figsize = (15,10))
            plt.bar(df2['행정구역(동읍면)별'], df2['계'])
            plt.title('안양시 동별 65세 이상 노인 인구수')
            plt.xticks(rotation = 45)
            st.pyplot(fig)
    elif choice == '유년기, 노년기 인구 변화':
        st.header("안양시 유년기, 노년기 인구 변화 비교")
        col1, col2 = st.columns(2)
        old = pd.read_csv('노년기.csv')
        young = pd.read_csv('유년기.csv')
        with col1:
            st.header("노년기")
            st.write(old)
            st.header("유년기")
            st.write(young)
        with col2:
            st.header("2014-2023 안양시 유년기, 노년기 인구 변화")
            fig = plt.figure()
            plt.plot(old.index, old['합'], 'bo-', c = 'r', label = '노년기')
            plt.plot(old.index, young['합'], marker = '*', c = 'b', label = '유년기')
            plt.title('2014-2023 안양시 유년기, 노년기 인구 변화')
            plt.xticks(old.index)
            plt.legend()
            st.pyplot(fig) 

    elif choice == '안양시 전체 등락':
        path_to_html2 = "안양전체등락.html"

        with open(path_to_html2,'r',encoding='UTF-8') as g: 
            html_data2 = g.read()

        # Show in webpage
        st.header("안양시 인구 등락 지도")
        html(html_data2, width=1600, height=800)

    elif choice == '안양시 종합 지도':

        path_to_html = "안양나이대.html" 

        with open(path_to_html,'r',encoding='UTF-8') as f: 
            html_data = f.read()

        # Show in webpage
        st.header("안양시 종합 지도")
        html(html_data, width=1600, height=800)
if __name__ == '__main__':
    main()