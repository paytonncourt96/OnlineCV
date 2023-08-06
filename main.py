import streamlit as st
import plotly.graph_objects as go

def Bio():
    bio_header = st.container()
    with bio_header:
        st.title("Welcome to my bio!")
def Skills():
    skill_header = st.container()
    with skill_header:
        st.title("Skills")
    skills = ["Data Visualization", "Machine Learning", "Data Analysis", "Data Cleaning", "Python", "Java", "R", "SQL/noSQl", "Pandas", "NumPy", "MatPlotLib", "seaborn", "Tensorflow", "Keras", "Torch", "Statistical Analysis"]
    skill_levels = [80, 90, 70, 85, 70, 90, 65, 70, 90, 90, 90, 90, 90, 90, 90, 90]
    fig = go.Figure(data=go.Bar(x=skills, y=skill_levels, marker_color="rgb(65, 168, 121)"))

    # Update chart layout for better visualization
    fig.update_layout(
        title="My Skills",
        xaxis_title="Skill",
        yaxis_title="Skill Level",
        xaxis=dict(tickfont_size=14),
        yaxis=dict(tickfont_size=14),
        margin=dict(l=50, r=50, t=50, b=50),
    )

    # Display the chart using Streamlit
    st.plotly_chart(fig)
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
