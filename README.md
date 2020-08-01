# Knowledge Base

The Knowledge Base is an information hub for your Data Science company to host,  
- Project Documentation, using R Markdown.
- Web Apps, using Django as Back End, Vue.js as Front End, Nuxt.js for server side rendering.

# Why Knowledge Base?

### Open Source
Make code Open Source, to enable access for everyone to your research, enable collaboration and easy code portability.

### Literate Programming  
Enable interleaving code with text, images or whatever best explains the free flowing thought process behind your project or code using RMarkdown

### Reproducible Research  
Enable peers to verify results of your research independently and strengthen your thesis

### Python and R projects  
Run your Python and R projects using the dedicated Web Server and RMarkdown

### Everyone Can Code   
Learn programming and solve data problems in a creative manner regardless of your job level

### ELI5  
Explain Like I'm 5, an approach to quickly educate on concepts one is unfamiliar with

### Web Apps  
Host Web Apps to serve your Users with Reports or give them an ability to interact with the Data

### Technologies  
Vue, Nuxt, Django, RMarkdown, Gitlab, Docker, Azure

# Requirements
* [Git](https://git-scm.com/downloads/)
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Node](https://nodejs.org/en/download/)
* [Npm](https://www.npmjs.com/get-npm/)
* [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

# Running the application
1. Open up a new Windows terminal ```Windows Key + R``` and type ```cmd```
2. Navigate to Desktop ```cd %UserProfile%\Desktop```
3. Create new folder on Desktop ```mkdir KnowledgeBase```
4. Navigate to folder ```cd KnowledgeBase```
5. Clone the project to the folder ```git clone https://scmgr.eams.ericsson.net/eshanme/knowledgebase```
6. Navigate into the project directory ```cd knowledgebase```
7. Navigate into the django directory ```cd api```
8. Start an instance of Python virtual environment ```pipenv shell```
9. Install the Python dependencies in the virtual environment ```pipenv install```
10. Start the Backend Django API server ```python manage.py runserver```
11. Explore the Backend server at ```http://localhost:8000/api/```
12. Open up a new Windows terminal (from the parent directory of the project) and navigate into the frontend directory ```cd client```
13. Install dependencies ```npm ci```
14. Start the Frontend Development server ```npm run dev```
15. Explore the server-side rendered application i.e., the Knowledge Base on this address - ```http://localhost:3000```

# To Run on Docker
1. Navigate into the directory ```cd knowledgebase```
2. Build and run a Container ```docker-compose up --build -d```
3. Follow steps 6-11 from above to run the Django backend

# Built With

* [Python](https://www.python.org/) - A programming language that lets you work quickly and integrate systems more effectively.
* [Django](http://djangoproject.org/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Nuxt](https://nuxtjs.org/) - Nuxt.js is a minimal framework for creating Vue.js applications with server side rendering, code-splitting, hot-reloading, static generation and more.

# To Do

- Implement Flask as Back end.
- Improve R Markdown folder structure.
- Integrate [DocSearch](https://docsearch.algolia.com/) from Algolia for R Markdown search engine.
- Add Docker for R Markdown.
- App for Navigation Cards.
- Resolve R Markdown iframe bug.
