import math, cv2, mediapipe as mp
from config import (DETECTION_CONFIDENCE, TRACKING_CONFIDENCE,
                    PINCH_CLOSE, PINCH_OPEN)

class GestureDetector:
    """
    Devuelve:
        "pinch"  cuando pulgar‑índice se tocan (botón A mantenido)
        None     en cualquier otro caso
    El estado interno evita parpadeos (<‑‑ histéresis).
    """
    def __init__(self, max_hands: int = 1):
        mp_hands = mp.solutions.hands
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            model_complexity=0,
            min_detection_confidence=DETECTION_CONFIDENCE,
            min_tracking_confidence=TRACKING_CONFIDENCE
        )
        self.draw = mp.solutions.drawing_utils
        self._pinched = False    # estado persistente

    # ----------------------------------------------------
    def detect(self, frame_bgr):
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        res = self.hands.process(rgb)

        gesture = None
        if res.multi_hand_landmarks:
            hand = res.multi_hand_landmarks[0]
            gesture = self._update_pinch_state(hand)
            # ► coméntalo para +fps
            self.draw.draw_landmarks(
                frame_bgr, hand, mp.solutions.hands.HAND_CONNECTIONS,
                self.draw.DrawingSpec(thickness=1, circle_radius=1),
                self.draw.DrawingSpec(thickness=1, circle_radius=1)
            )
        else:
            # mano perdida ⇒ suelta
            self._pinched = False

        return gesture, frame_bgr

    # ----------------------------------------------------
    def _dist3(self, p, q):
        return math.sqrt((p.x-q.x)**2 + (p.y-q.y)**2 + (p.z-q.z)**2)

    def _update_pinch_state(self, lm):
        tip_thumb  = lm.landmark[4]
        tip_index  = lm.landmark[8]
        wrist      = lm.landmark[0]
        mcp_middle = lm.landmark[9]      # centro de la palma

        # distancia relativa 3 D, independiente del ángulo
        dist_tip   = self._dist3(tip_thumb, tip_index)
        ref_len    = self._dist3(wrist, mcp_middle) + 1e-6
        dist_rel   = dist_tip / ref_len

        # ---------------- histéresis --------------------
        if not self._pinched and dist_rel < PINCH_CLOSE:
            self._pinched = True
        elif self._pinched and dist_rel > PINCH_OPEN:
            self._pinched = False

        return "pinch" if self._pinched else None
