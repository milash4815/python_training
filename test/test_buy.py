from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_process(app):
    app.open_home_page(link="https://demowebshop.tricentis.com/")
    app.session.log_in(email="miwoacc@gmail.com", password="Asuraloh581321!")
    app.add_to_cart()
    app.session.log_out()
