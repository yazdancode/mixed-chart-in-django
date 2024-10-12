
# Mixed Chart in Django

This Django project demonstrates how to create and display mixed charts using Chart.js. The application integrates Django with Chart.js to visualize data effectively, combining different types of charts such as line and bar charts in a single view.

## Features

- Display mixed charts using Chart.js
- Fetch data from Django views
- Responsive design for better accessibility on different devices

## Requirements

- Python 3.6 or higher
- Django 3.x or higher
- Chart.js

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yshabanei/mixed-chart-in-django.git
   cd mixed-chart-in-django
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for accessing the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open your web browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

Now you should be able to see the mixed charts in your Django application.
