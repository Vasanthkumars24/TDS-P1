def execute_task_a8():
    # Use the LLM to extract the credit card number from the image
    with open("/data/credit-card.png", "rb") as file:
        image_data = file.read()

    response = requests.post(
        "https://api.aiproxy.io/v1/completions",
        headers={"Authorization": f"Bearer {AIPROXY_TOKEN}"},
        json={"prompt": "Extract the credit card number from this image.", "image": image_data}
    )
    card_number = response.json()["choices"][0]["text"].strip()

    # Write the card number to a new file
    with open("/data/credit-card.txt", "w") as file:
        file.write(card_number)
