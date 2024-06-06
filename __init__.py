
import datetime
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient
import logging
import os


def function():
    """
    my function, just copy-paste your script here
    :return:
    """

    # load app settings (edit them in azure portal)
    connection_to_storage = os.environ['AzureWebJobsStorage']
    my_setting = os.environ["my-setting"]

    # load some data from a blob storage
    logging.info('connect to storage %s', connection_to_storage)
    blob_service_client = BlobServiceClient.from_connection_string(connection_to_storage)
    container_name = "sample"
    blob_container_client = blob_service_client.get_container_client(container_name)
    blob_container_client_upload = blob_service_client.get_container_client(container_name+"-json")
    blob_list_uploaded = blob_container_client_upload.list_blobs()
    uploaded_jsons = [blob.name for blob in blob_list_uploaded]
    blob_list = blob_container_client.list_blobs()
    for blob in blob_list:
        if blob.name not in uploaded_jsons:
            name = container_name+"/"+blob.name
            with open(name, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
            with open(name, "rb") as data:
                blob_client_upload = blob_container_client_upload.get_blob_client(blob.name)
                blob_client_upload.upload_blob(data)
                print("file_uploaded_successfully")


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due')
    try:
        function()
    except Exception as e:
        logging.error('Error:')
        logging.error(e)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
