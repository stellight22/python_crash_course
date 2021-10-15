#Ch11 test that the data has been stored
class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def random(self,numb):
        self.number = numb

    def randomprint(self):
        print(self.number)

    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("survey results:")
        for response in self.responses:
            print('- ' + response)
    number = 3
    print(number)

survey1 = AnonymousSurvey('huh?')
survey2 = AnonymousSurvey('who?')
print("survey1")
print(survey1.number)
print("survey2")
print(survey2.number)
survey1.randomprint()
survey2.randomprint()
survey1.random(6)
survey2.random(9)
print("survey1")
print(survey1.number)
print("survey2")
print(survey2.number)
survey1.randomprint()
survey2.randomprint()
survey1.number = 7
survey1.randomprint()
survey2.randomprint()
