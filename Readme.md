
**Setting Up**

We'll use a virtual environment to install python packages only for this project. 

From a command line run `pip install virtualenv virtualenvwrapper` and then run `mkvirtualenv kj` and `workon kj` to 
create and begin using the virtual environment for this project. 

From the project's main directory run `pip install -r requirements.txt` to install the necessary libraries for the project.


**Running The Service**

Once you've completed the setup, you'll be able to run the project with the command `manage.py runserver`.

After the service has been started, a GUI can be accessed by going to `http://127.0.0.1` or you can make direct requests
to the API at `http://127.0.0.1/api/geocode/`.

At the api endpoint, you can pass two parameters. The first required parameter is `address`, which is the query string you
are trying to geocode. The second parameter, `service`,  is optional. If you pass "google" as the parameter, the service
will use Google's geocoding service. Otherwise, Here's geocoding service will be used.

