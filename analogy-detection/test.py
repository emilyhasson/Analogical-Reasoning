import openai
import config

# Initialize the OpenAI API client
openai.api_key = config.GPT_KEY

# Your text prompt
prompt = "Translate the following English text to French: 'Hello, how are you?'"

# Make an API call to GPT-3.5 Turbo (chat model)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use GPT-3.5 Turbo model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
)

# Extract and print the generated text from the response
generated_text = response['choices'][0]['message']['content']
print(generated_text)