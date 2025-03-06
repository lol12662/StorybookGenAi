from flask import Flask, render_template, request
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, pipeline
from datasets import load_dataset, DatasetDict, Dataset

app = Flask(__name__)


story_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")


def generate_story(prompt):
    """Generate a structured children's story with better coherence."""
    response = story_generator(
        f" {prompt}. \n",
        max_length=300,  
        num_return_sequences=1,
        temperature=0.7  
    )
    return response[0]["generated_text"]


from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

def generate_image(description):
    """Generate an image using Stable Diffusion."""
    image = pipe(description).images[0]
    image_path = "static/story_image.png"
    image.save(image_path)
    return image_path


@app.route("/", methods=["GET", "POST"])
def home():
    story = None
    image_url = None

    if request.method == "POST":
        prompt = request.form["prompt"]
        story = generate_story(prompt)
        image_url = generate_image(prompt)  

    return render_template("index2.html", story=story, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)

