import logging
from fastapi import FastAPI
import uvicorn

from api.v1.controllers.standard_check import standard_check_controller

logging.basicConfig(
    format="u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s",
    filename='logs/logs.log',
)
app = FastAPI(title='Access-Check by Akkerman', version='0.0.1')

# controller register
app.include_router(standard_check_controller.router, prefix='/v1/standard-check', tags=['🔐 Access check'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
