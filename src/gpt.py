import sys
import os
import openai
from config import GPT3_API_KEY

openai.api_key = GPT3_API_KEY
openai.Model.list()

#create base prompt
s_prompt_0 = """
Pretend you are an expert software developer that specializes in python, sql, and bash shell scripting, and someone asks you the following question: 
"""

#add prompt from command line to base prompt
s_prompt_1 = sys.argv[1]
s_prompt = s_prompt_0 + s_prompt_1

# define the model, max tokens, and temperature
s_model="text-davinci-003"
n_max_tokens=250
n_temperature = 0.9

# generate the answer
completion = openai.Completion.create(model=s_model,prompt=s_prompt,max_tokens=n_max_tokens,temperature=n_temperature)
answer = completion.choices[0].text
#remove \n from answer
answer = answer.replace("\n", "")

# print the completion
print(f'Prompt: {s_prompt}')
print('')
print(f'{s_model} Answer: {answer}')