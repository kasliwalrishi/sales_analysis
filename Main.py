import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(data_file):
    
    df = pd.read_csv(data_file)

    monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

   
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales',hue = 'Year', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend(title='Year')
    plt.show()
    

def plot_category_distribution(data_file):
    
    df = pd.read_csv(data_file)

    
    plt.figure(figsize=(10, 8))

    sns.countplot(data=df, x='Category', palette='viridis')
    plt.title('Category-wise Sales Distribution')
    plt.xlabel('Category')

    plt.ylabel('Count')
    plt.show()

def plot_country_dist(data_file):
    df = pd.read_csv(data_file)
    
    # Get the top 10 countries by count so that names of countries on x-axis can be clearly seen
    top_countries = df['Country'].value_counts().nlargest(10).index
    df_top = df[df['Country'].isin(top_countries)]
    
    plt.figure(figsize=(10, 8))
    sns.countplot(data=df_top, x='Country', palette='viridis')
    plt.title('Top 10 Country-wise Sales Distribution')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.show()

def plot_country_dist_by_profit(data_file):
    df = pd.read_csv(data_file)
    
    # Group by Country and sum the Profit
    country_profit = df.groupby('Country')['Profit'].sum().reset_index()

    # Get the top 10 countries by profit
    top_countries_by_profit = country_profit.nlargest(10, 'Profit')

    plt.figure(figsize=(12, 7))
    plt.bar(top_countries_by_profit['Country'], top_countries_by_profit['Profit'])
    plt.title('Top 10 Profit-Wise Countries Distribution')
    plt.xlabel('Country')
    plt.ylabel('Total Profit')
    #plt.xticks(rotation=45)
    #plt.tight_layout()
    plt.show()


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

    print("Mean of Sales : ",sales_mean)
    print("Standard Deviation of Sales : ",sales_std)
    print("Median of Sales : ",sales_median)
    print("Minimum of Sales : ",sales_min)
    print("Maximum of Sales : ",sales_max)
    print("Variance of Sales : ",sales_variance)
    print("Total Sales : ",total_sales)

    print("Mean of profit : ",profit_mean)
    print("Standard Deviation of profit : ",profit_std)
    print("Median of profit : ",profit_median)
    print("Minimum of profit : ",profit_min)
    print("Maximum of profit : ",profit_max)
    print("Variance of profit : ",profit_variance)
    print("Total profit : ",total_profit)

 
if __name__ == "__main__":
    data_file = "processed_data.csv"
    plot_sales_trend(data_file)

    plot_category_distribution(data_file)

    plot_country_dist(data_file)

    plot_country_dist_by_profit(data_file)

    calculate_statistics(data_file)

