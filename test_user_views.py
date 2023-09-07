'''Test user views'''

import os
from unittest import TestCase

from models import db, User, Likes, Follows, connect_db, Message
from bs4 import BeautifulSoup

os.environ['DATABASE_URL'] = 'postgresql:///warbler-test'

from app import app, CURR_USER_KEY

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class TestMessageViews(TestCase):
    '''Test message views'''

    def setUp(self):
        '''Make test client + data'''

        db.drop_all()
        db.create_all()

        self.client = app.test_client()

        self.testuser = User.signup(
            username = 'user123',
            email = 'user@test.com',
            password = 'password123',
            image_url = 'None')
        self.testuser_id = 1000
        self.testuser.id = self.testuser_id 
        self.newUser = User.signup('newUser', 'newUser@test.com','newUserPassword', None)
        self.newUser_id = 1001
        self.newUser_id = self.newUser_id
        self.user1 = 1002
        self.user1 = self.newUser_id
        self.user2 = 1003
        self.user2 = self.newUser_id
    

        db.session.commit()

    def tearDown(self):
        response = super().tearDown()
        db.session.rollback()
        return response

    def test_users(self):
        with self.client as client:
            response =  client.get('/users')

            self.assertIn('@user123', str(resp.data))
            self.assertIn('@newUser', str(res.data))

            self.assertNotIn('@qwerty', str(res.data))

    def test_search(self):
        with self.client as client:
            response = client.get('/users?q=new')

            self.assertIn('@newUser', str(resp.data))

            self.assertNotIn('@qwerty', str(res.data))

    def test_new_user(self):
        with self.client as client:
            response = client.get(f'/users/{self.newUser_id}')
            
            self.assertEqual(response.status_code, 200)

    def test_likes(self):

        addedMessage = Message(id=501, text='Cool new message', user_id=self.newUser_id)
        db.session.add(addedMessage)
        db.session.commit()

        like = Likes(user_id = self.newUser_id, message_id = 501)

        db.session.add(like)
        db.sesion.commit()
        
        with self.client as client:
            with client.session_transaction as session:
                session[CURR_USER_KEY] = self.newUser

                response = client.post('/messages/501/like', follow_redirects = True)
                self.assertEqual(response.status_code, 200)

                likes = Likes.query.filter(Likes.message_id==501).all()
                self.assertEqual(len(likes), 1)

        db.session.remove(like)
        db.sesion.commit()

        with self.client as client:
            with client.session_transaction as session:
                session[CURR_USER_KEY] = self.newUser

                response = client.post('/messages/501/like', follow_redirects = True)
                self.assertNotEqual(response.status_code, 200)

                likes = Likes.query.filter(Likes.message_id==501).all()
                self.assertEqual(len(likes), 0)

        with self.client as client:
            response = client.post(f"/messages/{m.id}/like", follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

            self.assertIn('Access unauthorized', str(resp.data))

    def test_followers(self):

        follow1 = Follows(followed_user = self.user1_id, following_user =self.user2)
        follow2 = Follows(followed_user = self.user2_id, following_user =self.user1)
        
        db.session.add_all([follow1, follow2])
        db.session.commit()

    with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_KEY] = self.user1

            response = c.get(f"/users/{self.user1}/following")
            self.assertEqual(resp.status_code, 200)
            self.assertIn("@user2", str(resp.data))

    with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_KEY] = self.user1_id

            response = client.get(f'/users/{self.user1_id}/followers')
            self.assertEqual(resp.status_code, 200)
            self.assertIn("@user2", str(resp.data))

    with self.client as client:

            response = client.get(f"/users/{self.user1_id}/followers", follow_redirects=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Access unauthorized", str(resp.data))
            self.assertNotIn("@user2", str(resp.data))



