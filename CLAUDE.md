# Portfolio Site — Project Context

## What this is
Flask portfolio website for Owen Teo. Dark theme, plain HTML/CSS + Jinja2. No JS framework.

## Structure
- `app.py` — Flask app and routes
- `data/content.py` — ALL text content (edit this to update the site, no touching templates needed)
- `templates/` — Jinja2 HTML templates, extend `base.html`
- `static/css/style.css` — dark theme CSS (matches ricing aesthetic: purple accent, dark bg)
- `static/img/` — drop profile photo here as `photo.jpg`

## Running locally
```bash
pip install -r requirements.txt
flask run
# or: python app.py
```
Open http://127.0.0.1:5000

## To update content
Edit `data/content.py`. All sections (PROFILE, PROJECTS, EXPERIENCE, SKILLS, AWARDS, CERTIFICATIONS) are defined there.

## Hosting options
- **LattePanda local:** run `python app.py`, access via Tailscale IP
- **Render.com free tier:** `gunicorn app:app`, add `gunicorn` to requirements.txt
- **Railway:** same as Render, set `PORT` env var

## To add a profile photo
Put an image at `static/img/photo.jpg` and update `index.html`:
Replace the `.avatar-placeholder` div with:
```html
<img src="{{ url_for('static', filename='img/photo.jpg') }}" alt="Owen Teo" class="avatar" />
```
Add to CSS: `.avatar { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 2px solid var(--border); }`

## Pages
- `/` — hero + highlights
- `/about` — bio, experience timeline, awards, certs
- `/projects` — project cards with status badges
- `/skills` — skills grouped by category
- `/contact` — contact links
