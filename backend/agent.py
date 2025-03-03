from langchain_community.tools.reddit_search.tool import RedditSearchRun, RedditSearchSchema
from langchain_community.utilities.reddit_search import RedditSearchAPIWrapper
from langchain_community.utilities.asknews import AskNewsAPIWrapper
from langchain_community.tools.asknews import AskNewsSearch
from langgraph.prebuilt import ToolNode
from langchain.tools.retriever import create_retriever_tool
from embeddings import bedrock_embeddings, get_vector_db
from models import get_nova_llm
from langgraph.prebuilt import create_react_agent
from langchain_aws.chat_models.bedrock import ChatBedrock
from models import bedrock as bedrock_runtime

from dotenv import load_dotenv
import os
import re

load_dotenv()

# USE NOVA PRO OR LITE / CLAUDE
llm = get_nova_llm()

# TOOLS 1: REDDIT SEARCH
def agent_func(question):
    print("question: ",question)
    reddit_search_tool = RedditSearchRun(
        api_wrapper=RedditSearchAPIWrapper(
            reddit_client_id=os.getenv('REDDIT_CLIENT_ID'),
            reddit_client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            reddit_user_agent=os.getenv('USER_AGENT'),
        ),
        description="A tool that searches for posts on Reddit about the brand. Useful when you need to know customer post information on a subreddit."
    )

    reddit_search_params = RedditSearchSchema(
        query="beginner", sort="new", time_filter="week", subreddit="cocacola", limit="3"
    )
    # TOOLS 2: NEWS SEARCH

    asknews_tool = AskNewsSearch(
        api_wrapper=AskNewsAPIWrapper(
            asknews_client_id=os.getenv('ASK_NEWS_ID'),
            asknews_client_secret=os.getenv('ASK_NEWS_SECRET')    
        ),
        description="This tool allows you to perform a search on up-to-date news and historical news of the brand."
    )

    # TOOLS 3: VECTOR SEARCH

    faiss_index = get_vector_db()
    retriever = faiss_index.as_retriever(search_kwargs={"k": 4})

    vector_search = create_retriever_tool(
        retriever=retriever,
        name="analyse_customer_reviews",
        description="Analyse and returns overall feedback about the brand in 150 words",
    )

    tools = [reddit_search_tool, asknews_tool, vector_search]

    # Instance of the model

    react_agent_llm = ChatBedrock(
        model_id="us.amazon.nova-pro-v1:0",
        client=bedrock_runtime,
        #model_kwargs={"max_tokens_to_sample": 100},
        model_kwargs={"temperature": 0.5},
    )

    # Agent

    agent = create_react_agent(
        react_agent_llm,
        tools,
        state_modifier=(
            "You are a brand image analysis expert that can analyse customer reviews, posts and common public knowledge"
            "You MUST only respond in 100 words."
            "You MUST include human-readable response before transferring to another agent."
            "You MUST suggest or recommend corrective measures if you find any negative reviews about product"
        ),
    )
    response = agent.invoke({"messages": question})
    print("RESPONSE: ", type(response["messages"][0]),response["messages"][-1].content)
    clean_content = re.sub(r'<thinking>.*?</thinking>', '', response["messages"][-1].content)
    return clean_content
    # return response["messages"][-1].content
# agent_func()
    # EXTRA CODE

    # def chatbot(state: State):
    #     llm_response = llm_with_tools.invoke([
    #         {"role": "user", "content": f'{state["messages"]}'}
    #     ])
    #     return {"message": llm_response.content}

    # graph_builder.add_node("chatbot", chatbot)

    # tool_node = ToolNode(tools=tools)
    # graph_builder.add_node("tools", tool_node)

    # graph_builder.add_conditional_edges(
    #     "chatbot",
    #     tools_condition
    # )

    # graph_builder.add_edge("tools", "chatbot")
    # graph_builder.set_entry_point("chatbot")

    # graph = graph_builder.compile()
