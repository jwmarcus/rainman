from fastapi import APIRouter, Depends
from starlette.requests import Request
import httpx

router = APIRouter()

# This function is a dependency that will be used to inject the shared AsyncClient into the route handlers.
# It avoids the need to create a new AsyncClient for each request.
# It also avoids circular imports by using the request.app.state.client to access the shared AsyncClient.
def get_http_client(request: Request):
    return request.app.state.client

@router.get("/")
async def index():
    return {"message": "..:: goliath online ::.."}

@router.get("/joke")
async def read_joke(client: httpx.AsyncClient = Depends(get_http_client)):
    response = await client.get('https://api.api-ninjas.com/v1/dadjokes?limit=1')
    print(response.json())
    return response.json()