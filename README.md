# Flask Static Web App

A simple static web application built with Flask featuring three pages with random content.

## Features

- **Landing Page** - Displays a random image (uses Lorem Picsum)
- **Details Page** - Shows random informational text
- **Contact Page** - Displays random contact information

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Debug Mode

By default, debug mode is disabled. To enable it, set the environment variable:

```bash
export FLASK_DEBUG=true
python app.py
```

## Project Structure

```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/
│   └── css/
│       └── style.css      # CSS styling
└── templates/
    ├── base.html          # Base template with navigation
    ├── landing.html       # Landing page template
    ├── details.html       # Details page template
    └── contact.html       # Contact page template
```
