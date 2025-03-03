import boto3
import json
import os

## LLm Models
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from embeddings import data_ingestion
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end but usse atleast summarize with 
250 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# system_prompt = 'You are a writing assistant to write report for a certain topic related to technical field. Give us in 200 words'
system_prompt = """
You are a intelligent chatbot give only from the contex 
"""

bedrock_runtime = boto3.client(service_name='bedrock-runtime')
# model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
# model_id = 'amazon.nova-pro-v1:0'
model_id = 'us.amazon.nova-pro-v1:0'

def ask_model(bedrock_runtime, 
               model_id, 
               system_prompt, 
               messages):
  
    body = json.dumps(
    {
            "inferenceConfig": {
            "max_new_tokens": 1000
            },
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": system_prompt
                        }
                    ]
                },
                messages
            ]
    })
    print(body)
    response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
    print(response.keys())
    response_body = json.loads(response.get('body').read().decode('utf-8'))
    print(response_body)
    return response_body


def get_user_messages(topic):
    prompt = f'Please write an article about a recently completed project in: {topic}'
    
    messages = {'role': 'assistant', 'content':[{"text":prompt}]}
    res = ask_model(bedrock_runtime, model_id, system_prompt, messages)
    # output_text = res['content'][0]['text']
    output_text = res['output']['message']['content'][0]['text']
    return output_text



def get_response_llm(llm,vectorstore_faiss,question):
    # NOT WORKING TEST LATER
    # qa = RetrievalQA.from_chain_type(
    #     llm=llm,
    #     chain_type="stuff",
    #     retriever=vectorstore_faiss.as_retriever(
    #         search_type="similarity", search_kwargs={"k": 3}
    #     ),
    #     return_source_documents=True,
    #     chain_type_kwargs={"prompt": PROMPT}
    # )
    # answer=qa({"query":question})
    # print("answer: ",answer)
    # return answer['result']  
    pass 