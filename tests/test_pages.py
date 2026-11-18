import pytest

from app import app

PAGES = ["/", "/about", "/projects", "/skills", "/contact"]


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize("path", PAGES)
def test_page_loads(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert b"Owen Teo" in response.data


@pytest.mark.parametrize("path", PAGES)
def test_nav_marks_the_current_page(client, path):
    html = client.get(path).get_data(as_text=True)
    assert html.count('aria-current="page"') == 1


def test_unknown_page_returns_404(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404
    assert b"Page not found" in response.data


def test_every_project_has_the_fields_the_template_needs():
    from data.content import PROJECTS

    for project in PROJECTS:
        for field in ("title", "subtitle", "period", "description", "tags", "status", "link"):
            assert field in project, f"{project.get('title')} is missing {field}"
        assert project["status"] in ("in-progress", "planned", "complete")
