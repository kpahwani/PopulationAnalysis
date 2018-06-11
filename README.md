# PopulationAnalysis
Data analysis and representation

This aplication focuses on data analysis, parsing and data representation using Django Framework.

Setup 
  Create a python virtual enviorment 
  Install Django
  Import the PIngPong project 
  Create database using magae.py task: 
    -manage.py makemigrations 
    -manage.py migrate 
  Start serve yo host the application on browser: -manage.py runserver

Deployment: Before deployment don't forget to set the DEBUG flag to False in settings.py

Project technology specifications: 
  Django - The web framework 
  Python - Programming language 
  Databases - sqlite 
  Templates - DjangoTemplates, Html, 
  RestAPI - Rest api framework
  UI Interaction: Javascrit, Jquery, Ajax  

Launch project: Enter [http://127.0.0.1:8000/user/index/] in browser this will take you to the home page

Project Structure: 
  Projecr PopulationAnalysis: Contains project setting and url mapings.
  User: Manages data handling and representation

REST API calls:
http://127.0.0.1:8000/user/list_all/
http://127.0.0.1:8000/user/gender_count/
http://127.0.0.1:8000/user/relationship_count/
http://127.0.0.1:8000/user/search/gender=M/race=2/rel=3/
http://127.0.0.1:8000/user/selector_list/

Parser : load_data.py is the parser used to populate the data base using csv input file.

Authors Kaushal Pahwani
