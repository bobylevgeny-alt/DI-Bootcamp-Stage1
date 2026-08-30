import anthropic
client = anthropic.Anthropic()
MODEL = "claude-sonnet-5"

PROMPT = "Give a catchy 5 word slogan for a coffee shop"

# PROMPT2 = ''

tickets = [
    'My card was charg 3 times',
    'Package was wrong adress',
    'I bought a mug, not',
    'Do you have?',
]


for tiket in tickets:

    message = client.messages.create(
    model = MODEL,
    max_tokens=100,
    # temperature=0.0,
    thinking={'type': 'adaptive'},
    output_config = {'effort': 'low'},
    messages=[{'role': 'user', 'content': PROMPT}],
)
print(message.content[0].text)