import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def main():
    st.set_page_config(layout="wide")
    logo_url = 'title.jpg'
    st.sidebar.image(logo_url)
    with st.sidebar:
        choice = option_menu("Menu", ['유년기, 노년기 인구 변화','안양시 전체 등락', '안양시 유소년 시설 지도', '동별 노인 인구수','안양시 종합 지도'],
                            icons=['bi bi-people', 'bi bi-map', 'bi bi-backpack3', 'bi bi-graph-up-arrow', 'bi bi-globe-americas'],
                            menu_icon="bi bi-app-indicator", default_index=0,
                            styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        })
    st.sidebar.markdown("※모든 데이터는 2023년 이전을 기준으로 사용 되었습니다※")
    if choice == '동별 노인 인구수':
        st.header("안양시 동별 노인 인구수")
        st.divider()
        col1, col2 = st.columns(2)
        df = pd.read_csv('안양_65세이상_동별_2023.csv').iloc[:,1:]
        df2 = df.sort_values(by = '계', ascending = False).reset_index(drop = True)
        with col1:
            st.subheader("동별 노인 인구수 CSV")
            st.write(df2)
            st.divider()
        with col2:
            st.subheader("동별 노인 인구수 Bar Chart")
            fig = plt.figure(figsize = (15,10))
            plt.bar(df2['행정구역(동읍면)별'], df2['계'])
            plt.title('Anyang 65 years of age or older')
            plt.xticks(rotation = 45)
            st.pyplot(fig)
    elif choice == '유년기, 노년기 인구 변화':
        st.header("안양시 유년기, 노년기 인구 변화 비교")
        st.divider()
        col1, col2 = st.columns(2, gap = 'small')
        old = pd.read_csv('노년기.csv')
        young = pd.read_csv('유년기.csv')
        with col1:
            st.subheader(":blue[노년기]")
            st.write(old)
            st.divider()
            st.subheader(":red[유년기]")
            st.write(young)
        with col2:
            st.subheader("2014-2023 안양시 :red[유년기], :blue[노년기] 인구 변화")
            fig = plt.figure()
            plt.plot(old.index, old['합'], 'bo-', c = 'r', label = '노년기')
            plt.plot(old.index, young['합'], marker = '*', c = 'b', label = '유년기')
            plt.title('2014-2023 Anyang childhood(r) and old age(b)')
            plt.xticks(old.index)
            plt.legend()
            st.pyplot(fig) 

    elif choice == '안양시 전체 등락':
        st.header("안양시 인구 등락 정보")
        st.divider()
        col1, col2 = st.columns([4,6])
        with col1:
            st.subheader('동별 등락 그래프 2022 ~ 2023')
            updown = pd.read_csv('안양시_2022_2023_인구변화.csv').iloc[:,1:]
            col_li = ['tab:red' if i < 0 else 'tab:blue' for i in updown['change']]
            fig = plt.figure(figsize = (7,5))
            plt.bar(updown['행정구역(동읍면)별'], updown['change'], color = col_li)
            plt.xticks(range(len(updown.index)),fontsize = 7, rotation = 45)
            plt.axhline(y=0, color = 'black')
            st.pyplot(fig)
            st.divider()
            col3, col4 = st.columns(2)
            col3.metric('비산1동',int(updown[(updown['행정구역(동읍면)별'] == '비산1동')]['2023']), int(updown[(updown['행정구역(동읍면)별'] == '비산1동')]['change']))
            col4.metric('호계1동',int(updown[(updown['행정구역(동읍면)별'] == '호계1동')]['2023']), int(updown[(updown['행정구역(동읍면)별'] == '호계1동')]['change']))

        with col2:
            st.subheader('동별 등락 지도 2022 ~ 2023')
            path_to_html2 = "안양전체등락.html"

            with open(path_to_html2,'r',encoding='UTF-8') as g: 
                html_data2 = g.read()
            # Show in webpage
            html(html_data2, width=800, height=800)

    elif choice == '안양시 종합 지도':
        path_to_html = "안양나이대.html" 

        with open(path_to_html,'r',encoding='UTF-8') as f: 
            html_data = f.read()

        # Show in webpage
        st.header("안양시 종합 지도")
        st.divider()
        st.caption(':red[노인복지관] / :blue[치매안심센터]')
        html(html_data, width=1500, height=800)
    elif choice == '안양시 유소년 시설 지도':
        path_to_html3 = "young.html"
        with open(path_to_html3,'r',encoding='UTF-8') as h: 
            html_data3 = h.read()
        st.header("안양시 유소년 시설 지도")
        st.divider()
        html(html_data3, width=1500, height=800)
if __name__ == '__main__':
    main()
