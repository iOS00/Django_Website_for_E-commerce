# Django_website_for_e-commerce
Repository contains my solution for the demo-website project for e-commerce created with Python Django following the manual from the cource on 
Pluralsight https://app.pluralsight.com/library/courses/django-getting-started/table-of-contents

## Installation
Create a virtual environment in the root project and activate it.
```bash
python -m venv <venv_name>

source <venv_name>/bin/activate # Linux
<venv_name>\Scripts\activate.bat # CMD (Windows)
<venv_name>\Scripts\Activate.bat # PowerShell (Windows)

deactivate # To deactivate the venv
```

Install all the required Python packages.
```bash
pip install -r requirements.txt
```

Execute all the migrations, then start the server. Make sure to be in the `meeting_planner` folder, where there's the `manage.py` file.
```bash
python manage.py migrate
python manage.py runserver
```

Enjoy!