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
<<<<<<< HEAD
    zoom = 2 if zoom > 2 else zoom
    scale = 16 * (16 - zoom * (10 - zoom * 2))
=======
    zoom = 15 if zoom > 15 else zoom
    scale = 16 * (16 - zoom)
>>>>>>> parent of a395ccd (last zoom fix)
    chunk = layer.getInts(x * scale, z * scale, scale, scale)
    image = gl.getImage(chunk, scale, scale).resize((256, 256), BOX)
    buffer = BytesIO()
    image.save(buffer, "png")
    return StreamingResponse(BytesIO(buffer.getvalue()))
