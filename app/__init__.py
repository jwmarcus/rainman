# Standard library imports
from contextlib import asynccontextmanager

# Related third party imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

# Local application/library specific imports
from .routers import root, weather

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load a shared AsyncClient for the lifespan of the application
    app.state.client = httpx.AsyncClient()
    yield
    # Close the shared AsyncClient when the application is shutting down
    await app.state.client.aclose()

app = FastAPI(lifespan=lifespan)

# The `origins` list contains the allowed origins for CORS (Cross-Origin Resource Sharing).
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(root.router)
app.include_router(weather.router)
