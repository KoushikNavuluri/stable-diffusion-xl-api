# Stable Diffusion XL ( API )

   Reverse engineered API of Stable Diffusion XL 1.0 ( Midjourney Alternative ) via https://replicate.com/ , A text-to-image generative AI model that creates beautiful 1024x1024 images.

<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/d1022d40-05f0-4d2d-a37e-8cab7d444bec" width="900" >   

# Table of Contents

- [Stable Diffusion XL ( API )](#stable-diffusion-xl---api--)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Send Prompt to generate image](#send-prompt-to-generate-image)
    + [Output](#output)
  * [Example Images Generated](#example-images-generated)
  * [Advanced Generation using parameters](#advanced-generation-using-parameters)
    + [List of parameters](#list-of-parameters)
  * [CLI Version](#cli-version)
  * [Disclaimer](#disclaimer)
  * [License](#license)

## Prerequisites

To use this API, you need to have the following:

Python installed on your system
requests library installed 
```bash
  pip install requests

```

## Installation

To use the Claude AI Unofficial API, you can either clone the GitHub repository or directly download the Python file.

Terminal :

    pip install sdxl
    
or

Clone the repository:

    git clone https://github.com/KoushikNavuluri/stable-diffusion-xl-api.git

## Usage
Import the claude_api module in your Python script:

    from sdxl import ImageGenerator

* Next, you need to create an instance of the ImageGenerator class:
  
```bash
client = ImageGenerator()
```
## Send Prompt to generate image
```bash
images = sdxl.gen_image(
    "Vibrant, Headshot of a serene, meditating individual surrounded by soft, ambient lighting.")
print(images)
```

### Output
<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/5f362c03-d8f1-462c-873a-40e47bdaea63" width="600" >

## Example Images Generated

<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/eb1976ac-0cf7-4817-9116-bd7384282380" width="200" >

<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/9bcfa7de-338e-48ca-a008-a068236d052c" width="200">

<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/a7ad3bc8-431a-40d3-a43f-aec9426b8f18" width="200" >

<img src="https://github.com/KoushikNavuluri/stable-diffusion-xl-api/assets/103725723/1fd90d12-aaba-4fce-bf94-2077355a5d41" width="200">



## Advanced Generation using parameters

```bash
#Parameters set to their default values
images = sdxl.gen_image(prompt=
    "Vibrant, Headshot of a serene, meditating individual surrounded by soft, ambient lighting.",count=1, width=1024, height=1024, refine="expert_ensemble_refiner", scheduler="DDIM", guidance_scale=7.5, high_noise_frac=0.8, prompt_strength=0.8, num_inference_steps=50)
print(images)
```
### List of parameters

      *   prompt = Input text prompt
      *   width  = Width of output image(max:1024)
      *   height = height of output image(max:1024)
      *   count  = Number of images to output. (minimum: 1; maximum: 4) 
      *   refine = Which refine style to use ( no_refiner or expert_ensemble_refiner or base_image_refiner )
      *   scheduler = scheduler (valid_schedulers = ["DDIM" or "DPMSolverMultistep" or "HeunDiscrete" or "KarrasDPM" or "K_EULER_ANCESTRAL" or "K_EULER" or "PNDM"])
      *   guidance_scale = Scale for classifier-free guidance (minimum: 1; maximum: 50) 
      *   prompt_strength = Prompt strength in image (maximum: 1) 
      *   num_inference_steps = Number of denoising steps (minimum: 1; maximum: 500) 
      *   high_noise_frac = for expert_ensemble_refiner, the fraction of noise to use (maximum: 1)
      
## CLI Version

For cli version you can check example folder in this repository (filename:cli.py)

> How to:

```bash
python main.py "beautiful landscape with two kittens,realistic,4k" --count 1 --width 1024 --height 1024 --refine expert_ensemble_refiner --scheduler DDIM --guidance_scale 7.5 --high_noise_frac 0.6 --prompt_strength 0.9 --num_inference_steps 40

```

## Disclaimer

This project provides an unofficial API for Replicate's Stable Diffusion XL and is not affiliated with or endorsed by Replicate or Stable Diffusion. Use it at your own risk.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.

