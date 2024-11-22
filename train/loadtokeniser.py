from transformers import AutoTokenizer, AutoModelForCausalLM

# load BioGPT tokeniser
tokeniser = AutoTokenizer.from_pretrained("microsoft/biogpt")

# save tokeniser to fine-tuned model checkpoint dir
tokeniser.save_pretrained("results/checkpoint-972")
