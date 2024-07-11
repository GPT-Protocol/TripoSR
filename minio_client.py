from minio import Minio
from os import environ
from dotenv import load_dotenv

load_dotenv()
minio_client = Minio(environ["MINIO_ENDPOINT"],
    access_key=environ["MINIO_ACCESS_KEY"],
    secret_key=environ["MINIO_SECRET_KEY"],
)

minio_bucket_name = "test1"
minio_generated_3d_assets_bucket="generated-3d-assets"