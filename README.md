# Owen Teo — Portfolio Site

**Live site: https://portfolio-site-sxr1.onrender.com**

A personal portfolio website built with Flask and Jinja2. Dark theme, plain HTML/CSS, no JavaScript framework.

---

## Pages

| Route | Content |
|-------|---------|
| `/` | Hero section, 3 highlight cards (Marine Eng, Embedded Systems, 3D Design) |
| `/about` | Bio, work experience timeline, awards, certifications |
| `/projects` | Project cards with status badges (In Progress / Planned / Complete) |
| `/skills` | Skills grouped by category |
| `/contact` | Email, LinkedIn, location |

---

## How to Run

```bash
cd /home/Tesla/projects/portfolio-site
python3.12 app.py
```

Open in browser:
- `http://localhost:5000` (usually works on WSL2)
- If not: run `hostname -I`, use the first IP — `http://172.x.x.x:5000`

---

## How It Works

**Flask** starts a web server. When a browser requests a URL like `/projects`, Flask runs the matching function in `app.py`, which calls `render_template()`.

**Jinja2** (built into Flask) is the templating engine. It takes HTML files with placeholders like `{{ profile.name }}` and `{% for job in experience %}`, injects real data, and sends finished HTML to the browser. The server does all the work — no JavaScript required.

**Data flow:**

```
browser requests /projects
       ↓
Flask matches @app.route("/projects")
       ↓
projects() function runs, passes PROJECTS list to template
       ↓
Jinja2 fills projects.html — loops over each project, renders cards
       ↓
finished HTML sent back to browser
```

---

## File Responsibilities

```
app.py           — URL routing only, no content (30 lines)
data/content.py  — ALL text and data, edit this to update the site
templates/       — HTML structure + Jinja2 loops and variables
static/css/      — styling only, no logic
```

### Template Inheritance

`base.html` contains the nav, footer, and `<head>`. Every other page does:

```html
{% extends "base.html" %}
{% block content %}
  ... page content here ...
{% endblock %}
```

The nav is written once. Change it in `base.html` and all pages update.

---

## Updating Content

All content lives in `data/content.py`. You never need to touch HTML for a content change.

**Add a new project** — append a dict to the `PROJECTS` list:

```python
{
    "title": "My New Project",
    "subtitle": "Description of role",
    "description": "What it does.",
    "tags": ["ESP32", "Python"],
    "status": "in-progress",  # "in-progress" | "planned" | "complete"
    "link": None,  # or "https://github.com/..."
},
```

The template automatically renders a new card for it.

**Update your bio** — edit the `about` list in `PROFILE`.

**Add a skill** — add a string to the relevant list in `SKILLS`.

---

## Styling

Dark theme matches the ricing setup:
- Background: `#0c0b0f` (same as WezTerm)
- Accent: `#8b5cf6` (purple)
- Font stack: Iosevka SS14 → Cascadia Code → Fira Code → monospace

All colours are CSS variables at the top of `static/css/style.css`. One variable change recolours the whole site.

---

## Adding a Profile Photo

Drop a photo at `static/img/photo.jpg`, then in `templates/index.html` replace:

```html
<div class="avatar-placeholder">OT</div>
```

with:

```html
<img src="{{ url_for('static', filename='img/photo.jpg') }}" alt="Owen Teo" class="avatar" />
```

And add to `style.css`:

```css
.avatar { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 2px solid var(--border); }
```

---

## Hosting

**Deployed on Render.com** — https://portfolio-site-sxr1.onrender.com

Free tier — sleeps after 15 mins of inactivity, wakes on next visit (few second delay).

**To deploy updates:**
```bash
git add .
git commit -m "describe your change"
git push
```
Render auto-deploys on every push to `master`.

**Local (LattePanda):** run `python3.12 app.py`, access via Tailscale IP.
