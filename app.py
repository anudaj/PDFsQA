import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    
    # Home page details with question input area
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:") 

    # Sidebar to attach relevant pdf document
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your PDFs here and click on process")
        st.button("Process")

if __name__ == '__main__':
    main()