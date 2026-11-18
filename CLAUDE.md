# Portfolio Site — Project Context

## What this is
Flask portfolio website for Owen Teo. Dark theme, plain HTML/CSS + Jinja2. No JS framework.
Live on Render: https://portfolio-site-sxr1.onrender.com (auto-deploys on every push to `master`, so work on a branch).

## Structure
- `app.py` — Flask app, routes, 404 handler. A context processor gives every template `profile`.
- `data/content.py` — ALL text content: PROFILE, HIGHLIGHTS, PROJECTS, EXPERIENCE, EDUCATION, SKILLS, AWARDS, CERTIFICATIONS
- `templates/` — Jinja2 HTML templates, all extend `base.html` (nav with active page, meta + Open Graph tags, footer)
- `static/css/style.css` — dark theme CSS (purple accent, dark bg); colours are CSS variables at the top
- `static/favicon.svg` — tab icon
- `static/img/` — drop a profile photo here as `photo.jpg` (not added yet)
- `tests/test_pages.py` — pytest checks that every page loads and unknown paths 404

## Running locally
```bash
pip install -r requirements.txt
FLASK_DEBUG=1 python app.py   # debug is off unless FLASK_DEBUG=1
```
Open http://127.0.0.1:5000

## Tests
```bash
pip install -r requirements-dev.txt
pytest
```

## To update content
Edit `data/content.py` only. Each project needs title, subtitle, period, description, tags, status ("in-progress" | "planned" | "complete") and link (None or a URL).

## Writing style for site text and README
Owen's voice: first person, plain words, short sentences, British spelling, no em dashes or semicolons, no hype words. Only facts Owen has confirmed; no invented numbers, dates or results.

## Hosting
- **Render.com free tier:** `gunicorn app:app` (gunicorn is in requirements.txt)
- **LattePanda local:** run `python app.py`, open it over Tailscale

## To add a profile photo
Put an image at `static/img/photo.jpg` and update `index.html`:
Replace the `.avatar-placeholder` div with:
```html
<img src="{{ url_for('static', filename='img/photo.jpg') }}" alt="Owen Teo" class="avatar" />
```
Add to CSS: `.avatar { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 2px solid var(--border); }`

## Pages
- `/` — hero + highlights
- `/about` — bio, experience, education, awards, certs
- `/projects` — project cards with dates and status badges
- `/skills` — skills grouped by category
- `/contact` — contact links
