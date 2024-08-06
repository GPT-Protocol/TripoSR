from minio import Minio
from os import environ
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

# Parse the MINIO_ENDPOINT to extract host and port
parsed_endpoint = urlparse(environ["MINIO_ENDPOINT"])
host = parsed_endpoint.hostname or parsed_endpoint.path
port = parsed_endpoint.port

# Construct the endpoint string
endpoint = f"{host}:{port}" if port else host

minio_client = Minio(
    endpoint,
    access_key=environ["MINIO_ACCESS_KEY"],
    secret_key=environ["MINIO_SECRET_KEY"],
    secure=False  # Set to True if you're using HTTPS
)

minio_bucket_name = "test1"
minio_generated_3d_assets_bucket = "generated-3d-assets"