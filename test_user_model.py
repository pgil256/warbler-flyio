"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    def test_following(self):
        self.user1.following.append(self.user2)
        db.session.commit()

        self.assertTrue(self.user1.is_following(self.user2))
        self.assertFalse(self.user2.is_following(self.user1))

        self.assertTrue(self.user2.is_followed_by(self.user1))
        self.assertFalse(self.user1.is_followed_by(self.user2))

    def test_signup(self):
        signup_test = User.signup('testUser', 'throwaway@email.com', 'randPass', None)
        userId = 100
        user_test.id = userId
        db.session.commit

        signup_test = User.query.get(userId)
        self.assertEqual(signupTest.username, 'testUser')
        self.assertEqual(signupTest.username, 'throwaway@email.com')
        self.assertEqual(signupTest.username, 'password')

        invalid_username = User.signup(None, 'throwaway2@email.com', 'randPass', None)
        userId= 101
        invalid_username.id = userId
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()

        invalid_password = User.signup('testUser3', 'throwaway3@email.com', None, None)
        userId= 102
        invalid_password.id = userId
        with self.assertRaises(ValueError) as context:
            db.session.commit()

    def test_authentification(self):
        user = User.authenticate(self.user1.username, self.user1.password)
        self.assertEqual(user.id, self.userid1)

    def test_credentials(self):
        self.assertFalse(User.authenticate('nonsense', self.user1.password))
        self.assertFalse(User.authenticate(self.user1.username, 'nonsense'))        