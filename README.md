# Flask Starter Project

A starter template for Flask applications with a structured layout, environment configurations, and essential setup for rapid development.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Organized file structure to kickstart Flask application development.
- Built-in database integration using SQLAlchemy.
- Environment-based configurations for development and production.
- Templates and static files for easy setup of frontend.
- Pre-configured basic routes, error handling, and logging.

## Requirements

- **Python 3.7+**
- **Virtual environment** (e.g., `venv` or `virtualenv`)
- Optional: **Flask-Migrate** and **pytest** for database migrations and testing

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pygenicarc/flask_starter_project.git
cd flask_starter_project
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file to set up your environment variables:

```bash
cp .env.example .env
```

Update `.env` with your configuration, such as database URL and secret keys.

## Usage

### Running the Application

Once installed, start the Flask app with:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

### Running in Development Mode

For auto-reloading in development mode, set the `FLASK_ENV` variable to `development` in your `.env` file:

```bash
export FLASK_ENV=development  # On Windows, use `set FLASK_ENV=development`
```

### Database Migrations

If you're using SQLAlchemy with Flask-Migrate, you can initialize and manage migrations with:

```bash
flask db init         # Initializes the migrations directory
flask db migrate -m "Initial migration."  # Creates migration scripts
flask db upgrade      # Applies migrations to the database
```

## Project Structure

The project follows this directory structure:

```plaintext
flask_starter_project/
│
├── app/                    # Main application package
│   ├── __init__.py         # Initializes app and extensions
│   ├── routes.py           # Application routes/endpoints
│   ├── models.py           # Database models
│   ├── templates/          # HTML templates
│   └── static/             # Static assets (CSS, JS, images)
│
├── migrations/             # Database migration files
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .env.example            # Sample environment variables
├── .gitignore              # Files and directories to ignore in Git
└── README.md               # Project documentation
```

## Configuration

All configurations are set in `config.py` and `.env`:

- **`FLASK_ENV`**: Set to `development` for development mode.
- **`DATABASE_URL`**: Connection string for the database.
- **`SECRET_KEY`**: Secret key for session management.

You can extend `config.py` with environment-specific configurations for production, testing, etc.

## Testing

This project uses `pytest` for unit testing.

1. **Install Testing Dependencies** (if not already installed):

   ```bash
   pip install pytest
   ```

2. **Run Tests**:

   Run all tests with:

   ```bash
   pytest
   ```

3. **Coverage** (Optional):

   To check test coverage, install `pytest-cov` and use:

   ```bash
   pip install pytest-cov
   pytest --cov=app
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch and create a pull request.

For more details, see the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

This `README.md` file covers installation, usage, configurations, project structure, testing, and contribution guidelines specific to the Flask starter project.
