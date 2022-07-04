def test_malformed_timeline_post(self):
  response = self.client.post("/api/timeline_post", data={"email": 	"aimailene@gmail.com", "content": "hello world, I'm Aima!"})
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid name" in html
    
   response= self.client.post("/api/timeline_post", data= {"name":"John Doe","email":"john@example.com","content":""})
       assert response.status_code==400
       html = response.get_data(as_text = True)
       assert "Invalid content" in html 
       
    def test_malformed_timeline_post_email(self):
       response = self.client.post("/api/timeline_post", data={"name":"aimailene@gmail.com","email":"not-an-email","content":"Hello world,I'm Aima!"})
       assert response.status_code==400
       html = response.get_data(as_text = True)
       assert "Invalid email" in html 
