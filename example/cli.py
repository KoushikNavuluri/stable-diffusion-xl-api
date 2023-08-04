# basic cli example
import argparse
from sdxl import ImageGenerator


class ImageGeneratorCLI:

    def __init__(self):
        self.image_generator = ImageGenerator()

    def run(self):
        parser = argparse.ArgumentParser(description="Generate cool images using the ImageGenerator.")
        parser.add_argument("prompt", type=str, help="The text prompt for generating the image.")
        parser.add_argument("--count", type=int, default=1, help="Number of images to generate (1-4). Default: 1")
        parser.add_argument("--width", type=int, default=1024, help="Width of the generated image. Default: 1024")
        parser.add_argument("--height", type=int, default=1024, help="Height of the generated image. Default: 1024")
        parser.add_argument("--refine", type=str, default="expert_ensemble_refiner", help="Refine type. Default: expert_ensemble_refiner")
        parser.add_argument("--scheduler", type=str, default="DDIM", choices=["DDIM", "DPMSolverMultistep", "HeunDiscrete", "KarrasDPM", "K_EULER_ANCESTRAL", "K_EULER", "PNDM"], help="Scheduler type. Default: DDIM")
        parser.add_argument("--guidance_scale", type=float, default=7.5, help="Guidance scale (1-50). Default: 7.5")
        parser.add_argument("--high_noise_frac", type=float, default=0.8, help="High noise fraction (0-1). Default: 0.8")
        parser.add_argument("--prompt_strength", type=float, default=0.8, help="Prompt strength (0-1). Default: 0.8")
        parser.add_argument("--num_inference_steps", type=int, default=50, help="Number of inference steps (1-500). Default: 50")

        args = parser.parse_args()

        image_url = self.image_generator.gen_image(
            prompt=args.prompt,
            count=args.count,
            width=args.width,
            height=args.height,
            refine=args.refine,
            scheduler=args.scheduler,
            guidance_scale=args.guidance_scale,
            high_noise_frac=args.high_noise_frac,
            prompt_strength=args.prompt_strength,
            num_inference_steps=args.num_inference_steps
        )

        if image_url:
            print("Image generated successfully!")
            print("Image URL:", image_url)
        else:
            print("Failed to generate the image. Please check the input parameters.")

if __name__ == "__main__":
    image_generator_cli = ImageGeneratorCLI()
    image_generator_cli.run()
