import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Zia Sun - UX designer, Architect, ",
    page_icon=":rice:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Define columns
col1, col2 = st.columns([0.3, 0.7])

# Define CSS style
round_css = """
<style>
  .circle-image {
      width: 200px;
      height: 200px;
      border-radius: 50%;
      overflow: hidden;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  }
  
  .circle-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
  }
</style>
"""

# Apply external CSS style
st.markdown(round_css, unsafe_allow_html=True)

# Column 1 with profile image
with col1:
    st.markdown('<div class="circle-image"><img src="https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/Zia_Profile.jpg" alt="Profile Picture"></div>', unsafe_allow_html=True)

# Column 2 with text
with col2:
    st.markdown(
        """
        # Zia Sun (She/Her)
        - UX designer, Architect                    
        - Graduate Student at [UW](https://www.washington.edu/)
        - Global Innovation Exchange [GIX](https://gix.uw.edu/)
        """
    )

# About section
st.markdown("# :ok_woman: About")
st.markdown(
    """
    I am a creative designer with a package of skills in different fields. 
    As an architect and UX designer, my different identities provide me with different perspectives on issues, and I hope to respond and solve the problems through design.
    """
)

# Education section
st.markdown("# :mortar_board: Education")
st.markdown(
    """
    - [University of Washington](https://www.washington.edu/) - Master of Science in Technology innovation - 2023~2025
    - [University of Nottingham](https://www.nottingham.ac.uk/) - Bachelor of Engineering in Architecture - 2017~2021
    """
)

# Work Experience section
st.markdown("# :briefcase: Work Experience")
st.markdown(
    """
    - Aproject Factory - UX designer - 2022-2023
    - ECADI(East China Architecture Design Institution) - Architect intern - 2021-2022
    """
)

# Projects section
st.markdown(
    """
    # :book: Projects
    - [Project 1 - Blossom](https://ziyisun.com/blossom/)
    - [Project 2 - GrowingTogether](https://ziyisun.com/growing-together/)
    - [Project 3 - A-NFT](https://ziyisun.com/elementor-3973/)
    """
)

# Hobbies and Interests section
st.markdown("# :heartpulse: Hobbies and Interests")
st.markdown(
    """
    - :sunrise_over_mountains: I love to travel and explore new places.
    """
)

# Display travel images
col1, col2, col3 = st.columns(3)
for col, image_url in zip([col1, col2, col3], [
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/TRAVEL1.jpg",
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/TRAVEL2.jpg",
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/TRAVEL3.jpg"
]):
    col.markdown(
        f"""
        <style>
        .profile-img img {{
            width: 100%;
            border-radius: 10%;
        }}
        </style>

        <div class="profile-img">

        ![]({image_url})
        </div>
        """,
        unsafe_allow_html=True,
    )

# Cooking section
st.markdown(
    """
    - :ramen: I like cooking Chinese food.
    """
)

# Display cooking images
col1, col2, col3 = st.columns(3)
for col, image_url in zip([col1, col2, col3], [
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/COOKING1.jpg",
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/COOKING2.jpg",
    "https://raw.githubusercontent.com/sayzs1/510_Lab/main/media/COOKING3.jpg"
]):
    col.markdown(
        f"""
        <style>
        .profile-img img {{
            width: 100%;
            border-radius: 10%;
        }}
        </style>

        <div class="profile-img">

        ![]({image_url})
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
footer_text = """
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
st.write(footer_text, unsafe_allow_html=True)