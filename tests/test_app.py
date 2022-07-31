# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_test=True)
        assert "<title>MLH Fellow</title>" in html

        #TODO Add more tests relating to the home page - DONE
        assert '<p><font color="#FFFFFF">Caribbean Hindustani</font></p>' in html
        assert '<p style="font-size:25px">My name is {{ student.f_name }} {{ student.l_name }}.' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status.code == 200
        assert response.is_json
        json == response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # TODO Add more tests relating to the /api/timeline_post GET and POST apis - DONE
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": "Hello world, I'm John!"})
        html = response.get_data(as_text=True)
        assert "John Doe" in html
        assert "john@example.com" in html
        assert "Hello world, I'm John!" in html

        # TODO Add more tests relating to the timeline page - DONE
        response = self.client.get("/api/timeline_post")
        assert response.status.code == 200
        assert response.is_json
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "john@example.com", "content": "Hello world, I'm John"})
        assert response.status_code == 400
        html = response.get_data(as_test = True)
        assert "Invalid name" in html

        #POST request with empty content 
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_test = True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John"})
        assert response.status_code == 400
        html = response.get_data(as_test = True)
        assert "Invalid email" in html