from email import header
from os import access
import unittest
from main import create_app
from config import TestConfig
from exts import db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)

            db.create_all()

    def test_ping_api(self):
        ping_response = self.client.get("/api/hello")
        status_code = ping_response.status_code
        self.assertEqual(status_code, 200)

    def test_signup(self):
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        status_code = signup_response.status_code
        self.assertEqual(status_code, 201)

    def test_login(self):
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        status_code = login_response.status_code
        self.assertEqual(status_code, 200)

    def test_create_a_post(self):
        """TEST CREATE A POST"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        create_post_response = self.client.post(
            "/posts/",
            json={
                "title": "The black Adam",
                "post_content": "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
                "user_id": f"{user_id}",
            },
            headers=headers,
        )
        status_code = create_post_response.status_code
        self.assertEqual(status_code, 201)

    def test_get_one_post(self):
        """TEST TO GET SINGLE POST"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        create_post_response = self.client.post(
            "/posts/",
            json={
                "title": "The black Adam",
                "post_content": "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
                "user_id": f"{user_id}",
            },
            headers=headers,
        )
        post_id = create_post_response.json["id"]
        get_one_post_response = self.client.get(f"/posts/post/{post_id}")
        status_code = get_one_post_response.status_code
        self.assertEqual(status_code, 200)

    def test_get_all_users(self):
        """TEST TO GET ALL USERS"""
        get_all_users_response = self.client.get("/users/")
        status_code = get_all_users_response.status_code
        self.assertEqual(status_code, 200)

    def test_get_one_user(self):
        """TEST TO GET SINGLE USER"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        get_one_user_response = self.client.get(
            f"/users/user/{user_id}", headers=headers
        )
        status_code = get_one_user_response.status_code
        self.assertEqual(status_code, 200)

    def test_update_post(self):
        """TEST TO UPDATE A POST"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        create_post_response = self.client.post(
            "/posts/",
            json={
                "title": "The black Adam",
                "post_content": "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
                "user_id": f"{user_id}",
            },
            headers=headers,
        )
        post_id = create_post_response.json["id"]
        update_post_response = self.client.put(
            f"/posts/post/{post_id}",
            json={"title": "An Updated Title", "post_content": " Newly updated post"},
            headers=headers,
        )
        status_code = update_post_response.status_code
        self.assertEqual(status_code, 200)

    def test_update_user(self):
        """TEST TO UPDATE USER DETAILS"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        update_user_response = self.client.put(
            f"/users/user/{user_id}",
            json={
                "username": "user1-updated",
                "user_email": "test_mail-update@gmail.com",
                "password": "password",
                "avatar": "profile_pic.jpg",
            },
            headers=headers,
        )
        status_code = update_user_response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_post(self):
        """TEST TO DELETE A POST"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        create_post_response = self.client.post(
            "/posts/",
            json={
                "title": "The black Adam",
                "post_content": "magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat",
                "user_id": f"{user_id}",
            },
            headers=headers,
        )
        post_id = create_post_response.json["id"]
        delete_post_response = self.client.delete(
            f"/posts/post/{post_id}", headers=headers
        )
        status_code = delete_post_response.status_code
        self.assertEqual(status_code, 200)

    def test_delete_user(self):
        """TEST TO DELETE A USER"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "user1",
                "user_email": "testmail@example.com",
                "password": "password",
                "avatar": "avatar.jpeg",
            },
        )
        user_id = signup_response.json.get("user_id")
        login_response = self.client.post(
            "/auth/login",
            json={
                "username": "user1",
                "password": "password",
            },
        )
        access_token = login_response.json.get("access_token")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        delete_user_response = self.client.delete(
            f"/users/user/{user_id}", headers=headers
        )
        status_code = delete_user_response.status_code
        self.assertEqual(status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
