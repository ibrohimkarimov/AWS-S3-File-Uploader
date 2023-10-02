import boto3

def upload_file_to_s3(file_path, bucket_name, object_name):
    try:
        s3 = boto3.client('s3')
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"{file_path} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    file_to_upload = "example.txt"  # Change this to the file you want to upload
    bucket_name = "your-s3-bucket-name"  # Change this to your S3 bucket name
    object_name = file_to_upload

    upload_file_to_s3(file_to_upload, bucket_name, object_name)
