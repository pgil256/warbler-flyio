'''Test message model.'''

import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

os.environ['DATABASE_URL'] = 'postgresql:///warbler-test'

from app import app

db.create_all()

class TestUserModel(TestCase):
    '''Test message functionality'''

    def setUp(self):
        '''Test client and data'''

        db.drop_all
        db.create_all

        self.userid = 10,000
        user = User.signup('test', 'randomname@test.com', 'randompassword', None)
        user.id = self.userid
        db.session.commit()

        self.u = User.query.get(self.userid)

        self.client = app.test_client()

    def tearDown(self):
        response = super().tearDown()
        db.session.rollback()
        return response

    def test_message_model(self):
        
        message = Message(
            text = 'Random text',
            user_id = self.userid
        )
        
        db.session.add(m)
        sb.session.commit()

        self.assertEqual(len(self.user.messages), 1)
        self.assertIn(self.user.messages,'Random text')
        

        