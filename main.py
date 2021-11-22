from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from io import BytesIO

from mcbiomes import genLayer as gl

app = FastAPI()


@app.get("/{seed}//{x}/{z}.jpg")
def tile(seed: int, x: int, z: int):
    layer = gl.genlayer(seed)
    image = gl.getImage(
        layer.getInts(
            int(x / 16),
            int(z / 16),
            16,
            16,
        ),
        16,
        16,
    )
    buffer = BytesIO()
    image.save(buffer, "jpeg")
    return StreamingResponse(BytesIO(buffer.getvalue()))
