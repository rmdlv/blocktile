from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from io import BytesIO

from mcbiomes import genLayer as gl

app = FastAPI()


@app.get("/{seed}/{zoom}/{x}/{z}.jpg")
def tile(seed: int, zoom: int, x: int, z: int):
    layer = gl.genlayer(seed)
    if zoom > 16:
        zoom = 16
    scale = 16 * zoom
    image = gl.getImage(
        layer.getInts(
            int((x / scale) * scale),
            int((z / scale) * scale),
            scale,
            scale,
        ),
        scale,
        scale,
    )
    buffer = BytesIO()
    image.save(buffer, "jpeg")
    return StreamingResponse(BytesIO(buffer.getvalue()))
