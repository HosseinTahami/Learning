from boto3.session import Session
from django.conf import settings


class Bucket:

    """CDN Bucket manager

    init method creates connection.

    NOTE:
        None of these methods are async so, use public interface in tasks.py modules instead.
    """

    def __init__(self):
        session = Session()
        self.connection = session.client(
            service_name=settings.AWS_SERVICE_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

    def get_objects(self):
        results = self.connection.list_objects_v2(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if results['KeyCount']:
            return results['Contents']
        return None


bucket = Bucket()
