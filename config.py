# ----------------- cámara y resolución -----------------
CAMERA_INDEX = 0
FRAME_WIDTH  = 640
FRAME_HEIGHT = 480
MAX_FPS      = 60           # latencia baja

# --------- confianza de MediaPipe Hands ----------------
DETECTION_CONFIDENCE = 0.7
TRACKING_CONFIDENCE  = 0.7

# -------- umbrales de pinch dinámico (3 D) -------------
#   dist_rel = dist(tip4‑tip8) / dist(wrist‑mcp9)
#   • PINCH_CLOSE  → se activa  (≈ 18 % del largo de la palma)
#   • PINCH_OPEN   → se libera (≈ 25 %)  → histéresis
PINCH_CLOSE = 0.18
PINCH_OPEN  = 0.25
