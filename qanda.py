import openai

openai.api_key = "PUT API KEY HERE"
completion = openai.Completion()

default_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

def ask(question, chat_log=None):

	if chat_log is None:
		chat_log = default_log
	
	prompt = f'{chat_log}Human: {question}\nAI:'
	response = completion.create(
		prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
		top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
		max_tokens=150)
	
	answer = response.choices[0].text.strip()
	return answer

if __name__ == "__main__":
	while True:
		
		question = input("Q: ")
		answer = ask(question)
		print(answer)
