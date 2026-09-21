# Ritu Priya Singh — Flask Portfolio

A sleek, dark-themed personal portfolio website built with Flask.

## Project Structure

```
portfolio/
├── app.py                  # Flask application & data
├── requirements.txt
├── templates/
│   └── index.html          # Jinja2 template (single page)
└── static/
    ├── css/
    │   └── style.css       # All styles
    └── js/
        └── main.js         # Animations, form, interactions
```

## Setup & Run

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
python app.py
```

Open your browser at: **http://localhost:5000**

## Customization

All portfolio content lives in `app.py` inside the `portfolio_data` dictionary.  
Update your links, experience, projects, certifications, and skills there.

## Features

- Fully responsive (mobile, tablet, desktop)
- Dark terminal aesthetic with indigo/violet accents
- Smooth scroll reveal animations
- Interactive contact form (JSON API endpoint)
- Animated terminal card in hero section
- Active nav link highlighting on scroll
- Hamburger menu on mobile
