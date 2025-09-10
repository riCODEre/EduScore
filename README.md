# EduScore - Teacher Evaluation System

EduScore is a comprehensive web application designed to help students evaluate and rate their professors. The platform allows students to provide feedback on various aspects of their educational experience, helping future students make informed decisions about course selection.

## Features

- **User Authentication**: Secure registration and login system for students
- **Teacher Evaluation**: Rate professors on multiple metrics:
  - Overall professor rating
  - Professor difficulty
  - Willingness to retake courses with the professor
  - BigSky usage rate
  - Professor attendance
  - Grades received
- **Search Functionality**: Find professors by name, subject, or department
- **Tagging System**: Add tags to evaluations to highlight specific professor characteristics
- **Bookmarking**: Save favorite professors for quick access
- **Evaluation Management**: Edit or delete your evaluations
- **Statistics**: View aggregated statistics for each professor including average ratings
- **Sorting and Filtering**: Sort evaluations by various criteria

## Technologies Used

- **Backend**: Django 5.0.8
- **Frontend**: HTML, CSS, JavaScript, Tailwind CSS
- **Database**: SQLite (default)
- **Authentication**: Django's built-in authentication system

## Project Structure

```
EduScore/
├── EduScore/              # Main Django project settings
├── EvalSys/               # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Form definitions
│   └── tests.py           # Tests
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/riCODEre/EduScore.git
   cd EduScore
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## Usage

1. **Register an Account**: Create a new account with your student information
2. **Search for Professors**: Use the search functionality to find professors by name, subject, or department
3. **View Professor Details**: Click on a professor to view their details and existing evaluations
4. **Evaluate a Professor**: Fill out the evaluation form with your ratings and feedback
5. **Add Tags**: Add relevant tags to your evaluation to highlight specific characteristics
6. **Bookmark Professors**: Save professors to your bookmarks for quick access
7. **Manage Your Evaluations**: Edit or delete your evaluations as needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the license included in the repository.