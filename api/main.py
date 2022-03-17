import uvicorn

from collections import deque
from fastapi import FastAPI

from api.models import RovPosition

app = FastAPI(
    title="Remora Message Center",
    description="Handler Remora messages sent from different pens",
    version="v1.0"
)

positions = deque(maxlen=10000)

@app.get("/position/")
async def get_position():
    if positions:
        return positions.pop()
    return "No available position"


@app.post("/position/")
async def put_position(rov_position: RovPosition):
    positions.append(rov_position)
    return "position sent."



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)