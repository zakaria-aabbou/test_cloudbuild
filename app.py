import streamlit as st

def get_text():
    return "Hello, Streamlit!"

def main():
    st.title(get_text())
    # test

if __name__ == "__main__":
    main()