# Turi Style Transfer

The following repo contains code for training a style transfer a model on Skafos using the Turi Create framework.

As much as possible, the code in this repo mimicks Turi Create's style transfer example which can be found [here](https://apple.github.io/turicreate/docs/userguide/style_transfer/). 

## What is here?

The two main components to this repo are:
- `style_transfer.py` - a Skafos job that trains a style transfer model and saves a core ml model
- `style_transfer.ipynb` - a python notebook with the same code as the above `style_transfer.py` job.

Additionallly, there exists:
- `metis.config.yml` - a file telling Skafos how the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- To get this to run, the model required training images. Specifically, *style* and *content* images.
- The images for this project came from [Pexels.com](https://www.pexels.com/) as it has many free images available.
- For this project, we highly recommend running it on  a GPU. We encourage you to do this once you've changed the data to reflect your use case. As benchmarks, we've found this takes about 90 minutes on a GPU and about 3 days on Skafos with 6 CPU's and 10G of memory. This can take considerably more time locally using only CPU. 