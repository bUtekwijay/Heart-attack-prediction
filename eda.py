import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Title and Introduction
    st.title('Exploratory Data Analysis (EDA) - Heart Disease Prediction')

    st.image('https://heartology.id/_next/image/?url=https%3A%2F%2Fheartology-bucket.s3.ap-southeast-1.amazonaws.com%2F1907%2Fheartology-cardiovascular-hospital-blog-waspadai-serangan-jantung-fi-1920-1080.jpg&w=2048&q=75')


    st.write('# Introduction')
    '''
    Cardiovascular disease remains among the primary causes of mortality in Indonesia. This condition can progress silently, often manifesting only at critical stages. 
    As such, early risk detection is essential for preventing complications and enhancing patient outcomes. However, accurate risk assessment frequently proves challenging in the absence of comprehensive medical data.
    '''
    st.markdown('''
    Cardiovascular disease remains among the primary causes of mortality in Indonesia. This condition can progress silently, often manifesting only at critical stages. 
    As such, early risk detection is essential for preventing complications and enhancing patient outcomes. However, accurate risk assessment frequently proves challenging in the absence of comprehensive medical data.
    ''')

    # Load the dataset
    data = pd.read_csv('heart.csv')

    # Display the dataset
    st.header('Dataset Overview')
    st.write(data.head())

    # Visualizations
    st.subheader('Distribution of Age')
    fig1, ax1 = plt.subplots()
    sns.histplot(data['Age'], kde=True, bins=20, ax=ax1)
    ax1.set_title('Age Distribution')
    st.pyplot(fig1)
    st.markdown("""**Insight**: Most patients are between 40 and 70 years old, with the highest risk observed around age 55. The dataset covers ages ranging from 30 to 80.""")

    st.subheader('Distribution of Cholesterol Levels')
    fig2, ax2 = plt.subplots()
    sns.histplot(data['Cholesterol'], kde=True, bins=20, color='red', edgecolor='black', alpha=0.7, ax=ax2)
    ax2.set_title('Cholesterol Distribution')
    st.pyplot(fig2)
    st.markdown("""**Insight**: Most cholesterol levels fall between 100 and 400 mg/dL. Values near 0 may represent missing or invalid data.""")

    st.subheader('Gender Distribution')
    fig3, ax3 = plt.subplots()
    data['Sex'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['blue', 'magenta'], ax=ax3)
    ax3.set_ylabel('')
    ax3.set_title('Gender Distribution')
    st.pyplot(fig3)
    st.markdown("""**Insight**: Approximately 79% of the patients are male, while 21% are female. This suggests that heart disease may be more common in males in this dataset.""")

    st.subheader('Chest Pain Type Distribution')
    fig4, ax4 = plt.subplots()
    data['ChestPainType'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue', 'purple'], ax=ax4)
    ax4.set_ylabel('')
    ax4.set_title('Chest Pain Type Distribution')
    st.pyplot(fig4)
    st.markdown("""**Insight**: Asymptomatic chest pain (54%) is the most common, followed by Non-Anginal Pain (22%), Atypical Angina (19%), and Typical Angina (5%).""")

    st.subheader('Resting Blood Pressure Distribution')
    fig5, ax5 = plt.subplots()
    sns.histplot(data['RestingBP'], kde=True, color='orange', ax=ax5)
    ax5.set_title('Resting Blood Pressure Distribution')
    st.pyplot(fig5)
    st.markdown("""**Insight**: Resting blood pressure ranges from 100 to 200 mmHg, with values above 140 possibly indicating higher risk for heart issues.""")

if __name__ == '__main__':
    main()
