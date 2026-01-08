import streamlit as st
import pandas as pd

def Bio():
    with st.container():
        st.header("Biography")
        st.write(
            "I am a DevOps Engineer at Third Horizon, where my work centers on healthcare "
            "data systems with a focus on carrier cost data and Machine-Readable Files (MRFs). "
            "I support infrastructure and data workflows that enable analysis of complex, "
            "large-scale pricing and cost datasets."
        )
        st.write(
            "My professional background is rooted in the Medicaid claims and CMS space, "
            "with a strong emphasis on cost analysis, claims data, and large-scale "
            "healthcare datasets. This experience has given me a deep understanding of "
            "how policy, data, and technology intersect in public health programs."
        )
        st.write(
            "I hold a Master's degree in Data Science from Indiana University Bloomington, "
            "with a concentration in Machine Learning. My academic work focused on applying "
            "statistical modeling and machine learning techniques to complex, real-world data."
        )
        st.write(
            "By combining hands-on experience with claims data and cost modeling with my "
            "current work on carrier-side systems, I bring a well-rounded perspective to "
            "data engineering and machine learning challenges in healthcare."
        )

        st.write("Location: Indianapolis, Indiana, United States")
        st.write("Occupation: DevOps Engineer | Healthcare Data and Artifical Intelligence")
        st.write(
            "Education: Master of Science in Data Science, Indiana University Bloomington | "
            "Bachelor of Science in Mathematics (2019) | "
            "Bachelor of Arts in Physics (2019)"
        )
        st.write(
            "Interests: Hiking, biking, running, reading science fiction, and playing fetch with my dog Bjorn"
        )
        st.write("Contact: paytonncourt96@gmail.com")
        st.write("Connect with me:")
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




