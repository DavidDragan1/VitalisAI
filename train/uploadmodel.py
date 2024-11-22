from transformers import BioGptTokenizer, AutoModelForCausalLM
from huggingface_hub import HfApi

# define HF repo name
repo_name = "daviddragan/bio_gpt_base_1921_001275265"
model_path = "results/checkpoint-972"

# load the model and tokenizer for BioGPT
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = BioGptTokenizer.from_pretrained(model_path)

# save model and tokenizer locally in the model_path for upload
model.save_pretrained(model_path)
tokenizer.save_pretrained(model_path)

# upload to the Hugging Face Hub
model.push_to_hub(repo_name)
tokenizer.push_to_hub(repo_name)

print(f"Model successfully uploaded to https://huggingface.co/{repo_name}")
