import openai

openai.api_key = ""

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":"Write an essay about cows"}])
print(completion.choices[0].message.content)
