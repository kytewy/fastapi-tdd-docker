from app import main

# State	Explanation	Code
# Given	the state of the application before the test runs: 	setup code, fixtures, database state
# When	the behavior/logic being tested:                    code under test
# Then	the expected changes based on the behavior:         asserts

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
