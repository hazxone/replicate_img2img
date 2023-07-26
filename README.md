# Replicate img2img model in the style of Van Gogh

This is an img2img in the style of Van Gogh.
It was written in cog format to be push to replicate.com

The diffusion model is from https://replicate.com/cjwbw/van-gogh-diffusion

cog.yaml is specify the dependencies and python libraries

predict.py is to consume input (image and prompt) and run the input through the diffusion model

&nbsp;

## Cog process
```
cog init
```
To initialize the directory

```
cog predict -i prompt="lvngvncnt, a kid holding a balloon -i image=@balloon.jpg"
```

This will build locally and do inference to the image balloon.jpg
```
cog login
cog push r8.im/hazxone/img2img-vg
```
This will add credential and push the build to replicate.com

&nbsp;

## Inference process

Head over to https://replicate.com/hazxone/img2img-vg to try the web demo

For this Van Gogh model, the author suggested to use 'lvngvncnt' in the begging of the prompt.
