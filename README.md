# Flask Hello World

A very basic Flask app with 3 routes.

## Structure

```
flask_hello/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Install

```bash
pip install flask
```

## Run

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Routes

- `/` — HTML page saying "Hello, World!"
- `/api/hello` — returns JSON
- `/about` — simple text response
