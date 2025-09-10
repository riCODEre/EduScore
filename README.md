# EduScore - Teacher Evaluation System

A web-based platform that allows students to evaluate and provide feedback for their teachers, helping others make
informed decisions about their education.

## Features

- Teacher search functionality
- Detailed teacher profiles with ratings and reviews
- Tag-based evaluation system
- User authentication and registration
- Bookmark favorite teachers
- Edit and delete evaluation capabilities
- Privacy-focused design

## Prerequisites

- Python 3.12.10
- Node.js and npm
- Git
- virtualenv

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ricodere/EduScore.git
   cd EduScore
   ```

2. Set up Python virtual environment:
   ```bash
   python -m virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install JavaScript dependencies:
   ```bash
   npm install
   ```

5. Configure the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```
