import openai
openai.api_key = "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"

while True:
    model = "text-davinci-003"
    user = input("Enter your question here: ")
    if 'exit' in user:
        break

    completion = openai.Completion.create(model= "text-davinci-003",
      prompt= user,
      max_tokens= 1027,
      temperature= 0.5,
      n = 1,
      stop= None)
    
    response = completion.choices[0].text
    print(response)


