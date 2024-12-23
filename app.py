import json, random

import streamlit as st

@st.cache_resource
def get_bible():
    with open('files/bible.json') as bible_file:
        bible = json.load(bible_file)
    return bible

@st.cache_resource
def get_testaments():
    with open('files/testaments.json') as testaments_file:
        testaments = json.load(testaments_file)
    return testaments

@st.cache_resource
def get_authors():
    with open('files/authors.json') as authors_file:
        authors = json.load(authors_file)
    return authors

bible_json = get_bible()
books = tuple(bible_json.keys())

testaments = get_testaments()
authors = get_authors()

def get_random_verse():
    book = random.choice(list(bible_json.keys()))
    chapter = random.choice(list(bible_json[book].keys()))
    verse_list = bible_json[book][chapter]
    verse_number = random.randint(0, len(verse_list) - 1)
    verse = verse_list[verse_number]
    return f"{book} {chapter}:{verse_number + 1} - {verse}"

st.sidebar.title("Bible Navigator")
book_option = st.sidebar.selectbox(
    "Books of the Bible",
    books
)

if book_option == "Home":
    verse = get_random_verse()
    st.divider()
    st.write("Random Verse:")
    st.write(verse)
    st.divider()

else:

    st.sidebar.write("Summary:")
    st.sidebar.audio(f"audio/summaries/{book_option.lower()}.mp3", format="audio/mpeg", loop=False)

    book_chapters = list(bible_json[book_option].keys())
    chapters = st.sidebar.radio(
        "Chapter:",
        book_chapters,
        horizontal=True,
    )
    st.divider()
    st.write(testaments[book_option])
    st.write(f"Book Number: {list(testaments.keys()).index(book_option) + 1}/66")
    st.write(f"Author: {authors[book_option]}")
    st.audio(f"audio/chapters/{book_option.lower()}/{book_option.lower()}-{chapters}.mp3", format="audio/mpeg", loop=False)
    st.divider()
    for index, chapter in enumerate(bible_json[book_option][chapters]):
        st.write(index + 1, chapter)
