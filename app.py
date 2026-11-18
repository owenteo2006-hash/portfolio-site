import os

from flask import Flask, render_template

from data.content import (
    AWARDS,
    CERTIFICATIONS,
    EDUCATION,
    EXPERIENCE,
    HIGHLIGHTS,
    PROFILE,
    PROJECTS,
    SKILLS,
)

app = Flask(__name__)


@app.context_processor
def inject_profile():
    """Give every template the profile, so the nav, footer and link previews can use it."""
    return {"profile": PROFILE}


@app.route("/")
def index():
    return render_template("index.html", highlights=HIGHLIGHTS)


@app.route("/about")
def about():
    return render_template(
        "about.html",
        experience=EXPERIENCE,
        education=EDUCATION,
        awards=AWARDS,
        certs=CERTIFICATIONS,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=SKILLS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Debug mode only when you ask for it: FLASK_DEBUG=1 python app.py
    # Left on with host 0.0.0.0, the debugger would be reachable by anyone on the network.
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
