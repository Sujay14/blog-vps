import uuid
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

import boto3
from starlette.concurrency import run_in_threadpool
from config import settings

# PROFILE_PICS_DIR = Path("media/profile_pics")

def _get_s3_clients():
    return boto3.client(
        "s3",
        region_name=settings.s3_region,
        aws_access_key_id=(
            settings.s3_access_key_id.get_secret_value()
            if settings.s3_access_key_id
                else None
        ),
        aws_secret_access_key=(
            settings.s3_secret_access_key.get_secret_value()
            if settings.s3_secret_access_key
                else None
        ),
        endpoint_url=settings.s3_endpoint_url,
    )
def process_profile_image( content:bytes) -> tuple[bytes,str]:
    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original)

        img = ImageOps.fit(img, (300,300), method=Image.Resampling.LANCZOS)

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        filename = f"{uuid.uuid4().hex}.jpg"
        # filepath = PROFILE_PICS_DIR / filename

        output = BytesIO()

        # PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)

        img.save(output,"JPEG", quality=85, optimze= True)
        output.seek(0)


    return output.read(), filename 


# upload to s3
def _upload_to_s3(file_bytes, key: str) -> None:
    print("Bucket:", settings.s3_bucket_name)
    print("Uploading:", key)

    s3 = _get_s3_clients()

    s3.upload_fileobj(
        BytesIO(file_bytes),
        settings.s3_bucket_name,
        key,
        ExtraArgs={"ContentType": "image/jpeg"},
    )

    print("Upload completed!")

def _delete_from_s3(key: str) -> None:
    s3 = _get_s3_clients()
    s3.delete_object(Bucket=settings.s3_bucket_name, Key=key)

async def upload_profile_image(file_bytes: bytes, filename: str) -> None:
    key = f"profile_pics/{filename}"

    print("KEY =", key)

    await run_in_threadpool(_upload_to_s3, file_bytes, key)

    print("Finished upload_profile_image()")
    
async def delete_profile_image(filename:str |  None)-> None:
    if filename is None:
        return
    key = f"profile_pics/{filename}"
    print("🗑️ Attempting to delete:", key)

    await run_in_threadpool(_delete_from_s3, key)
    print("✅ delete_profile_image finished")

# def delete_profile_image(filename: str| None)-> None:
#     if filename is None:
#         return
    
#     filepath = PROFILE_PICS_DIR / filename
#     if filepath.exists():
#         filepath.unlink() 
        