from typing import Optional
from sqlmodel import Field, SQLModel


class OpportunityBase(SQLModel):
    title: str
    domain: str
    problem_definition: str
    why_it_matters: str
    existing_solutions: str
    bottleneck: str
    physics_involved: str
    engineering_involved: str
    manufacturing_notes: str = ""
    estimated_market_size: str = "Unknown"
    novelty: int = Field(default=5, ge=0, le=10)
    technical_difficulty: int = Field(default=5, ge=0, le=10)
    ip_potential: int = Field(default=5, ge=0, le=10)
    market_size_score: int = Field(default=5, ge=0, le=10)
    manufacturing_feasibility: int = Field(default=5, ge=0, le=10)
    capital_required: int = Field(default=5, ge=0, le=10)
    time_required: int = Field(default=5, ge=0, le=10)
    chance_of_success: int = Field(default=5, ge=0, le=10)
    long_term_moat: int = Field(default=5, ge=0, le=10)
    team_fit: int = Field(default=5, ge=0, le=10)


class Opportunity(OpportunityBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class OpportunityCreate(OpportunityBase):
    pass


class ResearchQuestionBase(SQLModel):
    title: str
    question_text: str
    domain: str
    category: str = "engineering"
    why_it_matters: str
    current_belief: str = "Unknown"
    known_facts: str = ""
    unknowns: str = ""
    related_physics: str = ""
    related_technologies: str = ""
    suggested_experiment: str = ""
    status: str = "open"
    review_date: str = ""
    scientific_importance: int = Field(default=5, ge=0, le=10)
    engineering_impact: int = Field(default=5, ge=0, le=10)
    commercial_relevance: int = Field(default=5, ge=0, le=10)
    feasibility: int = Field(default=5, ge=0, le=10)
    novelty: int = Field(default=5, ge=0, le=10)
    capability_creation: int = Field(default=5, ge=0, le=10)
    urgency: int = Field(default=5, ge=0, le=10)


class ResearchQuestion(ResearchQuestionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ResearchQuestionCreate(ResearchQuestionBase):
    pass


class EvidenceBase(SQLModel):
    opportunity_id: Optional[int] = Field(default=None, foreign_key="opportunity.id")
    claim: str
    source: str
    evidence_level: int = Field(default=0, ge=0, le=5)
    confidence_percent: int = Field(default=50, ge=0, le=100)
    contradicting_evidence: str = ""
    notes: str = ""


class Evidence(EvidenceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class EvidenceCreate(EvidenceBase):
    pass


class AssumptionBase(SQLModel):
    opportunity_id: Optional[int] = Field(default=None, foreign_key="opportunity.id")
    statement: str
    limitation_type: str = "unknown"
    evidence_level: int = Field(default=0, ge=0, le=5)
    proposed_test: str = ""
    risk_if_false: str = ""


class Assumption(AssumptionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class AssumptionCreate(AssumptionBase):
    pass


class ExperimentBase(SQLModel):
    opportunity_id: Optional[int] = Field(default=None, foreign_key="opportunity.id")
    hypothesis: str
    critical_question: str
    method: str
    equipment_required: str
    success_criteria: str
    failure_modes: str
    estimated_cost_inr: int = Field(default=0, ge=0)
    estimated_timeline_days: int = Field(default=7, ge=1)


class Experiment(ExperimentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ExperimentCreate(ExperimentBase):
    pass
