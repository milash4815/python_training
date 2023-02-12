


def test_add_to_cart(app):
    app.open_home_page(link="https://demowebshop.tricentis.com/")
    app.session.log_in(email="miwoacc@gmail.com", password="Asuraloh581321!")
    app.adding_to_cart()
