<p  align="center"><a  href="https://github.com/rmdlv/blocktile"><img  src="https://i.imgur.com/3LY2aw6.png"  width="200px"  style="display: inline-block; border-radius: 5px"></a></p>
<h1  align="center">Blocktile</h1>

> Minecraft biome tile server writing on Python using FastAPI
## Usage
```
https://blocktile.herokuapp.com/{seed}/{zoom}/{col}/{row}.png
```
- **seed** - Random seed of the world
- **zoom** - Count of rendered chunks
- **col**, **row** - Tile numbers, calculating by multiply chunk number on zoom value
