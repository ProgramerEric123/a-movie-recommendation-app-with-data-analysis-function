import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 用你的CSV文件路径替换下面的文件路径
csv_file = "Highest Holywood Grossing Movies.csv"

# 使用pandas读取CSV文件
df = pd.read_csv(csv_file)

# Set the plotting style
plt.style.use("ggplot")

# Create a Streamlit app with a title
st.title("Genre Distribution in Top 1000 Highest Grossing Hollywood Movies")

# Sidebar to show data labels
show_labels = st.checkbox("Show Data Labels")

# 将Genre列中的数据转换为列表
genre_list = df['Genre'].apply(eval)

# 统计不同genre的频数
genre_counts = {}
for genres in genre_list:
    for genre in genres:
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

# 统计不同genre的数量并排序
sorted_genre_counts = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

# 准备数据用于条形图
rank = [rank + 1 for rank in range(len(sorted_genre_counts))]
genres = [genre[0] for genre in sorted_genre_counts]
counts = [genre[1] for genre in sorted_genre_counts]

# 绘制条形图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(rank, counts, color='skyblue')
ax.set_yticks(rank)
ax.set_yticklabels(genres)
ax.set_xlabel('Count')
ax.set_ylabel('Genre')
ax.set_title('Genre Counts (sorted by count)')
ax.invert_yaxis()  # Invert the y-axis to have the highest count at the top

# 添加数据标签，如果用户选择显示数据标签
if show_labels:
    for bar, count in zip(bars, counts):
        ax.text(count + 5, bar.get_y() + bar.get_height() / 2, str(count), ha='center')

# Show the plot in the Streamlit app
st.pyplot(fig)

# 绘制饼状图
st.subheader("Pie Chart")

# 给出排名前十的genre
top_genres = genres[:10]
top_counts = counts[:10]

# 将其余的genre合并为"Other Genres"
other_genres = genres[10:]
other_counts = counts[10:]
other_counts_combined = sum(other_counts)

# 合并为"Other Genres"
if len(other_genres) > 0:
    top_genres.append("Other Genres")
    top_counts.append(other_counts_combined)

# 绘制饼状图
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(top_counts, labels=top_genres, autopct='%1.1f%%', startangle=140)
ax.set_title('Genre Distribution in Top 1000 Highest Grossing Hollywood Movies')
ax.axis('equal')

# Show the pie chart in the Streamlit app
st.pyplot(fig)
