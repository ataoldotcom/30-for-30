base_prompt = [
    "You are an AI assistant.",
    "Respond creatively.",
    "Site sources when possible."
]

custom_prompt = base_prompt[:]

custom_prompt.extend(["Use a friendlier tone, avoid apologies"])

print(custom_prompt)