import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import elastic as elastic
import eland as ed

st.title("Kiva Loan Analysis")
st.markdown("Kiva.org is an online crowdfunding platform \
to extend financial services to poor and financially excluded people \
around the world. Kiva lenders have provided over $1 billion dollars \
in loans to over 2 million people. In order to set investment priorities, \
help inform lenders, and understand their target communities, knowing the level \
of poverty of each borrower is critical. However, this requires inference based on \
limited set of information for each borrower.")

use_input = st.sidebar.text_input("Enter use of Loans")

strategy = st.sidebar.selectbox("Select Analysis Strategy",
                 ('None','Loan Amount',
                 'Funded Amount',
                 'Sector',
                 'Activity',
                 'Country'),index = 0)

if (strategy == "Loan Amount") or (strategy == "Funded Amount"):
    num_bins = st.slider('Number of bins to display',0, 100, 10)
 
selected_country = st.sidebar.selectbox('Country',
('All','India', 'Kenya','Pakistan','Cambodia','El Salvador',
'Kyrgyzstan','Albania'))

selected_sector = st.sidebar.selectbox('Sector',('All','Food', 
'Transportation', 'Arts', 'Services', 'Agriculture',
'Manufacturing', 'Wholesale', 'Retail', 'Clothing', 'Construction',
'Health', 'Education', 'Personal Use', 'Housing', 'Entertainment'))

selected_gender = st.sidebar.selectbox('Gender',
('All','female', 'male'))

num_rows = st.sidebar.slider('Number of rows to display',0, 100, 10)

selected_columns =['activity',  'country',
       'borrower_genders',  'funded_amount',  'loan_amount',  'sector', 'tags',  'use']

def display_hist(data):
    fig = Figure()
    ax = fig.subplots()
    data = data.apply(lambda x : int(x))
    sns.histplot(data,ax=ax, kde=True,bins = num_bins)
    st.pyplot(fig)

    st.table(data.describe())

def display_barplot(data):
    data_group = data.value_counts().reset_index().head(10)
    some_values = [""]
    data_group = data_group.loc[~data_group['index'].isin(some_values)]
    st.table(data_group)
    

    fig = Figure()
    ax = fig.subplots()
    sns.barplot(x = data_group.iloc[:,1], 
    y = data_group['index'],
     color="goldenrod",ax = ax)
    st.pyplot(fig)

if selected_country == "All":
        elastickiva_ = elastic.get_df()
else:
    elastickiva_ = elastic.get_df()
    elastickiva_.df=elastickiva_.df[elastickiva_.df["country"].es_match(selected_country)]


if use_input == "":
        pass
else:
    elastickiva_.df=elastickiva_.df[elastickiva_.df["use"].es_match(use_input)]

if selected_gender == "All":
        pass
else:
    elastickiva_.df=elastickiva_.df[elastickiva_.df["borrower_genders"].es_match(selected_gender)]

if selected_sector == "All":
        pass
else:
    elastickiva_.df=elastickiva_.df[elastickiva_.df["sector"].es_match(selected_sector)]


if strategy == "Loan Amount":
    st.subheader("Loan Amount Analysis")    
    loan_df = ed.eland_to_pandas(elastickiva_.df["loan_amount"])    
    display_hist(loan_df)
    

elif strategy == "Funded Amount":
    st.subheader("Funded Amount Analysis")
    loan_df = ed.eland_to_pandas(elastickiva_.df["funded_amount"])
    display_hist(loan_df)

elif strategy == "Sector":
    st.subheader("Most popular sectors")
    barplot_df = ed.eland_to_pandas(elastickiva_.df["sector"])
    display_barplot(barplot_df)

elif strategy == "Activity":
    st.subheader("Most popular activity")
    barplot_df = ed.eland_to_pandas(elastickiva_.df["activity"])
    display_barplot(barplot_df)

elif strategy == "Country":
    st.subheader("Most loans given to countries")
    barplot_df = ed.eland_to_pandas(elastickiva_.df["country"])
    display_barplot(barplot_df)
else:
    df2 =(elastickiva_.df)[selected_columns].head(num_rows)
    st.dataframe(ed.eland_to_pandas(df2))


   

    
 

    
 
        



