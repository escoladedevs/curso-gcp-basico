import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'demonstracao-cloud-storage-f4c79e7bb5dd.json'

storage_client = storage.Client()   

my_bucket = storage_client.get_bucket('mycloudstorage9999')


def upload_to_bucket(file_name, path, bucket_name):

       try:
            bucket = storage_client.get_bucket(bucket_name)
            file_to_upload = bucket.blob(file_name)
            file_to_upload.upload_from_filename(path)
            return True

       except Exception as e:
              print(e)
              return False

file_path = r'C:\Users\gcp\Desktop'

#upload_to_bucket('estrutura-curso.png', os.path.join(file_path, 'estrutura-curso.png'), 'mycloudstorage9999')


def download_file_from_bucket(file_name, path, bucket_name):
       try:
              bucket = storage_client.get_bucket(bucket_name);
              file_to_download = bucket.blob(file_name)
              with open(path, 'wb') as f:
                     storage_client.download_blob_to_file(file_to_download, f)
              return True
       
       except Exception as e:
              print(e)
              return False
              
download_file_from_bucket('estrutura-curso.png', os.path.join(os.getcwd(), 'estrutura-curso.png'), 'mycloudstorage9999')
