def arby(*package):
    for p in package:
        print(p)

arby(5,'jenga')

def kirby(**google):
    for k, v in google.items():
        google[k] = v
    print(google)

print(kirby(happy = 5, l = 'loops'))
