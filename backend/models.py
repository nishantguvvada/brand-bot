
import boto3
bedrock=boto3.client(service_name="bedrock-runtime")
from langchain_community.llms import Bedrock

bedrock=boto3.client(service_name="bedrock-runtime")

def get_claude_llm():
    ##create the Anthropic Model
    llm=Bedrock(model_id="us.anthropic.claude-3-haiku-20240307-v1:0",client=bedrock)
    
    return llm

def get_nova_llm():
    ##create the Anthropic Model
    llm=Bedrock(model_id="us.amazon.nova-pro-v1:0",client=bedrock,
                model_kwargs={'maxTokens':512})
    
    return llm

def get_llama3_llm():
    ##create the Anthropic Model
    llm=Bedrock(model_id="us.meta.llama3-2-1b-instruct-v1:0",client=bedrock,
                model_kwargs={'max_gen_len':512})
    
    return llm
