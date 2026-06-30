from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from .database import get_session
from .models import ResearchQuestion, ResearchQuestionCreate
from .scoring import calculate_question_score, question_score_explanation

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("")
def list_questions(session: Session = Depends(get_session)) -> list[dict[str, Any]]:
    items = session.exec(select(ResearchQuestion)).all()
    return [serialize_question(item) for item in items]


@router.post("", response_model=ResearchQuestion)
def create_question(payload: ResearchQuestionCreate, session: Session = Depends(get_session)) -> ResearchQuestion:
    item = ResearchQuestion.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("/high-priority")
def high_priority_questions(session: Session = Depends(get_session)) -> list[dict[str, Any]]:
    items = session.exec(select(ResearchQuestion)).all()
    scored = [serialize_question(item) for item in items]
    return sorted(scored, key=lambda item: item["question_score"], reverse=True)


@router.get("/{question_id}")
def get_question(question_id: int, session: Session = Depends(get_session)) -> dict[str, Any]:
    item = session.get(ResearchQuestion, question_id)
    if not item:
        raise HTTPException(status_code=404, detail="Research question not found")
    return serialize_question(item)


def serialize_question(item: ResearchQuestion) -> dict[str, Any]:
    data = item.model_dump()
    data["question_score"] = calculate_question_score(item)
    data["score_explanation"] = question_score_explanation(item)
    return data
