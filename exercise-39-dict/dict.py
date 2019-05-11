states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
print('- ' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
print('- ' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
print('- ' * 10)
print(cities['NY'])
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
