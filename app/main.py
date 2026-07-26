from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="API de prueba",
    description="API sencilla para practicar pruebas automáticas con pytest.",
    version="1.0.0",
)


class PredictRequest(BaseModel):
    input: str = Field(
        ...,
        min_length=1,
        description="Texto que se desea consultar",
        examples=["becas"],
    )


class PredictResponse(BaseModel):
    result: str


@app.get("/")
def root() -> dict[str, str]:
    """
    Endpoint principal de la API.
    """
    return {
        "message": "API funcionando correctamente",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> dict[str, str]:
    """
    Permite comprobar que la API está disponible.
    """
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    """
    Procesa una consulta simple y devuelve una respuesta simulada.

    Más adelante, esta función puede conectarse con un modelo de IA,
    una base de datos o un servicio externo.
    """
    normalized_input = payload.input.strip().lower()

    responses = {
        "becas": "Existen distintas alternativas de becas y beneficios estudiantiles.",
        "matricula": "La información de matrícula está disponible en el portal institucional.",
        "horarios": "Los horarios pueden consultarse en la plataforma académica.",
    }

    result = responses.get(
        normalized_input,
        f"Consulta recibida correctamente: {payload.input.strip()}",
    )

    return PredictResponse(result=result)