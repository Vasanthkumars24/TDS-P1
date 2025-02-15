def execute_task_a7():
    with open("/data/email.txt", "r") as file:
        email_content = file.read()

    # Use the LLM to extract the sender's email
    response = requests.post(
        "https://api.aiproxy.io/v1/completions",
        headers={"Authorization": f"Bearer {AIPROXY_TOKEN}"},
        json={"prompt": f"Extract the sender's email from this email: {email_content}", "max_tokens": 50}
    )
    sender_email = response.json()["choices"][0]["text"].strip()

    # Write the sender's email to a new file
    with open("/data/email-sender.txt", "w") as file:
        file.write(sender_email)
