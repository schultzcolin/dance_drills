import vimeo
import json 
import rich 
client = vimeo.VimeoClient(
    token='077254c4181f7d9ee0eb1b90edeef4b6',
    key='57edc58f14868708f96b4e9f7c3da072c5f7e912',
    secret='zz32GFZBxF7OeVySeAD/+Voq+6cI77Cgk2ICfoG4ipPMJVPgSBr1eR/nfGkr+W0wCY6adzo3enJuXnKArPWJfUdYzKyQ9BuljdBDGuKykDPchn+NEMrvW/XC/IK0qK8y'
  )

response = client.get("https://api.vimeo.com/videos/869052534")

response = response.json()

formatted_string = json.dumps(response, indent=2)

print(rich.print_json(formatted_string))