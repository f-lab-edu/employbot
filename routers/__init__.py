from fastapi import FastAPI, Body, Request, APIRouter
import json

from SlackAPI import *

router = APIRouter(
    prefix="/search",
)