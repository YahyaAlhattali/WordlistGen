
from fastapi import FastAPI
import subprocess
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://192.168.100.9",
    "http://192.168.100.9:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os

# checking if the directory demo_folder
# exist or not.
if not os.path.exists("/tmp/wordlist"):
    # if the demo_folder directory is not present
    # then create it.
    os.makedirs("/tmp/wordlist")


@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/range_of_numbers") # 1-999
def read_root(first_number: int, second_number: int):
 with open('/tmp/wordlist/Final.txt','a') as tmp_file:
  for i in range(first_number,second_number+1):
    tmp_file.write(str(i)+'\n')
 tmp_file.close()
 return ('True')

@app.post("/text_number") # Oman@2020
def read_root(first_text: str, first_number: int ,second_number: int):
 with open('/tmp/wordlist/Final.txt','a') as tmp_file:
  for i in range(first_number,second_number+1):
    tmp_file.write(first_text+str(i)+'\n')
 tmp_file.close()
 return ('True')

@app.post("/add") # Oman@2020
def read_root(first_text: str):
 with open('/tmp/wordlist/Final.txt','a') as tmp_file:
    tmp_file.write(first_text+"\n")
 tmp_file.close()
 return ('True')
