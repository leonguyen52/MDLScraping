from typing import Dict, Any

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

# bypassing cloudflare anti-bot
import cloudscraper

from api.utils import search_func, fetch_func


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index() -> str:
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MDL Scraper API</title>
        <style>
            body {
                background-color: #f8f8f8;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            .container {
                margin: 0 auto;
                max-width: 800px;
                padding: 20px;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 20px;
                text-align: center;
            }
            p {
                font-size: 24px;
                line-height: 1.5;
                text-align: center;
            }
            code {
                background-color: #f4f4f4;
                border-radius: 3px;
                color: #333;
                display: block;
                font-family: monospace;
                font-size: 16px;
                padding: 10px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>MDL Scraper API</h1>
            <p>This is a simple API that scrapes information from MyDramaList.com</p>
            <code>Try making a request to /search/q=&lt;drama_name&gt;</code>
        </div>
    </body>
    </html>
    """


@app.get("/search/q/{query}")
async def search(query: str, response: Response) -> Dict[str, Any]:
    code, r = await search_func(query=query)

    response.status_code = code
    return r


@app.get("/id/{drama_id}")
async def fetch(drama_id: str, response: Response) -> Dict[str, Any]:
    code, r = await fetch_func(query=drama_id, t="drama")

    response.status_code = code
    return r


@app.get("/id/{drama_id}/cast")
async def fetch_cast(drama_id: str, response: Response) -> Dict[str, Any]:
    code, r = await fetch_func(query=f"{drama_id}/cast", t="cast")

    response.status_code = code
    return r


@app.get("/id/{drama_id}/reviews")
async def fetch_reviews(
    drama_id: str, response: Response, page: int = 1
) -> Dict[str, Any]:

    code, r = await fetch_func(query=f"{drama_id}/reviews?page={page}", t="reviews")

    response.status_code = code
    return r


@app.get("/people/{person_id}")
async def person(person_id: str, response: Response) -> Dict[str, Any]:
    code, r = await fetch_func(query=f"people/{person_id}", t="person")

    response.status_code = code
    return r


# get seasonal drama list -- official api available, use it with cloudflare bypass
@app.get("/seasonal/{year}/{quarter}")
async def mdlSeasonal(year: int, quarter: int) -> Any:
    # year -> ex. ... / 2019 / 2020 / 2021 / ...
    # quarter -> every 3 months (Jan-Mar=1, Apr-Jun=2, Jul-Sep=3, Oct-Dec=4)
    # --- seasonal information --- winter --- spring --- summer --- fall ---

    scraper = cloudscraper.create_scraper()

    return scraper.post(
        "https://mydramalist.com/v1/quarter_calendar",
        data={"quarter": quarter, "year": year},
    ).json()
