#Author: Jiajie Chu
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Replace with your CSV file path
csv_file = "Highest Holywood Grossing Movies.csv"

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Set the plotting style
plt.style.use("ggplot")

# Create a Streamlit app with a title
st.title("What's the Top 5 Distributors in Total Box Office of Movies?")

# Calculate total box office by distributors
distributor_box_office = df.groupby('Distributor')['World Wide Sales (in $)'].sum().sort_values(ascending=False)

# Create a bar chart in descending order
st.markdown('''##### ~The bar chart below displays total box office by distributor.''')
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
distributor_box_office.sort_values(ascending=True).plot(kind='barh', ax=ax_bar)
ax_bar.set_title('Total Box Office by Distributor (Descending Order)')
ax_bar.set_xlabel('Total Box Office (in $)')
ax_bar.set_ylabel('Distributor')
st.pyplot(fig_bar)

# Create a pie chart for the top 5 distributors
st.subheader("The pie chart below may give you a general view of the proportions of Total box office by distributors")
fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
top_5_distributors = distributor_box_office.head(5)
other_distributors = distributor_box_office.tail(len(distributor_box_office) - 5)
other_box_office = other_distributors.sum()
combined_distributors = pd.concat([top_5_distributors, pd.Series({ 'Other Distributors': other_box_office })])
labels = combined_distributors.index
sizes = combined_distributors.values
ax_pie.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax_pie.axis('equal')
st.pyplot(fig_pie)

# Display the box plot of box office by top 5 distributors
st.markdown('''##### ~The box plot below may help you analyze the distribution of box office of the Top 5 distributors''')
fig_box, ax_box = plt.subplots(figsize=(10, 6))
top_5_data = [df[df['Distributor'] == distributor]['World Wide Sales (in $)'] for distributor in top_5_distributors.index]
ax_box.boxplot(top_5_data, labels=top_5_distributors.index, showfliers=False)
ax_box.set_title('Box Plot of Box Office by Top 5 Distributors')
ax_box.set_ylabel('Box Office (in $)')
plt.xticks(rotation=45)
st.pyplot(fig_box)