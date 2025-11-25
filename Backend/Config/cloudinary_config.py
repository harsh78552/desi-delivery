import cloudinary
import cloudinary.uploader
import certifi
import ssl

# Create an SSL context using certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

cloudinary.config(
    cloud_name="dofbbfgg4",
    api_key="596269484844184",
    api_secret="0uzI8tt4-bGFwAZuTfOiEMEQD2o",
    secure=True
)
