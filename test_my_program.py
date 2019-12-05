import pytest
from app.models import User, UserCards, OurCards
import tempfile, os
# from app import app
from app import create_app
from config import Config



@pytest.fixture(scope='module')
def new_user():
    user = User(username='bobby', email='bobbywasabi@gmail.com')
    user.set_password('BobbyTheGreat1997')
    return user
# test 1: validate new user
def test_new_user(new_user):
    assert new_user.username == 'bobby'
    assert new_user.email == 'bobbywasabi@gmail.com'
    assert new_user.check_password != 'BobbyTheGreat1997!'

# test 2: change user password, ensure password is changed (not plain text)
def test_setting_password(new_user):
    new_user.set_password('newpass')
    assert new_user.check_password != 'newpass'
    assert new_user.check_password('newpass')
    assert not new_user.check_password('BobbyTheGreat1997!')
    

@pytest.fixture(scope='module')
def our_new_card():
    card = OurCards(name="bank", percentOnline=3.12, percentTravel=2.11, percentAuto=1.56)
    return card
# test 3: ensure card is initialized in our database correctly
def test_our_new_card(our_new_card):
    assert our_new_card.name == "bank"
    assert our_new_card.percentOnline == 3.12
    assert our_new_card.percentTravel != 2.18
    assert our_new_card.percentAuto == 1.56

# test 4: test if user gets authenticated
def test_user_authentification(new_user):
    assert new_user.is_authenticated == True

@pytest.fixture(scope='module')
def new_user_cards(new_user):
    card = UserCards(author=new_user, cardName="test", onlineEstimate=3000, cbOnlinePercentage=3, travelEstimate=2000, cbTravelPercentage=2, autoEstimate=1000, cbAutoPercentage=1)
    return card

# test 5: test if user card has correct values
def test_user_cards(new_user_cards):
    assert new_user_cards.cardName == "test"
    assert new_user_cards.onlineEstimate == 3000
    assert new_user_cards.travelEstimate == 2000
    assert new_user_cards.autoEstimate == 1000
    assert new_user_cards.cbOnlinePercentage == 3
    assert new_user_cards.cbTravelPercentage == 2
    assert new_user_cards.cbAutoPercentage == 1

# test 6: validate owner of the credit card
def test_new_user_cards_creator(new_user_cards, new_user):
    assert new_user_cards.author == new_user

# test 7: validate user id
def test_user_card_id(new_user):
    assert new_user.get_id() == "None"
    new_user.id = 2
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == "2"


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()

# test 8: validate that we can start a flask application and visit the home
def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    
# # def test_new_user