# PopulationAnalysis
Data analysis and representation

This aplication focuses on data analysis, parsing and data representation using Django Framework.

Setup <br>
  Create a python virtual enviorment <br>
  Install Django<br>
  Import the PIngPong project <br>
  Create database using magae.py task: <br>
    -manage.py makemigrations <br>
    -manage.py migrate <br>
  Start serve yo host the application on browser: -manage.py runserver<br>

Deployment: Before deployment don't forget to set the DEBUG flag to False in settings.py<br>

Project technology specifications: 
  Django - The web framework 
  Python - Programming language 
  Databases - sqlite 
  Templates - DjangoTemplates, Html, 
  RestAPI - Rest api framework
  UI Interaction: Javascrit, Jquery, Ajax  

Launch project: Enter [http://127.0.0.1:8000/user/index/] in browser this will take you to the home page

Project Structure: <br>
  Projecr PopulationAnalysis: Contains project setting and url mapings.<br>
  User: Manages data handling and representation<br>

REST API calls:
http://127.0.0.1:8000/user/list_all/<br>
http://127.0.0.1:8000/user/gender_count/<br>
http://127.0.0.1:8000/user/relationship_count/<br>
http://127.0.0.1:8000/user/search/gender=M/race=2/rel=3/<br>
http://127.0.0.1:8000/user/selector_list/<br>

Parser : load_data.py is the parser used to populate the data base using csv input file.

Authors Kaushal Pahwani
