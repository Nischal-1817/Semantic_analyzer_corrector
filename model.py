import streamlit as st


st.title("Correct Grammar with Transformers 🦄")
st.write("")
st.write("Input your text here!")

default_value = "Mike and Anna is skiing"
sent = st.text_area("Text", default_value, height = 50)
num_return_sequences = st.sidebar.number_input('Number of Return Sequences', min_value=1, max_value=3, value=1, step=1)

### Run Model
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = T5Tokenizer.from_pretrained('deep-learning-analytics/GrammarCorrector')
model = T5ForConditionalGeneration.from_pretrained('deep-learning-analytics/GrammarCorrector').to(torch_device)

def correct_grammar(input_text,num_return_sequences=num_return_sequences):
  batch = tokenizer([input_text],truncation=True,padding='max_length',max_length=64, return_tensors="pt").to(torch_device)
  results = model.generate(**batch,max_length=64,num_beams=2, num_return_sequences=num_return_sequences, temperature=1.5)
  #answer = tokenizer.batch_decode(results[0], skip_special_tokens=True)
  return results
  
##Prompts
results = correct_grammar(sent, num_return_sequences)

generated_sequences = []
for generated_sequence_idx, generated_sequence in enumerate(results):
    # Decode text
    text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True, skip_special_tokens=True)
    generated_sequences.append(text)

st.write(generated_sequences)
