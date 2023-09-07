# Warbler Flyio

## Overview
**Warbler Flyio** is a web application designed to provide users with an interactive platform for sharing and discussing various topics. Built on a robust backend, it incorporates various features to ensure a smooth user experience.

## Deployment URL
The app is deployed at: [https://https://warbler-app.fly.dev/](#)

## Features
- **Interactive UI**: Built with modern web technologies for a responsive experience.
- **Database Integration**: Uses SQL to store and manage user data and posts.
- **Testing**: Comprehensive test suites for models and views.

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL

### Installation
1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
Set up the database using the provided SQL dump:

bash
Copy code
psql < dump.sql
Run the application:

bash
Copy code
python app.py
Directory Structure
app.py: Main application file.
forms.py: Form definitions.
models.py: Database models.
static/: Contains static assets.
templates/: HTML templates for the application.
test_*.py: Test files.
Testing
To run the test suites, execute:

bash
Copy code
python test_message_model.py
python test_message_views.py
python test_user_model.py
python test_user_views.py
Contributing
Contributions are always welcome! Feel free to submit pull requests or raise issues to improve the application.
