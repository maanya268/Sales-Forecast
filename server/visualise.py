import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import numpy as np


st.set_option('deprecation.showPyplotGlobalUse', False)

# Load your data
def load_data():
    excel_data = st.sidebar.file_uploader("Please upload the data file", type="csv")
    if excel_data is not None:
        data = pd.read_csv(excel_data)
        return data

# Create a scatter plot
def scatter_plot(data, x_column, y_column):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    st.pyplot()

# Create a bar chart
def bar_chart(data, column):
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Bar Chart: {column}')
    st.pyplot()

# Create a pie chart
def pie_chart(data, column):
    plt.figure(figsize=(6, 4))
    value_counts = data[column].value_counts()
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
    plt.ylabel('')
    plt.title(f'Pie Chart: {column}')
    st.pyplot()


# Create a line graph
def line_graph(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Line Graph: {x_column} vs {y_column}')
    st.pyplot()

#Time series plot
# Create a time series plot with a fixed number of samples
# def time_series_plot(data, time_column, value_column, num_samples):
#     # Convert the time column to datetime format
#     data[time_column] = pd.to_datetime(data[time_column])

#     # Sample the data based on the fixed number of samples
#     sampled_data = data.sample(n=num_samples, random_state=42)

#     plt.figure(figsize=(10, 6))
#     plt.plot(sampled_data[time_column], sampled_data[value_column])
#     plt.xlabel(time_column)
#     plt.ylabel(value_column)
#     plt.title(f'Time Series Plot: {value_column} over {time_column} ({num_samples} samples)')
#     st.pyplot()


# Create Heat Map
def heatMap(data, selected_columns):
    grouped_data = data.groupby(selected_columns[0])[selected_columns[1]].sum().reset_index()
    heatMap_table = grouped_data.pivot(index=selected_columns[0], columns=selected_columns[1], values=selected_columns[1])
    sns.heatmap(heatMap_table, annot=True, cmap='YlGnBu', fmt='.1f')
    st.pyplot()

def donut_chart(data, column):
    counts = data[column].value_counts()

    fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts.values)])
    fig.update_traces(hole=0.4, hoverinfo='label+percent+value')
    fig.update_layout(title=f"Donut Chart: {column}")
    st.plotly_chart(fig)

def donut_chart_compare(data, column1, column2):
    grouped_data = data.groupby(column1)[column2].count().reset_index()

    fig = go.Figure(data=[go.Pie(labels=grouped_data[column1], values=grouped_data[column2])])
    fig.update_traces(hole=0.4, hoverinfo='label+percent+value')
    fig.update_layout(title=f"Donut Chart: {column1} vs {column2}")
    st.plotly_chart(fig)

# Create a histogram for a column vs another column
# def histogram_compare(data, column1, column2, sample_size=1000):
#     unique_values = data[column2].unique()
#     np.random.seed(42)
    
#     plt.figure(figsize=(10, 6))
#     for value in unique_values:
#         subset_data = data[data[column2] == value]
#         if len(subset_data) < sample_size:
#             subset_size = len(subset_data)
#         else:
#             subset_size = sample_size
#         sample = subset_data[column1].sample(n=subset_size)
#         plt.hist(sample, bins=10, alpha=0.5, label=value)
    
#     plt.xlabel(column1)
#     plt.ylabel('Frequency')
#     plt.title(f'Histogram: {column1} vs {column2}')
#     plt.legend()
#     st.pyplot()

# Update the area_chart function
def area_chart(data, date_column, value_column, start_date, end_date):
    data[date_column] = pd.to_datetime(data[date_column])  # Convert date column to datetime format

    filtered_data = data[
        (data[date_column] >= pd.to_datetime(start_date)) & (data[date_column] <= pd.to_datetime(end_date))
    ]

    aggregated_data = filtered_data.groupby(date_column)[value_column].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(aggregated_data[date_column], aggregated_data[value_column], color='deepskyblue', label='Boundary Line')
    plt.fill_between(aggregated_data[date_column], aggregated_data[value_column], color='lightskyblue')
    plt.scatter(aggregated_data[date_column], aggregated_data[value_column], color='deepskyblue', label='Marked Points')
    plt.xlabel(date_column)
    plt.ylabel(f"Sum of {value_column}")
    plt.title(f'Area Chart: Sum of {value_column} over {date_column}')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot()




# Main function
def main():
    # Sidebar
    st.sidebar.title('Data Visualization')

    # Load data
    data = load_data()

    if data is not None:
        # Select graph type
        graph_type = st.sidebar.selectbox('Select graph type', ['Scatter Plot', 'Bar Chart', 'Pie Chart', 'Line Graph','Heat Map','Donut Chart Compare','Donut Chart','Histogram','Area Chart'])
        # Select columns for comparison
        selected_columns = st.sidebar.multiselect('Select columns', data.columns)

        # Create the selected graph
        if graph_type == 'Scatter Plot':
            if len(selected_columns) == 2:
                scatter_plot(data, selected_columns[0], selected_columns[1])
            elif len(selected_columns) > 2:
                st.warning('Please select only 2 columns for scatter plot.')
        elif graph_type == 'Bar Chart':
            if len(selected_columns) > 0:
                for column in selected_columns:
                    bar_chart(data, column)
        elif graph_type == 'Pie Chart':
            if len(selected_columns) > 0:
                for column in selected_columns:
                    pie_chart(data, column)
        elif graph_type == 'Line Graph':
            if len(selected_columns) == 2:
                line_graph(data, selected_columns[0], selected_columns[1])
            elif len(selected_columns) > 2:
                st.warning('Please select only 2 columns for line graph.')
        elif graph_type == 'Heat Map':
            if len(selected_columns) == 2:
                heatMap(data,selected_columns)
        # elif graph_type == 'Time Series Plot':
        #     if len(selected_columns) == 2:
        #         num_samples = 200  # Choose the desired number of samples
        #         time_series_plot(data, selected_columns[0], selected_columns[1], num_samples)
        #     elif len(selected_columns) > 2:
        #         st.warning('Please select only 2 columns for time series plot.')
        elif graph_type == 'Donut Chart':
            if len(selected_columns) > 0:
                for column in selected_columns:
                    donut_chart(data, column)
        elif graph_type == 'Donut Chart Compare':
            if len(selected_columns) == 2:
                donut_chart_compare(data, selected_columns[0], selected_columns[1])
            else:
                st.warning('Please select exactly 2 columns for donut chart comparison.')
        # elif graph_type == 'Histogram':
        #     if len(selected_columns) == 2:
        #         histogram_compare(data, selected_columns[0], selected_columns[1])
        #     else:
        #         st.warning('Please select exactly 2 columns for histogram comparison.')
        elif graph_type == 'Area Chart':
            if len(selected_columns) == 2:
                data[selected_columns[0]] = pd.to_datetime(data[selected_columns[0]])
                min_date = data[selected_columns[0]].min().date()
                max_date = data[selected_columns[0]].max().date()
                st.sidebar.write(f"Date range: {min_date} to {max_date}")
                start_date = st.sidebar.date_input('Select start date', value=min_date, min_value=min_date, max_value=max_date)
                end_date = st.sidebar.date_input('Select end date', value=max_date, min_value=min_date, max_value=max_date)

                # Create area chart
                area_chart(data, selected_columns[0],selected_columns[1], start_date, end_date)
            else:
                st.warning('Please select exactly 2 columns for Area Chart.')



# Run the app
if __name__ == '__main__':
    main()
