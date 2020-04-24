This is a minimal implementation of the Question
 Create an API to allow user connect Hong Kong Government Address Lookup Service and store the result in MongoDB through Django


PREFACE & Methodology
- The HK Address look up is found here
https://data.gov.hk/en-data/dataset/hk-ogcio-st_div_02-als
more options and technical information here
https://www.als.ogcio.gov.hk/docs/Data_Dictionary_for_ALS_EN.pdf

This is my first django app, although I have familiar with python pymongo I have 0 experience with django, the initial plan (building the CRUD) was scrapped after realizing it was a full fledge framework.

the changed plan was to get a minimal working product that works along the line and add more features/error handling later

however, when migrating to djongo I encountered a serious bug.  this bug took a whole day before realizing that djongo must be adopted with a clean mlab database 

files added/modified
addr_manager/settings.py
addr_manager/urls.py

address/models.py
address/urls.py
address/views.py

USAGE
http://localhost:8000/address?query=<your_search_string>

Limitations
no user login / tracking is implemented
no error checking is implemented
this only works for GET Method
application only queries GOV site for ONE result
result is stored AS TEXT in ONE line in mongo (The plan was to modelize it if time permits)





 


