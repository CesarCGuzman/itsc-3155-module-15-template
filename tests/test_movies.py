from flask.testing import FlaskClient
def test_get_all_movies(test_app: FlaskClient):
    

    res = test_app.get('/movies')
    page_data = res.data.decode()

    assert res.status_code == 200
    assert f'<td>5<td>' 