from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import bedrock_agent
import embeddings
from fastapi.middleware.cors import CORSMiddleware
from agent import agent_func

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://182.72.211.14"
]


app.add_middleware(
    CORSMiddleware,    
    allow_origins=["*"],    
    allow_credentials=True,    
    allow_methods=["*"],    
    allow_headers=["*"]
    )

class UserQuery(BaseModel):
    user_input: str

@app.get("/")
def home():
    print("working")
    return { "response": "working" }
    
@app.post("/agent")
def agent(user_query: UserQuery):
    print("user_query.user_input: ",user_query.user_input)
    response = agent_func(user_query.user_input)
    return { "response": response}

@app.post("/agent2")
def agent2(user_query: UserQuery):
    print("user_query.user_input: ",user_query.user_input)
    messages = bedrock_agent.get_user_messages(str(user_query.user_input))
    return { "response": messages}

@app.post("/data-ingestion")
def ingestion():
    docs = embeddings.data_ingestion()
    embeddings.get_vector_store(docs)
    return { "response": docs}
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)