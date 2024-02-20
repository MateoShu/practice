import utils

data = [
  {
    'Country': 'Colombia',
    'Population': 300
  },  
  {
    'Country': 'Argentina',
    'Population': 1000
  }
]

def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input('Type Country --').capitalize()
  
  result = utils.population_by_country(data, country)
  print(result)

#Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta
if __name__ == '__main__': 
  run()
