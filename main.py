import streamlit as st
import webbrowser
import pandas as pd
from streamlit_option_menu import option_menu
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost

Dataset = 'http://localhost:8502'
About = 'http://localhost:8503'
with st.sidebar:
    choice = option_menu(menu_title="Main Menu",
                         options=["Product Analysis","Dataset",  "About"],
                         icons=["link", "folder-symlink", "info-circle"],
                         menu_icon="cast",
                         default_index=0)

if choice == "Product Analysis":
    st.title("Product Review Sentiment Analysis")
    Data = pickle.load ( open ( 'Analysis.pkl', 'rb' ) )
    Analysis = pd.DataFrame ( Data )

    tab1, tab2 = st.tabs ( ["Product Type wise sentiment", "Description wise sentiment"] )
    with tab1 :
        st.subheader("All Products")
        hist = plt.figure ( figsize=(10, 4) )
        sns.histplot ( data=Analysis, x='Product_Type' )
        st.pyplot ( hist )

        Product_type = Analysis['Product_Type']
        product_options = st.selectbox('Select Product Type', Analysis['Product_Type'].unique())
        st.write("Product Type :", product_options)
        if product_options == '0':
            product_0 = Analysis [Analysis ['Product_Type'] == '0']
            st.write("Product Description", product_0)

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_0, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_0 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '1':
            product_1 = Analysis [Analysis ['Product_Type'] == '1']
            st.write ( "Product Description",product_1 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_1, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_1 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '2':
            product_2 = Analysis [Analysis ['Product_Type'] == '2']
            st.write ( "Product Description", product_2 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_2, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_2 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '3':
            product_3 = Analysis [Analysis ['Product_Type'] == '3']
            st.write ("Product Description", product_3 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_3, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_3 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '4':
            product_4 = Analysis [Analysis ['Product_Type'] == '4']
            st.write ( "Product Description", product_4 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_4, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_4 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '5':
            product_5 = Analysis [Analysis ['Product_Type'] == '5']
            st.write ( "Product Description", product_5 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_5, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_5 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )


        elif product_options == '6':
            product_6 = Analysis [Analysis ['Product_Type'] == '6']
            st.write ( "Product Description", product_6 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_6, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_6 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )


        elif product_options == '7':
            product_7 = Analysis [Analysis ['Product_Type'] == '7']
            st.write ( "Product Description", product_7 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_7, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_7 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '8':
            product_8 = Analysis [Analysis ['Product_Type'] == '8']
            st.write ( "Product Description", product_8 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_8, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_8 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

        elif product_options == '9':
            product_9 = Analysis [Analysis ['Product_Type'] == '9']
            st.write ( "Product Description", product_9 )

            fig_hist = plt.figure ( figsize=(10, 4) )
            sns.histplot ( data=product_9, x='Sentiment' )
            plt.title ( "Sentiment Count" )
            st.pyplot ( fig_hist )
            count = {'Sentiment count': product_9 ['Sentiment'].value_counts ()}
            sentiment_count = pd.DataFrame ( count )
            st.table ( sentiment_count )

    with tab2 :
        description = st.selectbox ( "Select Any Description", Analysis ['Product_Description'] )
        index = Analysis.loc [description == Analysis ['Product_Description']]
        columns = pd.DataFrame ( index )
        product= columns['Product_Type'].to_list()
        sentiment = columns ['Sentiment'].to_list ()
        st.markdown("Product Type: ")
        st.success(product)
        st.markdown( "Sentiment: ")
        st.success (sentiment )
        st.write ( columns )

    # model = pickle.load ( open ( 'model.pkl', 'rb' ) )
    # prediction  = model.predict(Analysis)

elif choice == "Dataset":
    webbrowser.open_new_tab( Dataset )


else:
    webbrowser.open_new_tab( About )