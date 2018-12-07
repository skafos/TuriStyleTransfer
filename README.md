# Turi Style Transfer

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training a style transfer model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's style transfer example which can be found [here](https://apple.github.io/turicreate/docs/userguide/style_transfer/). 

## What is here?

The two main components to this repo are:
- `style_transfer.py` - a Skafos job that trains a style transfer model and saves a core ml model
- `style_transfer.ipynb` - a python notebook with the same code as the above `style_transfer.py` job.

Additionallly, there exists:
- `metis.config.yml` - a file telling Skafos how to execute the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- To get this to run, the model required training images. Specifically, *style* and *content* images.
- The images for this project came from [Pexels.com](https://www.pexels.com/) which has many free images available for download.
- For retraining this object detection model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create object detection model takes about 90 minutes on a GPU and about 3 days on Skafos with 6 CPU's and 10G of memory. Training will take considerably more time locally using only CPU. GPU support on Skafos is currently in development and will be coming soon.
