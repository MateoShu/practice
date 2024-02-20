def get_population():
  keys = ['col', 'arg']
  values = [300, 1000]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data)) 
  return result

