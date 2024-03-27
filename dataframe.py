# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # dataFrame으로 반환
    return df

def plot_matplotlib(): # streamlit  문법
    st.title("Categorical Bar Plot with Seaborn") # 대시보드 제목
    df = load_data() #데이터 불러오기 -> 데이터프레임 구조 변환
    fig, ax = plt.subplots() # 시각화
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs. lifeExp")
    
    st.pyplot(fig) # streamlit에 그리기

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')

    df = load_data()
    st.dataframe(df, use_container_width=True) # 대시보드에 표 삽입

    #pandas style- 두번째 표 
    st.title("Maximum value per column") 
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib() # 그래프 삽입    
    
if __name__ == "__main__":
    main()