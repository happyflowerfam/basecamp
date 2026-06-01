"""
Hawaii Drive Times — OSRM Router
Uses OpenStreetMap routing (free, no API key required).
Run: python3 drive_times.py
"""

import requests


def driving_time(name, origin_coords, dest_coords):
    """coords as (lat, lon) tuples"""
    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{origin_coords[1]},{origin_coords[0]};"
        f"{dest_coords[1]},{dest_coords[0]}"
        f"?overview=false"
    )
    r = requests.get(url)
    seconds = r.json()["routes"][0]["duration"]
    minutes = round(seconds / 60)
    print(f"{name}: ~{minutes} min")


# --- Kauai ---
print("\n🌿 Kauai")
driving_time("LIH airport → Smith's Kauai (Wailua)",  (21.9760, -159.3390), (22.0495, -159.3413))
driving_time("Kapaa → Waimea Canyon",                 (22.0752, -159.3190), (22.0561, -159.6584))
driving_time("Waimea Canyon → Kalalau Lookout",       (22.0561, -159.6584), (22.1285, -159.6496))
driving_time("Waimea Canyon → Poipu Beach",           (22.0561, -159.6584), (21.8731, -159.4682))
driving_time("Kapaa → Kikiaola Harbor",               (22.0752, -159.3190), (21.9667, -159.7394))
driving_time("Kapaa → 1 Hotel Princeville",           (22.0752, -159.3190), (22.2197, -159.4816))
driving_time("1 Hotel Princeville → Ke'e Beach",      (22.2197, -159.4816), (22.2233, -159.5800))
driving_time("Ke'e Beach → Kapaa",                    (22.2233, -159.5800), (22.0752, -159.3190))
driving_time("Kapaa → LIH airport",                   (22.0752, -159.3190), (21.9760, -159.3390))

# --- Big Island ---
print("\n🌋 Big Island")
driving_time("KOA airport → Hilo",                    (19.7388, -156.0456), (19.7297, -155.0900))
driving_time("Hilo → Volcanoes NP entrance",          (19.7297, -155.0900), (19.4194, -155.2885))
driving_time("Volcanoes NP → Hilo",                   (19.4194, -155.2885), (19.7297, -155.0900))
driving_time("Hilo → Punalu'u Black Sand Beach",      (19.7297, -155.0900), (19.1308, -155.5050))
driving_time("Punalu'u → Volcanoes NP",               (19.1308, -155.5050), (19.4194, -155.2885))
driving_time("Hilo → Waipio Valley Lookout",          (19.7297, -155.0900), (20.1197, -155.5872))
driving_time("Waipio → KOA airport",                  (20.1197, -155.5872), (19.7388, -156.0456))
driving_time("Hilo → Rainbow Falls",                  (19.7297, -155.0900), (19.7361, -155.1025))
driving_time("Hilo → Akaka Falls",                    (19.7297, -155.0900), (19.8522, -155.1536))
