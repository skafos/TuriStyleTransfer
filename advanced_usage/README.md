# Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building style transfer models. 

## Tips and "Gotchas"

-  **Training Data**: In order for a style transfer model to detect the content of the training images, it must be provided with many examples of the kinds of content you wish to apply style images to. 
For example, to apply style transfer to images of people, many images of people must be provided to the model so that it can understand how to apply style to the arms and head of the person's body. If a model is trained on images of objects (tables, plants, buildings, books, etc), and you subsequently try to apply this model to stylize a selfie, it will not work well.
-  **Model Runtime**: The out-of-the box model takes a long time to train on CPU. Unfortunately, even for a small number of images, it can take multiple days to run. If you want to reduce the model training time on a CPU, set `max_iterations` to a lower number in the `turicreate.style_transfer.create` function.

## Need Help?
Didn't find something you need? Confused by something? Need more guidance?

Please contact us with questions or feedback! Here are two ways:

-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos)

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/style_transfer/) on style transfer basics.
