import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What lang was your first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        #question = "What was your first language?"
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response("English")
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
       
    
    def test_store_three_responses(self):
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            self.my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

