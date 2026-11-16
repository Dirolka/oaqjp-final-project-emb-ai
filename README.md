# Final project

Emotion detection web application using the embeddable Watson NLP service and Flask.

## Setup and run

Run inside the Skills Network Theia lab: the Watson endpoint is only accessible there.

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_emotion_detection.py
python3 -m pylint server.py
python3 server.py
```

Open the lab preview on port 5000. Enter text to receive anger, disgust, fear, joy and sadness scores and the dominant emotion. Blank input displays `Invalid text! Please try again!`.

The original `templates/index.html` and `static/mywebscript.js` are preserved.

## Evidence

The `evidence` folder contains stage-specific code for Tasks 2, 3, 5, 6, 7 and 8. Live service results must be generated inside the lab; they are not simulated.
