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
st.title("Release year distribution of Top 1000 Highest Grossing Hollywood Movies ")

# Extract the release year and create a new column
df['Release Year'] = pd.to_datetime(df['Release Date']).dt.year

# Calculate the frequency of each year
year_counts = df['Release Year'].value_counts().sort_index()

# Create a sidebar for the selectbox
st.sidebar.title("Please select the year that you are interested in and then you will see something wonderful ")
sorted_years = sorted(df['Release Year'].unique())
selected_year = st.sidebar.selectbox("Select a Release Year", sorted_years)

st.markdown('''##### ~The histogram below may give you an overal view on realease year distribution .''')
# Plot a frequency histogram
fig, ax = plt.subplots(figsize=(12, 6))
year_counts.plot(kind='bar', ax=ax)
ax.set_title('Frequency Histogram of Top 1000 Highest Grossing Hollywood Movies Releases by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)



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
st.markdown('''##### ~The bar chart below tells the genre distribution in your selected year.''')
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
st.subheader("Top Popular Genres in "+str(selected_year))
st.write(popular_genres)

# Find the top three movies by worldwide sales
# Make sure the column name matches your data
top_movies = filtered_df.nlargest(3, 'World Wide Sales (in $)')
st.subheader("The table below displays  movie list by worldwide sales in "+str(selected_year))
st.write(top_movies[['Title', 'Genre','World Wide Sales (in $)','Running Time']])
