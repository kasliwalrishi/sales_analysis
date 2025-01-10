import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_sales_trend(data_file):
    
    df = pd.read_csv(data_file)

    
    monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

    
    fig, ax = plt.subplots(figsize=(12, 7))

    sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o', ax=ax)

    ax.set_title('Monthly Sales Trend')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend(title='Year')
    return fig

def plot_category_distribution(data_file):
    
    df = pd.read_csv(data_file)

    
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.countplot(data=df, x='Category', palette='viridis', ax=ax)
    ax.set_title('Category-wise Sales Distribution')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    return fig

def plot_country_dist(data_file):
    df = pd.read_csv(data_file)
    
    
    top_countries = df['Country'].value_counts().nlargest(10).index
    df_top = df[df['Country'].isin(top_countries)]

    fig, ax = plt.subplots(figsize=(12, 7))

    sns.countplot(data=df_top, x='Country', palette='viridis', ax=ax)

    ax.set_title('Top 7 Country-wise Sales Distribution')
    ax.set_xlabel('Country')
    ax.set_ylabel('Count')
    return fig

def plot_country_dist_by_profit(data_file):
    df = pd.read_csv(data_file)
    
    
    country_profit = df.groupby('Country')['Profit'].sum().reset_index()

    # Get the top 10 countries by profit
    top_countries_by_profit = country_profit.nlargest(10, 'Profit')

    fig,ax = plt.subplots(figsize=(12,7))
    plt.bar(top_countries_by_profit['Country'], top_countries_by_profit['Profit'])

    ax.set_title('Top 10 Profit-Wise Countries Distribution')
    ax.set_xlabel('Country')

    ax.set_ylabel('Total Profit')
    
    return fig


def calculate_statistics(data_file):
    
    df = pd.read_csv(data_file)
    
    
    sales_mean = np.mean(df['Sales']) 
    sales_std = np.std(df['Sales']) 
    sales_median = np.median(df['Sales']) 
    sales_min = np.min(df['Sales']) 
    sales_max = np.max(df['Sales']) 
    sales_variance = np.var(df['Sales']) 
    total_sales = np.sum(df['Sales'])

    profit_mean = np.mean(df['Profit'])

    profit_std = np.std(df['Profit']) 
    profit_median = np.median(df['Profit'])

    profit_min = np.min(df['Profit']) 
    profit_max = np.max(df['Profit']) 
    profit_variance = np.var(df['Profit'])

    total_profit = np.sum(df['Profit'])

    return {


        "Mean Sales": sales_mean, 
        "Standard Deviation": sales_std, 
        "Median Sales": sales_median, 
        "Minimum Sales": sales_min, 
        "Maximum Sales": sales_max, 
        "Variance": sales_variance, 
        "Total Sales": total_sales,    
        
        "Mean Profit": profit_mean, 
        "Standard Deviation": profit_std, 
        "Median Profit": profit_median, 
        "Minimum Profit": profit_min, 
        "Maximum Profit": profit_max,
        "Profit Variance": profit_variance, 
        "Total Profit": total_profit
        

    }

def main():
    st.title("E-commerce Sales and Profit Analysis Of Super-Market")
    st.write("~ By Rishi Kasliwal")

    
    data_file = "processed_data.csv"
    df = pd.read_csv(data_file)

    # Display data
    st.header("Dataset Overview")
    st.dataframe(df.head())

    # Visualizations
    st.header("Sales Trend")
    sales_trend_fig = plot_sales_trend(data_file)
    st.pyplot(sales_trend_fig)

    st.header("Sales by Category")
    category_sales_fig = plot_category_distribution(data_file)
    st.pyplot(category_sales_fig)

    st.header("Sales by Country")
    country_sales_fig = plot_country_dist(data_file)
    st.pyplot(country_sales_fig)

    st.header("Profit by Country")
    country_profit_fig = plot_country_dist_by_profit(data_file)
    st.pyplot(country_profit_fig)

    # Display statistics
    st.header("Sales and Profit Statistics($)") 
    statistics = calculate_statistics(data_file) 
    for stat, value in statistics.items(): 
        st.write(f"{stat}: {value}")

if __name__ == "__main__":
    main()
