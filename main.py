import streamlit as st
def main():
    header = st.container()
    with header:
        st.title("Courtney Shammas")
    buttons = st.sidebar.radio("Select content",["Bio", "Skills", "Projects"])
    image_url = "https://github.com/paytonncourt96/OnlineCV/raw/main/CV_picture.jpg"
    st.image(image_url,  width=200, use_column_width=False)
       
    if buttons == "Bio":
        # Login page
        Bio()
    elif buttons == "Skills":
        Skills()
    elif buttons == "Projects":
        Projects()
    else:
        st.warning("Please select an option: ")
        
if __name__ == "__main__":
    main()
