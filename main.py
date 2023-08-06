import streamlit as st
def main():
    header = st.container()
    with header:
        st.title("Courtney Shammas")
    buttons = st.sidebar.radio("Select user",["Bio", "Skills", "Projects"])
    main_image = "/Users/payto/Documents/Courses/ADT/Final_Project/Phase3/Streamlit_tast/main_icon.jpg"
    st.image(main_image,  width=200, use_column_width=False)
       
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
