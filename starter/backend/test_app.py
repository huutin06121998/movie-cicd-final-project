from . import app
import os


def test_movies_endpoint_returns_200():
    # Test if the movies endpoint returns status code 200
    with app.test_client() as client:
        # Check if the status code is as expected or the default is 200
        status_code = os.getenv("FAIL_TEST", 200)
        response = client.get("/movies/")
        assert response.status_code == status_code


def test_movies_endpoint_returns_json():
    # Test if the movies endpoint returns JSON
    with app.test_client() as client:
        response = client.get("/movies/")
        # Check if the content type of the response is JSON
        assert response.content_type == "application/json"


def test_movies_endpoint_returns_valid_data():
    # Test if the movies endpoint returns valid data
    with app.test_client() as client:
        response = client.get("/movies/")
        # Get JSON data from the response
        data = response.get_json()
        # Check if the data is a dictionary
        assert isinstance(data, dict)
        # Check if the 'movies' key exists in the data
        assert "movies" in data
        # Check if the value corresponding to the 'movies' key is a list
        assert isinstance(data.get("movies"), list)
        # Check if there is at least one movie in the list
        assert len(data["movies"]) > 0
        # Check if the 'title' key exists for the first movie in the list
        assert "title" in data["movies"][0]
