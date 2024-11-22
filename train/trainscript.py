from transformers import BioGptForCausalLM, BioGpttokeniser, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset
import pandas as pd
import torch


# main function to set up and run training
def main():

    # load data as dataframe using pandas
    df = pd.read_json('data/data_preprocessed.json')

    # convert dataframe to Hugging Face dataset
    dataset = Dataset.from_pandas(df)

    # load BioGPT and respective tokeniser
    tokeniser = BioGpttokeniser.from_pretrained("microsoft/biogpt")
    model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")

    # method to tokenise the dataset with max_length specified
    def tokenise_function(examples):
        return tokeniser(examples['Symptom Description'], padding="max_length", truncation=True, max_length=128)

    # apply tokenise_function
    tokenised_dataset = dataset.map(tokenise_function, batched=True)

    # use DataCollator for padding/truncation during training
    data_collator = DataCollatorForLanguageModeling(tokeniser=tokeniser, mlm=False)

    # trainer config
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir="./logs"
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenised_dataset,
        eval_dataset=tokenised_dataset,
        data_collator=data_collator
    )

    # start training
    trainer.train()

if __name__ == "__main__":
    main()
