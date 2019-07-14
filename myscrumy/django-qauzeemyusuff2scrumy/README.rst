========================
  qauzeemyusuff2scrumy
========================

qauzeemyusuff2scrumy is a simple Django app required to be created
in the current (July 2019) cohort of Linux Jobber internship.


Quick start
-----------

1. Add "qauzeemyusuff2scrumy" to your INSTALLED_APPS in settings.py
file like this:

    INSTALLED_APPS = [
      ...
      "qauzeemyusuff2scrumy.apps.Qauzeemyusuff2ScrumyConfig",
  ]

2. Include the qauzeemyusuff2scrumy URLConf in your project's urls.py
file like this:

    path('qauzeemyusuff2scrumy', include('qauzeemyusuff2scrumy.urls')),
  
3. Run 'python manage.py migrate' to create the qauzeemyusuff2scrumy models

4. Start the development server and visit http://127.0.0.1:8000/qauzeemyusuff2scrumy
   to visit the app index page.