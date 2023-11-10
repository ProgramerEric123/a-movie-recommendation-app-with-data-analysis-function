#Linxin Feng
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Movie Assistant! 🍎")

  

    st.markdown(
        """
        😊Focusing on your favoriate movie😊

        Movie assistant is an app that aims to recommend movies to users based on their preferred genre and distributor and provide users with some interesting  data analysis results about Top 1000 Highest Grossing Movies.
        
        ## About the dataset
        [Top 1000 Highest Grossing Movies](https://www.kaggle.com/datasets/sanjeetsinghnaik/top-1000-highest-grossing-movies/)

        ###### Context
        It contains information about the top 1000 highest grossing holywood films. 
        It is up to date as of 25th September 2023.

        ###### Acknowledgements
        This data has been scraped from multiple site and has been added together for performing various data operations. 
        The data has been taken from IMDB, rotten tomatoes and many other sites.

    """
    )


if __name__ == "__main__":
    run()
