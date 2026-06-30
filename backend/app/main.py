from typing import Any
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from .config import settings
from .database import create_db_and_tables, get_session
from .models import (
    Assumption,
    AssumptionCreate,
    Evidence,
    EvidenceCreate,
    Experiment,
    ExperimentCreate,
    Opportunity,
    OpportunityCreate,
)
from .questions import router as questions_router
from .scoring import calculate_priority_score, score_explanation
from .seed import seed_data

app = FastAPI(title="DAEDALUS API", version="0.2.0")
app.include_router(questions_router)

origins = [item.strip() for item in settings.cors_origins.split(",") if item.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()
    with next(get_session()) as session:
        seed_data(session)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "system": "DAEDALUS"}


@app.get("/opportunities")
def list_opportunities(session: Session = Depends(get_session)) -> list[dict[str, Any]]:
    items = session.exec(select(Opportunity)).all()
    return [serialize_opportunity(item) for item in items]


@app.post("/opportunities", response_model=Opportunity)
def create_opportunity(payload: OpportunityCreate, session: Session = Depends(get_session)) -> Opportunity:
    item = Opportunity.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.get("/opportunities/{opportunity_id}")
def get_opportunity(opportunity_id: int, session: Session = Depends(get_session)) -> dict[str, Any]:
    item = session.get(Opportunity, opportunity_id)
    if not item:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return serialize_opportunity(item)


@app.get("/evidence", response_model=list[Evidence])
def list_evidence(session: Session = Depends(get_session)) -> list[Evidence]:
    return session.exec(select(Evidence)).all()


@app.post("/evidence", response_model=Evidence)
def create_evidence(payload: EvidenceCreate, session: Session = Depends(get_session)) -> Evidence:
    item = Evidence.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.get("/assumptions", response_model=list[Assumption])
def list_assumptions(session: Session = Depends(get_session)) -> list[Assumption]:
    return session.exec(select(Assumption)).all()


@app.post("/assumptions", response_model=Assumption)
def create_assumption(payload: AssumptionCreate, session: Session = Depends(get_session)) -> Assumption:
    item = Assumption.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.get("/experiments", response_model=list[Experiment])
def list_experiments(session: Session = Depends(get_session)) -> list[Experiment]:
    return session.exec(select(Experiment)).all()


@app.post("/experiments", response_model=Experiment)
def create_experiment(payload: ExperimentCreate, session: Session = Depends(get_session)) -> Experiment:
    item = Experiment.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def serialize_opportunity(item: Opportunity) -> dict[str, Any]:
    data = item.model_dump()
    data["priority_score"] = calculate_priority_score(item)
    data["score_explanation"] = score_explanation(item)
    return data
