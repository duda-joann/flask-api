def test_get_artists_no_record(client):
    response = client.get('/api/v1/artists')
    expected_result = {
        'success': True,
        'data': 0,
        'number_of_records': 0,
    }

    assert response.status_code == 200
    assert response.header['Content_Type'] == 'application/json'
    assert response.get_json() == expected_result


def test_get_artists_full(client, sample_data):
    response = client.get('/api/v1/artists')
    expected_result = {
        'success': True,
        'data': 1,
        'number_of_records': 1,

    }

    assert response.status_code == 200
    assert response.header['Content_Type'] == 'application/json'
    assert response.get_json() == expected_result
    assert response.data['success'] is True
    assert response.data['id'] == 1
    assert response.data['name'] == 'AC/DC'
    assert response.data['playcount'] == 100
    assert response.data['listeners'] == 100
    assert response.data['mbid'] == 'aaa-100-bcd-99-cde'


def test_not_found_artist():
    pass