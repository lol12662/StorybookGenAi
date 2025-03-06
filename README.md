# StorybookGenAi
Very simple storybook generative ai using GPT Neo and Stable Diffusion to generate text and images respectively. 

Templates is for the HTML display

Additional Folder of "Static" is needed so that Stable Diffusion can store images

#Installation

Install models and other libraries
```
pip install transformers diffusers torch accelerate torchvision torchaudio numpy

```
Additional Step if your computer uses a GPU for processing, not just a CPU
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
