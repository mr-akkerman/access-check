import logging
from fastapi import FastAPI
import uvicorn

from api.v1.controllers.access_checking import simple_access_check_routes

logging.basicConfig(
    format="u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s",
    filename='logs/logs.log',
)
app = FastAPI(title='Access-Check by Akkerman', version='1.0.0')

# controller register
app.include_router(simple_access_check_routes.router, prefix='/v1/access-checking', tags=['🔐 Access check'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
