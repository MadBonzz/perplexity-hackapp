from openai import OpenAI
import pymupdf4llm
from tqdm import tqdm

llm_id = 'gemma-3-4b-it'
server_url = 'http://127.0.0.1:1234/v1'
gen_client = OpenAI(base_url=server_url, api_key="lm-studio")
output_path = 'extracted_questions_2013.txt'

system_prompt = {
            "role": "system",
            "content": "You are an AI data extraction assistant. You help the user extract the relevant data from the text provided",
    }

user_prompt = """
You will be provided a question, its options, the correct answer and the explanation/solution behind the answer in a raw and unclean format.
Your work is to extract the question, options, correct answer and the solution and provide them in a clean manner.
Provide the correct answer from the options rather than providing the correct option.
In your answer, provide the solution as it is from the provided raw text rather than relying on your own knowledge
You should provide your output in xml tags as 
<question>The question here</question>
<options>The options separated by comma here</options>
<answer>The correct answer</answer>
<solution>The solution/explanation behind the answer</solution>

The question provided is : 
{question}
"""

paper_path = 'NEET-PG-2013-Question-Paper-With-Solutions.pdf'
text = pymupdf4llm.to_markdown(paper_path)
questions = text.split('# **')[1:]

for question in tqdm(questions):
    if len(question) < 10:
        continue
    context = gen_client.chat.completions.create(
        model=llm_id,
        messages=[
            system_prompt,
            {
                "role" : "user",
                "content" : user_prompt.format(
                    question=question
                )

            }
        ],
        temperature=0.5
    )

    context = context.choices[0].message.content
    context = context.replace('**', '').replace('\n', '')
    with open(output_path, 'a', encoding='utf-8') as f:
        f.write(context + '\n')
