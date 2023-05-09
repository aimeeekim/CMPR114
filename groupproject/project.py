import openai
import time

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to get GPT-3 response
def get_gpt_response(prompt, model, engine):
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            model=model,
            temperature=0.8,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Define a dictionary of available models and engines
models = {
    "davinci": ["davinci", "davinci-codex"],
    "curie": ["curie", "curie-instruct-beta"],
}

# Define a list of available topics
topics = ["Python", "Machine Learning", "Data Science", "Web Development"]

# Define a tuple of greeting messages
greetings = ("Hi there! I'm ChatGPT. How can I assist you?", 
             "Hello! How can I help you today?", 
             "Greetings! What can I do for you?")

# Define a class to handle ChatGPT session
class ChatGPT:
    def __init__(self):
        self.model = models["davinci"][0]
        self.engine = models["davinci"][1]

    def run(self):
        print("\n" + "-"*40)
        print(greetings[0])

        while True:
            try:
                user_input = input("You: ").strip().lower()
                if user_input == "exit":
                    print("ChatGPT: Goodbye!")
                    break

                elif user_input.startswith("change model"):
                    model_name = user_input.split()[-1].lower()
                    if model_name in models:
                        self.model = models[model_name][0]
                        self.engine = models[model_name][1]
                        print(f"ChatGPT: Model changed to {model_name.capitalize()}.")
                    else:
                        print(f"ChatGPT: Model {model_name} not found. Please try again.")

                elif user_input == "topics":
                    print("ChatGPT: Available topics are:")
                    for i, topic in enumerate(topics, start=1):
                        print(f"{i}. {topic}")

                elif user_input.startswith("topic"):
                    topic_index = int(user_input.split()[-1]) - 1
                    if topic_index < len(topics):
                        topic = topics[topic_index]
                        prompt = f"What are some key concepts in {topic}?"
                        response = get_gpt_response(prompt, self.model, self.engine)
                        print(f"ChatGPT: {response}")
                    else:
                        print(f"ChatGPT: Invalid topic index. Please try again.")

                elif user_input.startswith("repeat"):
                    n = int(user_input.split()[-1])
                    for i in range(n):
                        print(f"ChatGPT: Repeating {i+1}/{n}...")
                        time.sleep(1)

                else:
                    prompt = f"{user_input}"
                    response = get_gpt_response(prompt, self.model, self.engine)
                    print(f"ChatGPT: {response}")

            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    chatbot = ChatGPT()
    chatbot.run()
