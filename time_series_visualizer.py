import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv"
              ,parse_dates=['date'])

# Clean data
df=df[(df['value']>df['value'].quantile(.025))
&
(df['value']<df['value'].quantile(.975))]



def draw_line_plot():
    # Draw line plot
    fig=plt.figure(figsize=(17,10))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.plot(df['date'],df['value'],"-r")
    plt.show()
    fig.canvas.draw() 





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar.date.dt.year
    df_bar['month'] = df_bar.date.dt.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)

    df_bar = df_bar.pivot_table(
        values='value',
        index='year',
        columns='month',
        aggfunc='mean'
    ).sort_index() 

    fig, ax = plt.subplots(figsize=(15, 13))

    df_bar.plot.bar(
        ax=ax,
        xlabel='Years',
        ylabel='Average Page Views'
    )

    legend = ax.legend(
        labels=month_order,    
        title='Months',
        title_fontsize='10',
        fontsize='8'
    )

    fig.tight_layout()

# Save image and return fig (don't change this part)

   


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig=plt.figure(figsize=(14, 6))


    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_box, x='year', y='value',hue='year',legend=False,palette='muted')
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.title('Year-wise Box Plot (Trend)')


    plt.subplot(1, 2, 2)
    # Ordering months to make Jan show as first entry 
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    plt.xlabel("Month")
    plt.ylabel("Page Views")
    sns.boxplot(data=df_box,x='month', y='value',hue='month',order=month_order ,palette='hls')
    plt.title('Month-wise Box Plot (Seasonality)')

    plt.tight_layout()
    plt.show()






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
