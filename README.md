# Securing Django REST APIs with JWT Authentication using Simple-JWT

![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-negative.png)

Enhance the security of your Django REST APIs with JSON Web Token (JWT) authentication using the Simple-JWT library. This comprehensive guide provides a step-by-step walkthrough, accompanied by a real project example, to help you set up JWT authentication seamlessly in your Django applications.

## Tutorial Overview

In this tutorial, you will learn how to:

- Set up a Django project
- Configure Django Rest Framework
- Install and configure Simple-JWT for JWT authentication
- Create API views that require authentication
- Configure URL routing for token endpoints
- Test your endpoints using tools like Postman

## Getting Started

Follow the steps outlined in the tutorial to implement JWT authentication in your Django project. Ensure you have Python and Django installed on your machine before proceeding.

## Prerequisites

- Python 3.x
- Django
- Django Rest Framework
- Simple-JWT

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MehediMK/Django-REST-APIs-with-JWT-Authentication.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Django-REST-APIs-with-JWT-Authentication
   python -m venv venv
   source venv/bin/activate (*linux) or venv\Scripts\activate (*Windows)
   copy "config.py sample" config.py
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Test your API endpoints using tools like Postman.
6. Customize and integrate JWT authentication into your Django project as needed.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve this tutorial.


## Acknowledgments

Special thanks to the Django and Django Rest Framework communities for their invaluable contributions to open-source software development.