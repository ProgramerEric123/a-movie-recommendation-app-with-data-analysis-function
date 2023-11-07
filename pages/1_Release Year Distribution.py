import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Replace with your CSV file path
csv_file = "Highest Holywood Grossing Movies.csv"

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Set the plotting style
plt.style.use("ggplot")

# Add a title
st.title("Release year distribution of Top 1000 Highest Grossing Hollywood Movies Releases by year")

# Extract the release year and create a new column
df['Release Year'] = df['Release Date'].str.split('-').str[0]

# Calculate the frequency of each year
year_counts = df['Release Year'].value_counts().sort_index()

# Plot a frequency histogram
plt.figure(figsize=(12, 6))
year_counts.plot(kind='bar')
plt.title('Frequency Histogram of Top 1000 Highest Grossing Hollywood Movies Releases by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Create a radio button to allow the user to select a year
selected_year = st.selectbox("Select a Release Year", df['Release Year'].unique())

# Filter the data based on the user's selected year
filtered_df = df[df['Release Year'] == selected_year]

# Calculate the count of different genres
genre_list = filtered_df['Genre'].apply(eval)
genre_counts = {}
for genres in genre_list:
    for genre in genres:
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

# Create a bar chart
st.subheader("Genre Counts by Year")
fig, ax = plt.subplots(figsize=(10, 6))
genres = list(genre_counts.keys())
counts = list(genre_counts.values())
ax.bar(genres, counts)
plt.xticks(rotation=90)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title(f'Genre Counts for Movies Released in {selected_year}')

# Display the bar chart
st.pyplot(fig)

# Find the top three most popular genres
popular_genres = dict(sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:3])
st.subheader("Top 3 Popular Genres")
st.write(popular_genres)

# Find the top three movies by worldwide sales
# Make sure the column name matches your data
top_movies = filtered_df.nlargest(3, 'World Wide Sales (in $)')
st.subheader("Top 3 Movies by Worldwide Sales")
st.write(top_movies[['Title', 'World Wide Sales (in $)']])
