from fastapi import FastAPI, Body

from pydantic.main import BaseModel
from routers import total_search, form_search, menu
import uvicorn

app = FastAPI()
app.include_router(total_search.router)
app.include_router(form_search.router)
app.include_router(menu.router)

class SlackModel(BaseModel):
    token: str
    challenge: str
    type: str

@app.post("/")
async def post_message(request_body: SlackModel = Body(...)):
    response = {"challenge": request_body.challenge}
    print(response)
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
