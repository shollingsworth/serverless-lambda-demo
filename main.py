#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entrypoint."""
import datetime
import os

from aws_lambda_powertools.logging.logger import Logger
from fastapi.applications import FastAPI
from mangum import Mangum

app = FastAPI(title="Serverless Demo")
handler = Mangum(app)

LOG = Logger(child=True)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG.setLevel(LOG_LEVEL)


@app.get("/")
async def hello_world():
    """Test env."""
    LOG.info("Hello World !")
    return "Hello World !!!!"


def rate(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    LOG.debug("Event: %s", event)
    LOG.info(f"RATE function {name} ran at {current_time}")


def cron(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    LOG.debug("Event: %s", event)
    LOG.info(f"CRON function {name} ran at {current_time}")
