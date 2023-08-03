import requests
import os
import json

class ImageGenerator:

    def __init__(self):
        pass

    def gen_image(self, prompt, count=1, width=1024, height=1024, refine="expert_ensemble_refiner", scheduler="DDIM", guidance_scale=7.5, high_noise_frac=0.8, prompt_strength=0.8, num_inference_steps=50):
        try:
            # Check if count is within the valid range
            if count < 1 or count > 4:
                raise ValueError("Count must be between 1 and 4")

            # Check if width and height are within the valid range
            if width > 1024 or height > 1024:
                raise ValueError("Width and height must be 1024 or less")

            # Check if scheduler is valid
            valid_schedulers = ["DDIM", "DPMSolverMultistep", "HeunDiscrete", "KarrasDPM", "K_EULER_ANCESTRAL", "K_EULER", "PNDM"]
            if scheduler not in valid_schedulers:
                raise ValueError("Invalid scheduler value")

            # Check if num_inference_steps is within the valid range
            if num_inference_steps < 1 or num_inference_steps > 500:
                raise ValueError("num_inference_steps must be between 1 and 500")

            # Check if guidance_scale is within the valid range
            if guidance_scale < 1 or guidance_scale > 50:
                raise ValueError("guidance_scale must be between 1 and 50")

            # Check if prompt_strength is within the valid range
            if prompt_strength > 1:
                raise ValueError("prompt_strength must be 1 or less")

            # Check if high_noise_frac is within the valid range
            if high_noise_frac > 1:
                raise ValueError("high_noise_frac must be 1 or less")

            url = "https://replicate.com/api/models/stability-ai/sdxl/versions/2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2/predictions"

            payload = json.dumps({
                "inputs": {
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                    "refine": refine,
                    "scheduler": scheduler,
                    "num_outputs": count,
                    "guidance_scale": guidance_scale,
                    "high_noise_frac": high_noise_frac,
                    "prompt_strength": prompt_strength,
                    "num_inference_steps": num_inference_steps
                }
            })

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
                'Accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://replicate.com/stability-ai/sdxl',
                'Content-Type': 'application/json',
                'Origin': 'https://replicate.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            response.raise_for_status()

            json_response = response.json()
            uuid = json_response['uuid']
            image_url = self.get_image_url(uuid)

            return image_url

        except ValueError as e:
            print(f"Error: {e}")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while making the request: {e}")
            return None

        except KeyError as e:
            print(f"Error occurred while processing the response: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def get_image_url(self, uuid):
        url = f"https://replicate.com/api/models/stability-ai/sdxl/versions/2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2/predictions/{uuid}"

        payload = {}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://replicate.com/stability-ai/sdxl',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }

        response = requests.request("GET", url, headers=headers, data=payload).json()

        if response['prediction']['status'] == "succeeded":
            output_url = response['prediction']['output_files']
            return output_url
        else:
            return self.get_image_url(uuid)
