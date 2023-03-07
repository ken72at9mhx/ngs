import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
print()
info = 'speak polish'
completion = openai.Completion.create(
    engine=model_engine,
    prompt=info,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)
response = completion.choices[0].text
print(response)


while True:
    model_engine = "text-davinci-003"
    print()
    info = str(input("Message: "))

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=info,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    response = completion.choices[0].text
    print(response)
