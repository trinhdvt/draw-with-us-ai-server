from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


def add_middleware(app: FastAPI):
    # add CORSMiddleware
    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'])

    # add GZipMiddleware
    app.add_middleware(GZipMiddleware, minimum_size=100 * 1024)  # 100KB
