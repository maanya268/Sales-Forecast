import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    plt.figure(figsize=(8, 6))
    data[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
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

# Main function
def main():
    # Sidebar
    st.sidebar.title('Data Visualization')

    # Load data
    data = load_data()

    if data is not None:
        # Select graph type
        graph_type = st.sidebar.selectbox('Select graph type', ['Scatter Plot', 'Bar Chart', 'Pie Chart', 'Line Graph'])
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

# Run the app
if __name__ == '__main__':
    main()
