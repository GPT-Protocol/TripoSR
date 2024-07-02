from minio import Minio
from os import environ

minio_client = Minio(environ["MINIO_ENDPOINT"],
    access_key=environ["MINIO_ACCESS_KEY"],
    secret_key=environ["MINIO_SECRET_KEY"],
)

minio_bucket_name = "test1"