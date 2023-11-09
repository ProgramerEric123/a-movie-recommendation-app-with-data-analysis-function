import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Replace with your CSV file path
csv_file = "Highest Holywood Grossing Movies.csv"

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Set the plotting style
plt.style.use("ggplot")

# Create a Streamlit app with a title
st.title("Genre Distribution in Top 1000 Highest Grossing Hollywood Movies")

# Create a sidebar for the question
st.sidebar.title("What's the genre distribution in Top 1000 Highest Grossing Hollywood Movies?")
st.markdown('''##### ~The bar chart below displays all the genre counts  .''')
# Sidebar to show data labels
show_labels = st.checkbox("Show Data Labels")



# Convert the data in the Genre column to a list
genre_list = df['Genre'].apply(eval)

# Count the frequency of different genres
genre_counts = {}
for genres in genre_list:
    for genre in genres:
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

# Count and sort different genres
sorted_genre_counts = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

# Prepare data for the bar chart
rank = [rank + 1 for rank in range(len(sorted_genre_counts))]
genres = [genre[0] for genre in sorted_genre_counts]
counts = [genre[1] for genre in sorted_genre_counts]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(rank, counts, color='skyblue')
ax.set_yticks(rank)
ax.set_yticklabels(genres)
ax.set_xlabel('Count')
ax.set_ylabel('Genre')
ax.set_title('Genre Counts (sorted by count)')
ax.invert_yaxis()  # Invert the y-axis to have the highest count at the top

# Add data labels if the user chooses to show them
if show_labels:
    for bar, count in zip(bars, counts):
        ax.text(count + 5, bar.get_y() + bar.get_height() / 2, str(count), ha='center')

# Show the plot in the Streamlit app
st.pyplot(fig)

# Create a pie chart
st.markdown('''##### ~The piechart below may give you a general view on genre distribution in Top 1000 Highest Grossing Hollywood Movies.''')

# Provide the top ten genres
top_genres = genres[:10]
top_counts = counts[:10]

# Combine the remaining genres into "Other Genres"
other_genres = genres[10:]
other_counts = counts[10:]
other_counts_combined = sum(other_counts)

# Combine into "Other Genres"
if len(other_genres) > 0:
    top_genres.append("Other Genres")
    top_counts.append(other_counts_combined)

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(top_counts, labels=top_genres, autopct='%1.1f%%', startangle=140)
ax.set_title('Genre Distribution in Top 1000 Highest Grossing Hollywood Movies')
ax.axis('equal')

# Show the pie chart in the Streamlit app
st.pyplot(fig)
