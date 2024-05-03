from pathlib import Path

import pandas as pd
import streamlit as st

FILE_PATH = './billboard.parquet'



@st.cache_data
def read_data(parquet_file: Path) -> pd.DataFrame:
    df = pd.read_parquet(parquet_file)
    return df

df = read_data(FILE_PATH)

with st.sidebar:
    artists = st.multiselect(
        'Choose two artists',
        options=df['artist'].unique(), 
        max_selections=2,
        default=None
        )
    if artists:
        songs = st.multiselect(
            'Choose two songs',
            options=df[df['artist'].isin(artists)]['song'].unique(),
            max_selections=2,
            default=None
        )
    else:
        songs = None

main_tab, research_questions, dataframe = st.tabs(['Data and visualizations', 'Research Questions', 'Dataframe'])



with main_tab:
    if (not artists) or (not songs):
        st.info('Please select an artist and a song on the sidebar to the left')
    else:
        st.scatter_chart(df[df['song'].isin(songs) & df['artist'].isin(artists)], x='date', y='this_week', color='song')

with research_questions:
     st.markdown('''
        Your webapp should contain a writeup of what you learned doing the project.  On your main project page, you should have the following information:

        1. Your name

        2. An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc.

        3. Any major “gotchas” (i.e. things that don’t work, go slowly, could be improved, etc.)

        In addition, you’ll need to answer the following questions (they’ll go in a specific page in your webapp.  Don’t worry, we’ll learn how to do that!)

        1. What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)

        2. What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)

        3. What difficulties did you have in completing the project?

        4. What skills did you wish you had while you were doing the project?

        5. What would you do “next” to expand or augment the project?
    '''
    )


with dataframe:
    if (not artists) or (not songs):
        st.info('Please select an artist and a song on the sidebar to the left')
    else:
        st.write(f'You chose {artists, songs}')
        st.dataframe(df[df['song'].isin(songs) & df['artist'].isin(artists)])

    
