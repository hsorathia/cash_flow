import pytest
from app.models import User, UserCards, OurCards

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

@pytest.fixture(scope='module')
def our_new_card():
    card = OurCards(name="bank", percentOnline=3.12, percentTravel=2.11, percentAuto=1.56)
    return card
# test 2: ensure card is initialized in our database correctly
def test_our_new_card(our_new_card):
    assert our_new_card.name == "bank"
    assert our_new_card.percentOnline == 3.12
    assert our_new_card.percentTravel != 2.18
    assert our_new_card.percentAuto == 1.56

# test 3: test if user gets authenticated
def test_user_authentification(new_user):
    assert new_user.is_authenticated == True

@pytest.fixture(scope='module')
def new_user_cards(new_user):
    card = UserCards(author=new_user, cardName="test", onlineEstimate=3000, cbOnlinePercentage=3, travelEstimate=2000, cbTravelPercentage=2, autoEstimate=1000, cbAutoPercentage=1)
    return card

# test 4: test if user card has correct values
def test_new_user_cards(new_user_cards):
    assert new_user_cards.cardName == "test"
    assert new_user_cards.onlineEstimate == 3000
    assert new_user_cards.travelEstimate == 2000
    assert new_user_cards.autoEstimate == 1000
    assert new_user_cards.cbOnlinePercentage == 3
    assert new_user_cards.cbTravelPercentage == 2
    assert new_user_cards.cbAutoPercentage == 1

# test 5: validate owner of the credit card
def test_new_user_cards_creator(new_user_cards, new_user):
    assert new_user_cards.author == new_user

# def test_new_user_cards_delete(new_user_cards):
