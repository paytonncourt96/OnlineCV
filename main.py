import streamlit as st
import pandas as pd

def Bio():
    with st.container():
        st.header("Biography")
        st.write("Hello! I am currently working for Third Horizon as a DevOps Engineer at the Family and Social Services Administration(FSSA) while pursuing a part-time Master's degree in Data Science at Indiana University Bloomington. I am eager and well-prepared to embrace Data Science opportunities, having gained invaluable knowledge and experience through both my previous job roles and educational pursuits.") 
        st.write("My main interest/emphasis within my education has been Machine Learning. One of the most exciting projects I have had the opportunity to work on is an image detection program utilizing many well-known architectures of Convolutional neural networks.")
        st.write("Age: 28")
        st.write("Location: Indianapolis, Indiana, United States")
        st.write("Occupation: Data Engineer")
        st.write("Education: Bachelor's of Science in Mathematics(Graduated 2019) and Bachelor's of Arts in Physics(Graduated 2019)")
        st.write("Interests: Hiking, Biking, Reading(mainly science fiction!), and playing fetch with my dog Bjorn ")
        st.write("Contact: paytonncourt96@gmail.com")
        st.write("Connect with me!")
        st.write("https://www.linkedin.com/in/courtney-payton96/")

def Skills():
    skill_header = st.container()
    with skill_header:
        st.title("Skills")
    skills_data = { 
        "Skill": ["Data Visualization", "Machine Learning", "Data Analysis", "Data Cleaning", "Python", "Java", "R", "SQL/noSQL", "Pandas", "NumPy", "MatPlotLib", "seaborn", "Tensorflow", "Keras", "Torch", "Spark", "PySpark", "Hadoop", "Statistical Analysis", "Generative AI", "Large Language Models(LLMs)", "Natural Language Processing"],
        "Years of Experience":  [4, 2, 2, 2, 4, 1, 4, 1, 4, 4, 4, 4, 1, 1, 1, 1, 2, 1, 6, 1, 1, 2]
    }
    skills_df = pd.DataFrame(skills_data)

   
    st.table(skills_df)
    
#def Projects():
   # project_header = st.container()
    #with project_header:
        #st.title("Current Projects")

def main():
    header = st.container()
    with header:
        st.title("Courtney Shammas")
    buttons = st.sidebar.radio("Select content",["Bio", "Skills"])#"Projects"
    image_url = "https://github.com/paytonncourt96/OnlineCV/raw/main/CV_picture1.jpg"
    st.image(image_url,  width=200, use_column_width=False)
       
    if buttons == "Bio":
        # Login page
        Bio()
    elif buttons == "Skills":
        Skills()
    #elif buttons == "Projects":
        #Projects()
    else:
        st.warning("Please select an option: ")
        
if __name__ == "__main__":
    main()

