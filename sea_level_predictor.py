import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lin_reg_1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051, 1), lin_reg_1.slope * range(1880, 2051, 1) + lin_reg_1.intercept)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    lin_reg_2 = linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), lin_reg_2.slope * range(2000, 2051, 1) + lin_reg_2.intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()