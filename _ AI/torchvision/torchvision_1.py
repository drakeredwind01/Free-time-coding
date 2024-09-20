from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id)

import torch

def generate_image(prompt):
  """Generates an image based on the given prompt."""

  # Set device (GPU or CPU)
  device = "cuda" if torch.cuda.is_available() else "cpu"
  pipe = pipe.to(device)

  # Generate image
  image = pipe(prompt, guidance_scale=7.5, num_inference_steps=30).images[0]

  return image

# Example usage
prompt = "A person painting a beautiful landscape."
image = generate_image(prompt)
image.save("painting_landscape.png")