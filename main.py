import cv2, time
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT, MAX_FPS
from gesture_detector import GestureDetector
from xbox_controller import XboxController

def main():
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS,          MAX_FPS)
    cap.set(cv2.CAP_PROP_BUFFERSIZE,   1)

    detector   = GestureDetector()
    controller = XboxController()

    t_prev = time.perf_counter()
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)

        gest, vis = detector.detect(frame)

        if gest == "pinch":
            controller.press_a()
        else:
            controller.release_a()

        cv2.imshow("Precise Pinch ➜ Xbox A", vis)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # sin sobre‑dormir
        dt = time.perf_counter() - t_prev
        wait = max(0.0, (1./MAX_FPS) - dt)
        if wait: time.sleep(wait)
        t_prev = time.perf_counter()

    controller.release_a()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
