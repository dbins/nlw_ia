from fastapi import FastAPI
from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.conversation import conversation

class Input(BaseModel):
    question: str

class Output(BaseModel):
    output: str

app=FastAPI()

@app.post("/conversation")
async def input(input: Input):
    output = Output(output=conversation(input.question))
    return output

origins = [
    "<http://localhost>",
    "<http://localhost:5173>"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)