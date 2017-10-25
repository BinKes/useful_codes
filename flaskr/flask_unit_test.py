#coding=utf8  
from flask import Flask,jsonify, Blueprint, render_template
from flask_testing import TestCase  
import unittest
from lib.server.mod_analytics.controllers import analyze_single_test, mod_analytics
from lib.server import app
import urllib.request
#from flask_testing import LiveServerTestCase

#app = Flask(__name__)  
page = Blueprint('page', __name__,
                    template_folder='templates')

@app.route("/ajax/")  
def some_json():  
    return jsonify(success=True)

@page.route('/')
def hello():
    return render_template('hello.html')

app.register_blueprint(page)

class TestViews(TestCase):
    render_templates = False

    def create_app(self):  
        app.config['TESTING'] = True
        return app  

    def test_some_json(self):  
        response = self.client.get("/ajax/")  
        ''''' 
                判断还回的JSON对像是不是{'success':True} 
        '''
        print(response)
        self.assertEqual(response.json, dict(success=True))

    def test_empty_db(self):
        rv = self.client.get('/')
        assert b'Not Found' not in rv.data
        #print(rv.data)

    '''def test_isjson(self):
        tjson = {

            "userIdentifier": "100000001",
            "datetime": "2016-10-25T01:35:01.411Z",
            "namespace": "JKOM",
            "isEmptyStomach": True,
            "profile": {
                "gender": "male",
                "age": 36,
                "dob": "1980-01-01",
                "weight": 175,
                "height": 65
            },
            "attributes": {
                "st_bp": "a",
                "st_diabetes": "a",
                "st_cvd": "a",
                "hs_hd": "a"
            },
            "samples": [
                {
                "name": "TC",
                "value": 5.2,
                "unit": "mmol/L",
                "metadata": "{\"aa\": 1}"
                },
                {
                "name": "GLU",
                "value": 6.5,
                "unit": "mmol/L",
                "metadata": "{}"
                },
                {
                "name": "TG",
                "value": 6.0,
                "unit": "mmol/L",
                "metadata": "{}"
                },
                {
                "name": "diastolic",
                "value": 111,
                "unit": "mmHg",
                "metadata": "{}"
                },
                {
                "name": "HDL-C",
                "value": 1.1,
                "unit": "mmol/L",
                "metadata": "{}"
                },
                {
                "name": "LDL-C",
                "value": 3.8,
                "unit": "mmol/L",
                "metadata": "{}"
                },
                {
                "name": "LP(a)",
                "value": 2,
                "unit": "mg/L",
                "metadata": "{}"
                },
                {
                "name": "Apo-A1",
                "value": 1.2,
                "unit": "g/L",
                "metadata": "{}"
                },
                {
                "name": "Apo-B",
                "value": 1.6,
                "unit": "g/L",
                "metadata": "{}"
                },
                {
                "name": "Hcy",
                "value": 20,
                "unit": "umol/L",
                "metadata": "{}"
                }
            ]
            }

        
        response = self.client.post('/analytics/single-test', 
            headers={"Authorization": "Basic {user}".format(user=b"jk724:5ylt/pD8522A6N2C/qD76A==")})
        print(response.data)'''

    
if  __name__ =='__main__':  
    unittest.main()