# Dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington Dc',
            'India':'New Delhi',
            'China':'Beijing',
            'Rusia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # update to add or change existing
capitals.update({'USA':'Las Vegas'})
capitals.pop('China') # pop for remove
capitals.clear()

# print(capitals['Rusia'])
# print(capitals.get('Germany'))
# print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key, value)

