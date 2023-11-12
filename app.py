import streamlit as st
from PIL import Image
import feedparser
import requests


import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Mathavan S.G
##### *Resume* 
''')
st.markdown('<p style="text-align:center;"><a href="https://drive.google.com/file/d/1lzu71jfUWl5_R9hMvo9s3OambJhydMgQ/view?usp=drive_link" download="Mathavan_Resume.pdf">Download Resume</a>', unsafe_allow_html=True)

image = Image.open('C:\\Users\\GANESH\\Desktop\\Project\\Portfolio\\16059.jpg')

st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Final year student in the Artificial Intelligence and Data Science department at Easwari Engineering College, showcasing a strong passion for the dynamic field of data science. Proficient in key areas of AI and data science, with a keen interest in leveraging data-driven insights to solve real-world problems. 
- Possesses excellent communication skills, adept at translating complex technical concepts into accessible and actionable information. Eager to contribute innovative solutions to the ever-evolving landscape of data science and make a meaningful impact in the industry.
''')

#####################
# Navigation

# Add Bootstrap CSS
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Add navigation bar
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href='https://www.linkedin.com/in/mathavansg/' target="_blank">Mathavan S G</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
      <li class="nav-item">
        <a class="nav-link" href="#blog">Blog</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Technology** (Artificial Intelligence and Data Science), *Easwari Engineering College*, Chennai',
'2020-2024')
st.markdown('''
- GPA: `8.6 CGPA`
''')

txt('**Senior Secondary** (Computer Science), *Sri Sankara Vidyshramam*, Chennai',
'2018-2020')
st.markdown('''
- Percentage: `76%`
''')
txt('**Secondary** (General), *Sri Sankara Vidyshramam*, Chennai',
'2017-2018')
st.markdown('''
- Percentage: `86%`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**AI-Intern**, Sona-Comstar, Chennai',
'June-August 2022')
st.markdown('''
- Developed and deployed an AI-powered chatbot that
significantly improved customer engagement and
satisfaction, resulting in a positive feedback. 
- Collaborated with cross-functional teams to design and
implement chatbot functionalities tailored to customer
needs, ensuring a seamless user experience. 
- Conducted regular data analysis on chatbot interactions, extracting valuable insights to further optimize the
chatbot's performance and functionality. 
''')


#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`, `HTML`,`CSS`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`, `Knime`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`Keras`')
txt3('Web development', ' `HTML`, `CSS`')
txt3('Model deployment', '`Streamlit`, `Azure`')
txt3('Business Intelligence Tool', '`Power-BI`')
txt3('LLM-Framework', '`Lang-chain`')
#####################
st.markdown('''
## Blog
''')
@st.cache_data
def blogs():
    rss_url = "https://medium.com/feed/@aimathavan14"
    feed = feedparser.parse(rss_url)

    st.caption("Total Blogs: {}".format(len(feed.entries)))
    for item in feed.entries:
        title = item.title
        categories = [category.term for category in item.get('tags', [])]
        link = item.link
        published = item.published

        with st.expander(f"📖 {title}"):
            st.caption(published)
            st.markdown(f"[Check blog here]({link})")
            st.write("Tags:", categories)

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Display blogs
blogs()

#####################

st.markdown('''
## Projects
''')
def get_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        return None

# Streamlit app
st.markdown('''
## GitHub Projects
''')

# Replace 'YourGitHubUsername' with your actual GitHub username
github_username = 'MathavanSG'

# Fetch GitHub repositories
repositories = get_github_repositories(github_username)

if repositories:
    st.caption(f"Total Repositories: {len(repositories)}")
    for repo in repositories:
        st.markdown(f"**{repo['name']}**")
        st.write(f"Description: {repo['description']}")
        st.write(f"URL: [{repo['html_url']}]({repo['html_url']})")
        st.write(f"Language: {repo['language']}")
        st.write("---")
else:
    st.error(f"Failed to fetch GitHub repositories for user '{github_username}'. Please check your username.")

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/mathavansg/')
txt2('Medium', 'https://medium.com/@aimathavan14')
txt2('GitHub', 'https://github.com/MathavanSG')
