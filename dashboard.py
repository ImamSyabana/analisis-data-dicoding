import streamlit as st
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn

st.markdown(
    """
    # Bike sharing dashboard
    Dashboard untuk memvisualisasikan graph untuk melakukan explanatory data
    """
)


bikeSharing_daily_df = pd.read_csv("bikeSharing_daily_clean.csv", delimiter=",")
bikeSharing_hourly_df = pd.read_csv("bikeSharing_hourly_clean.csv", delimiter=",")



def plot_time_series_day(timesteps, values, format="-", start=0, end=None, label=None):
    """
    Plots timesteps (a series of points in time) against values (a series of values across timesteps).

    Parameters
    ----------
    timesteps : array of timestep values
    values : array of values across time
    format : style of plot, default "."
    start : where to start the plot (setting a value will index from start of timesteps & values)
    end : where to end the plot (similar to start but for the end)
    label : label to show on plot about values, default None
    """
    # Create a numpy array from timesteps and values
    timesteps = np.array(timesteps)
    values = np.array(values)

    # plot the series
    st.line_chart(values[start:end], use_container_width=True)

    #st.pyplot(plt)

    if label:
        plt.legend(fontsize=14)  # make label font bigger
    plt.grid(True)


st.title('Grafik Tren jumlah sepedah yang direntalkan per hari')

rental_per_day = bikeSharing_daily_df.index.to_numpy()
count_day = bikeSharing_daily_df["cnt"].to_numpy()
month_perday = bikeSharing_daily_df["mnth"].to_numpy()

timesteps = rental_per_day
values = count_day

# Call the function to plot the time series chart
plot_time_series_day(timesteps, values)

st.markdown("**x-axis labelj**: hari ke-x")
st.markdown("**y-axis label**: jumlah sepedah yang direntalkan")


st.title('Grafik Nilai temperature cuaca yang sudah dinormalisasi per hari')

rental_per_day = bikeSharing_daily_df.index.to_numpy()
temp_day = bikeSharing_daily_df["temp"].to_numpy()

timesteps2 = rental_per_day
values2 = temp_day

plot_time_series_day(timesteps2, values2)
st.markdown("**x-axis labelj**: hari ke-x")
st.markdown("**y-axis label**: temperature cuaca yang sudah dinormalisasi per hari")



st.title('Grafik Jumlah akumulasi sepeda yang disewakan pada tiap-tiap jamnya')

hr_hourly = bikeSharing_hourly_df["hr"].to_numpy()
count_hourly = bikeSharing_hourly_df["cnt"].to_numpy()

unique_elements = np.unique(hr_hourly)

# Calculate the sum of values in B for each unique element in A
sum_values = np.zeros_like(unique_elements)  # Initialize array to store the sum of values
for i, element in enumerate(unique_elements):
    sum_values[i] = np.sum(count_hourly[hr_hourly == element])


# Create a dictionary with unique elements as keys and sum values as values
data = {element: value for element, value in zip(unique_elements, sum_values)}

# Plot the histogram
st.bar_chart(data)

# Add x-axis and y-axis labels and a title as Markdown text
st.markdown("**x-axis label**: jam")
st.markdown("**y-axis label**: akumulasi sepeda disewakan pada masing-masing jam")