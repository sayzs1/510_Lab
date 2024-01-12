import streamlit as st

st.set_page_config(
    page_title="Zia Sun - UX designer, Architect, ",
    page_icon=":rice:",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image('media/Zia_Profile.jpg', use_column_width=True)

with col2:
    st.markdown(
        """
        # Zia Sun (She/Her)
        - UX designer, Architect                    
        - Graduate Student at [UW](https://www.washington.edu/)
        - Global Innovation Exchange [GIX](https://gix.uw.edu/)
        """
    )

st.markdown("# About")

st.markdown(
    """
    I am a creative designer with a package of skills in different fields. As an architect, and UX designer, my different identities provide me with different perspectives on issues, and I hope to respond and solve the problems through design.
    """
)

st.markdown("# Education")

st.markdown(
    """
    - [University of Washington](https://www.washington.edu/) - Master of Science in Technology innovation - 2023~2025
    - [University of Nottingham](https://www.nottingham.ac.uk/) - Bachelor of Engineering in Architecture - 2017~2021
    """
)

st.markdown("# Work Experience")

st.markdown(
    """
    - Aproject Factory - UX designer - 2022-2023
    - ECADI(East China Architecture Design Institution) - Architect intern - 2021-2022
    """
)

st.markdown(
    """
    # Projects
    - [Project 1](https://www.google.com)
    - [Project 2](https://www.google.com)
    - [Project 3](https://www.google.com)
    - [Project 4](https://www.google.com)
    """
)

st.markdown("# Hobbies and Interests")

st.markdown(
    """
    - I love to travel and explore new places.
    """
)
# Card with image and text
col1, col2, col3 = st.columns(3)
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    - I like cooking Chinese food.
    """
)
col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )

   
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)