import os
os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
import unittest
from app import Todo, create_app,db
import random 


class FlaskTests(unittest.TestCase):    
    def test_createdb(self):
        self.client = create_app()
        db.create_all()

    def test_homepage(self):
        self.client = create_app().test_client()
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_example(self):
        self.client = create_app().test_client()
        random_id= random.randint(0, 1000)
        data=Todo(id =random_id, content="Mock Description", status=0)
        db.session.add(data) 
        db.session.commit() 
        response = self.client.get("/") 
        assert str(random_id) in response.data.decode('utf-8')  

    def test_delete_example(self):
        self.client = create_app().test_client()
        random_id= random.randint(0, 1000)
        data=Todo(id =random_id, content="Mock Description II", status=0)
        db.session.add(data) 
        db.session.commit() 
        db.session.delete(data) 
        db.session.commit()

        response = self.client.get("/") 
        assert str(random_id) not in response.data.decode('utf-8')  

    def tearDown(self):
        self.client = create_app().test_client()
        db.session.remove()
        db.drop_all()

if __name__ == "__main__": 
    unittest.main()