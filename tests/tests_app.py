def test_malformed_timeline_post(self):
  response = self.client.post("/api/timeline_post", data={"email": 	"aimailene@gmail.com", "content": "hello world, I'm Aima!"})
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid name" in html
