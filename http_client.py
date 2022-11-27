import http.client

url = "/api/people/2"

connection = http.client.HTTPSConnection("swapi.dev")
connection.request("GET", "/api/people/2")
res = connection.getresponse()

response_string = res.read().decode("utf-8")
print(response_string)




