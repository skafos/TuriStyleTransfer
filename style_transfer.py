from s3fs.core import S3FileSystem
import turicreate as tc
import os
import save_models as sm
from skafossdk import *


ska = Skafos()
s3 = S3FileSystem(anon=True)

ska.log("Pulling the style and content images from S3", labels = ['style_transfer'])
# get all the style and image paths from S3
style_paths = s3.ls("s3://skafos.example.data/StyleTransferImages/styles/")
content_paths = s3.ls("s3://skafos.example.data/StyleTransferImages/content/")
image_paths = style_paths + content_paths

# fi the local paths don't exist
for _dir in ['content', 'styles']:
    if not os.path.exists(_dir):
        os.makedirs(_dir)

ska.log("Building the necessary SFrames for model build", labels = ['style_transfer'])
# build the styles SFrame and the content SFrame
styles = tc.SFrame(); content = tc.SFrame();
for p in image_paths:
    _type = p.split("/")[-2]
    local_path = "/".join(p.split("/")[-2:])
    img1 = s3.get("s3://" + p, "./"+local_path)
    if _type == "styles":
        styles = styles.append(tc.load_images(local_path))
    if _type == "content":
        content = content.append(tc.load_images(local_path))

ska.log("Building the model", labels = ["style_transfer"])
# Create a Style Transfer model
model = tc.style_transfer.create(styles, content)

ska.log("Saving the model to Skafos", labels = ['style_transfer'])
# export to coreml
coreml_model_name = "style_transfer.mlmodel"
res = model.export_coreml(coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
                                compressed_model = compressed_model,
                                permissions = 'public')