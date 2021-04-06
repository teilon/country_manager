import os
import app
import unittest
import tempfile
import json

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        # app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    # empty --------------------------------------------
    
    def test_countries_get_empty(self):
        rv = self.app.get('/countries')
        assert b'Objects list is empty.' in rv.data
    
    def test_cities_get_empty(self):
        rv = self.app.get('/cities')
        assert b'Objects list is empty.' in rv.data
    
    def test_regions_get_empty(self):
        rv = self.app.get('/regions')
        assert b'Objects list is empty.' in rv.data
    
    # post ----------------------------------------------

    # def test_country_post_empty(self):
    #     rv = self.app.post('/country/Sudan', data=None, headers={'Content-Type': 'application/json'}, follow_redirects=True)
    #     assert b"Data is empty." in rv.data

    # def test_country_post_incorrect(self):
    #     wrong_data = {
    #         "population": "44.909.353",
    #         "land_area": "1.886.068",
    #         "migrants": "150.158",
    #         "medium_age": "28"
    #         }
    #     # rv = self.app.delete('/country/Sudan')
    #     # assert b'Item Sudan deleted' in rv.data

    #     rv = self.app.post('/country/Sudan', data=wrong_data, headers={'Content-Type': 'application/json'})
    #     assert b"Data is not correct." in rv.data

    def test_country_post_correct(self):
        data = {
            "population": "44.909.353",
            "land_area": "1.886.068",
            "migrants": "150.158",
            "medium_age": "28",
            "urban_pop": "31%"
            }
        rv = self.app.post('/country/Sudan', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        assert b'Sudan' in rv.data

    def test_country_post_repeat(self):
        data = {
            "population": "44.909.353",
            "land_area": "1.886.068",
            "migrants": "150.158",
            "medium_age": "28",
            "urban_pop": "31%"
            }
        rv = self.app.post('/country/Sudan', data=data) # , follow_redirects=True
        assert b'An item with name Sudan already exists.' in rv.data

    # delete --------------------------------------------

    def test_country_del(self):
        rv = self.app.delete('/country/Sudan')
        assert b'Item Sudan deleted' in rv.data

if __name__ == '__main__':
    unittest.main()