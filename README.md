# Turi Style Transfer

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training a style transfer model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/style_transfer/).  The example model was trained on "style" and "content" images chosen from [Pexels.com](https://www.pexels.com), a site that provides free images for download. The style images are mostly abstract art images while the content images are images of plants. 
  
## What is here?
-  `style_transfer.ipynb` - A Python notebook that trains and saves a style transfer model to use in your app. Start here.
-  `utilities/` - a directory that contains helper functions used by `style_transfer.ipynb`.
-  `advanced_usage/` - a directory that contains additional information about the style_transfer model.
-  `requirements.txt` - a file describing all required Python dependencies.

## About the model
-  The style transfer model creates a deep learning model capable of detecting and preserving the content features in images, and then applying the color scheme and texture of style images to the content images.
-  The style transfer model is trained on abstract art images (style) and plant images (content) taken from [Pexels.com](https://www.pexels.com).
-  Once trained, you can give the model a new image and apply the color scheme and texture of each of the style images to the new image.

## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/style_transfer/) on style transfer basics.

