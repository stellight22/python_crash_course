#Ch11 test that the data has been stored
class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("survey results:")
        for response in responses:
            print('- ' + response)

