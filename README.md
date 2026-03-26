# GeoSketch

An interactive web-based map tool for drawing shapes on OpenStreetMap and getting geodesic measurements in real time. All coordinates are displayed in the **MGRS** (Military Grid Reference System) format.

## What it does

GeoSketch lets you draw shapes directly on a full-screen map and instantly see accurate measurements for each shape you create:

- **Circles** — radius, diameter, circumference, and area
- **Triangles & polygons** — side lengths, total perimeter, longest diagonal, and area
- **Rectangles** — same as polygons, with 4-vertex measurements
- **Lines (polylines)** — individual segment lengths and total length
- **Markers** — precise MGRS coordinate of the placed point

All distances use the **Haversine formula** for accurate geodesic calculations on the Earth's surface. Polygon areas are computed using the **Shoelace formula** on metre-projected coordinates. The mouse cursor continuously shows the current MGRS coordinate as you move across the map.

Shapes can be edited (moved, resized, vertices repositioned) and deleted after creation — measurements update automatically.

## Tech stack

- [Leaflet.js](https://leafletjs.com/) (v1.9.4) — interactive map rendering with OpenStreetMap tiles
- [Leaflet.draw](https://leaflet.github.io/Leaflet.draw/) (v1.0.4) — shape drawing and editing toolbar
- Custom MGRS converter — built-in WGS84-to-MGRS conversion (no external dependency)
- Python `http.server` — zero-dependency local server

Everything runs in a single `index.html` file with libraries loaded from CDN. No build step, no npm, no bundler.

## How to run

**Requirements:** Python 3

```bash
git clone https://github.com/jhotti/geosketch.git
cd geosketch
python3 serve.py
```

Open [http://localhost:8001](http://localhost:8001) in your browser.

Alternatively, serve with any static file server:

```bash
# Python one-liner
python3 -m http.server 8001

# or Node
npx serve -p 8001
```

## Usage

1. Use the **drawing toolbar** (top-left) to select a shape type
2. Click on the map to place vertices (or click-drag for circles)
3. Measurements appear instantly in the **panel on the right**
4. The **MGRS coordinate** under your cursor is shown at the bottom-left
5. Use the **edit** and **delete** buttons in the toolbar to modify or remove shapes

## Project structure

```
geosketch/
├── index.html    # Full application — map, drawing tools, MGRS conversion, measurements
├── serve.py      # Local dev server (port 8001)
├── .gitignore
└── README.md
```

## License

MIT
