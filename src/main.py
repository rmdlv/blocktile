from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO

from mcbiomes import genLayer as gl

from PIL.Image import BOX

app = FastAPI()


@app.get("/{seed}/{zoom}/{x}/{z}.png")
async def tile(seed: int, zoom: int, x: int, z: int):
    layer = gl.genlayer(seed)
    zoom = 0 if zoom < 0 else zoom
    zoom = 4 if zoom > 4 else zoom
    scale = int(256 / 2 ** zoom)
    chunk = layer.getInts(x * scale, z * scale, scale, scale)
    image = gl.getImage(chunk, scale, scale).resize((256, 256), BOX)
    buffer = BytesIO()
    image.save(buffer, "png")
    return StreamingResponse(BytesIO(buffer.getvalue()))
