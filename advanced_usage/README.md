# Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building style transfer models. 

## Tips and "Gotchas"

-  **Training Data**: In order for a style transfer model to detect the content of the training images, it must be provided with many examples of the kinds of content you wish to apply style images to. For example, to extract the features of images of people, many images must be provided to the model so that the model can understand how to apply style to the arms and head of the person's body. This is similar to image classification problems where new classifications perform better when the underlying model has been trained on "similar" data.
-  **Model Runtime**: The out-of-the box model takes a long time to train on CPU. Unfortunately, even for a small number of images, it can take multiple days to run on CPU. Also, set `max_iterations` lower in the `turicreate.image_classifier.create` function if you want something to train quickly (at the cost of reduced accuracy).


## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://metismachine-skafos.slack.com/join/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also checkout Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/image_classifier/) on image classification basics.
