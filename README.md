# Fingerdash

**Controla Geometry Dash** con un simple toque de tus dedos, gracias a MediaPipe Hands y vgamepad.

---

## 📖 Descripción

Fingerdash es un controlador gestual para Geometry Dash que emula el botón “A” de un mando Xbox usando un gesto de **pinch** (pellizco) entre el pulgar y el índice. Funciona en tiempo real, a baja latencia y alta precisión, sin necesidad de hardware adicional.

---

## 🚀 Características

- **Detección 3D de pellizco**  
  Usa MediaPipe para medir la distancia relativa entre pulgar e índice, independientemente del ángulo de la mano.

- **Histéresis dinámica**  
  Umbrales configurables para evitar parpadeos de entrada (PINCH_CLOSE y PINCH_OPEN).

- **Baja latencia**  
  Captura y procesa a hasta 60 FPS, con buffers mínimos y sleep inteligente.

- **Plug & play**  
  Solo Python, tu cámara web y el paquete `vgamepad`.

---

## 📂 Estructura del proyecto

```
Fingerdash/
├─ config.py            # Parámetros de cámara, confianza y umbrales
├─ gesture_detector.py  # Lógica de MediaPipe y detección de pinch
├─ xbox_controller.py   # Emulación de mando Xbox (vgamepad)
├─ main.py              # Loop principal: captura, detección y envío de comandos
├─ requirements.txt     # Bibliotecas necesarias
└─ README.md            # Esta documentación
```

---

## ⚙️ Instalación

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/tuUsuario/Fingerdash.git
   cd Fingerdash
   ```

2. **Crea un entorno virtual (opcional pero recomendado)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows
   ```

3. **Instala dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso

1. Conecta tu cámara web y asegúrate de que no esté siendo usada por otra aplicación.  
2. Ejecuta el script principal:  
   ```bash
   python main.py
   ```
3. Abre Geometry Dash y posiciona tu mano frente a la cámara.  
4. Cuando pellizques pulgar e índice, Fingerdash enviará un “press A” y tu personaje saltará.

Para salir, presiona la tecla **q** en la ventana de vídeo.

---

## 🔧 Calibración y ajustes

- **Resolución / FPS**  
  Modifica `FRAME_WIDTH`, `FRAME_HEIGHT` y `MAX_FPS` en `config.py` según tu cámara y CPU.

- **Umbrales de pellizco**  
  Ajusta `PINCH_CLOSE` y `PINCH_OPEN` para tu mano: valores típicos 0.18 / 0.25 (18 % / 25 %).

- **Confianza de detección**  
  Cambia `DETECTION_CONFIDENCE` y `TRACKING_CONFIDENCE` (0.0–1.0) para más robustez o velocidad.

---

## 🏷 Etiquetas

```
#Fingerdash  #GeometryDash  #GestureControl  #MediaPipe  #vgamepad  #Python
```

---

## 🤝 Contribuciones

¡Bienvenidas! Si encuentras errores o quieres añadir nuevas gestos (doble salto, dash, etc.), abre un **issue** o envía un **pull request**.

---

