import streamlit as st
import pandas as pd

def Bio():
    bio_header = st.container()
    with bio_header:
        st.title("Welcome to my bio!")
def Skills():
    skill_header = st.container()
    with skill_header:
        st.title("Skills")
    skills_data = { 
        "Skill": ["Data Visualization", "Machine Learning", "Data Analysis", "Data Cleaning", "Python", "Java", "R", "SQL/noSQl", "Pandas", "NumPy", "MatPlotLib", "seaborn", "Tensorflow", "Keras", "Torch", "Statistical Analysis"],
        "Years of Experience":  [4, 1, 2, 2, 4, 1, 4, 1, 4, 4, 4, 4, 1, 1, 1, 6]
    skills_df = pd.DataFrame(skills_data)

   
    st.table(skills_df)
    
def Projects():
    project_header = st.container()
    with project_header:
        st.title("Current Projects")

def main():
    header = st.container()
    with header:
        st.title("Courtney Shammas")
    buttons = st.sidebar.radio("Select content",["Bio", "Skills", "Projects"])
    image_url = "https://github.com/paytonncourt96/OnlineCV/raw/main/CV_picture1.jpg"
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
