#modifying list in a function

unprinted_models = ['AI stylist','AI trainer', 'AI finance manager', 'AI therapist', 'neural-dot', 'neural_movie', 'auto-book']
created_models = []

while unprinted_models:
    current_project = unprinted_models.pop()
    print("Now working on: "+ current_project)
    created_models.append(current_project)

print("\nDear Ahyeon, \nThe following peojects have been completed:")
for model in created_models:
    print("\t-" + model.title())