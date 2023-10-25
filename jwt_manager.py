from jwt import encode, decode

def create_token(data: dict):
    # payload: contenido que convertire en el token
    # key: clave para el token (al momento de decifrar el token)
    # algorithm: algoritmo para el token
    token: str = encode(payload = data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithm=['HS256'])
    return data