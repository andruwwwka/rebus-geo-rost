from yandex_geocoder import Client

def decode_string(address):
    coords = Client.coordinates(address)
    return coords

print(decode_string('ул.Ленина, д.1'))
