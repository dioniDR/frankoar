# API Mínima FRANKO.AR

## Ejecutar localmente

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints

- `GET /avatar`
- `GET /historia`
- `POST /preguntar`
- `POST /consultar` → usa OpenAI y la ficha del personaje
