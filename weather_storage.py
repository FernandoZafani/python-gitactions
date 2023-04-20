from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "trans-sanctum-382223",
  "private_key_id": "9a35669927e4994e8ec66388b0b9df86f972aa2f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCkkTBSg+UBxrIQ\nZJBc+7+wsaefUbZoBhPYlZKbZZZoDv20rPKgKnxxQ979Wog0dNw47+A6EZeco8Be\n92eS/myZhW1LIC23cvcicet94j+FbEPaF43xb3y8qADiUh1j9aQqnFfyHFdgatxh\nXPoArPDkokydN9pjdpxW4j7Sr7E8TG89hyH1bCmdp3zoeWV+Y+QfcoOIM+EXIqO8\nE/ohjF6DmHKuRQupRQtiOw/C9PsYcoo6i1Ify7G7hJunNW+zsu8eEmOuNCELYMFY\nuC0ow3Sand642FW32h3wy1v3v3KJSY1rXbtcbNfmSut9I0b/chbcyN4vaG/VJssp\nCD2CnZUNAgMBAAECggEAN14X3XM9vdK9fxFulrImpMqoxEwILEh7Ld/o8vqDV6BP\nkJWtjeCtfKgioqfucoOswkVGchMQKOXZJ7picQzDugUvp9p8Nx/pcP/WBMT1rSyn\nSX2qRoRFee2mWn7ZH5P6N1HhrvYFGc3qNqHDBS4qYCoQz8aGZfd2ky7MhzMQVOIx\nbEtH5Ch6+OoqN8H4bqy2v+u3iJBNCR9O4jkCbf0AulaItiC+h3RvgY9Uma41X76n\nJ/Y9V0yDMfjQMXUpLa6d10y8NJ8iCkOBFZo81mQpxqzWzXbDRgxODaSDNHTuIYYz\nceVxrG+VZedq0ZtiiSIRnHXlvzW/Pk8hnWobSP8R2wKBgQDmyfHTtLELbhYxAxNP\naQU4NyXec3YeqyJMFYvKsQv0ucG6ieFPJW2cWlyz/8EegUSZFzugMz0AeBgnbYkL\nIfMHwGRZSl8cyWo7JOdJwbbZ1NBx4BKRsH+r6V+8TXXMYaNvq4Ry7uzH7ghZM1Vs\nW85c+poOwXGV8UNu8siatpcE5wKBgQC2i1dZ7XsvQogDNgkXgoWUC/vd/EBZrNiq\nEMFbsSF8Qx3EgVMEDJfZxnzHP/9ajm/Hakqugpwep73o11kU/R+eSsQQrbc6iuRn\nBByPCQSUeF3Z3Qhgca9NsgJHqmzqBGtozXx8vTOZaXTLdPOCnbAm67b6g48zhUWc\n3O2tSpuj6wKBgQCChHx9lLd3Vle4ehvGkgcApreE2VlYuMGZs6muBHhVe2PjIazI\n/MrDXJsGtMG7hbGMvoXa8H80L7bBPYH+SMHPhW96y8OEXSf1sMYYgTPudxs2+1il\nCeL6Du40aL4QyrsKIT6zXQmNe8E+6PgLYtQO4y6S37Vj7eCL80Ods1suywKBgEQq\niocJWJvQU2wnjIOb+PfM9dPyc7FJC2uOcDYmUiPOCFquFGsJrNbk+QmKy3dsgy9L\ncPHz0grcht1hNWHSGDGLJ+Y2iJqy7RHPBj8flfc/b4SAtrUVHup7k8BhUuScm+N6\nAIewO4mJSNUFKj3XVsVh9mVcJWiO1uz5z0OL/czbAoGAS5qZ+LrBReY3MyP7UGrz\nQNl9tNBGb4wQFi4z4TWpxHU5Cg6w6wV/MiOi8gNb4xRxqnfXLmpiU/FaF6KcIzEz\nBdsoBhi2hdqA7P9qfM0HcyFBPjrD20/nCn6cwM/zxpVWtAn6vAhnuZ8QU0xRhnhS\nwHnxcZ6yTMF7euBDdjFpOjc=\n-----END PRIVATE KEY-----\n",
  "client_email": "646374179998-compute@developer.gserviceaccount.com",
  "client_id": "105803026594360942955",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/646374179998-compute%40developer.gserviceaccount.com"
}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('3weather')
  blob = bucket.blob('weather_info.txt')

  blob.upload_from_string(info + '\n')

  print('File uploaded.')

  print("Finished.")
except Exception as ex:
  print(ex) 