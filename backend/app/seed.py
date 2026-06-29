from sqlmodel import Session, select
from .models import Assumption, Evidence, Experiment, Opportunity


def seed_data(session: Session) -> None:
    existing = session.exec(select(Opportunity)).first()
    if existing:
        return

    opportunities = [
        Opportunity(
            title="Self-calibrating industrial sensors",
            domain="Sensing and Metrology",
            problem_definition="Industrial sensors drift over time and often require manual calibration.",
            why_it_matters="Calibration downtime increases cost and reduces trust in automated decisions.",
            existing_solutions="Scheduled calibration, redundancy, high-end reference sensors, and manual inspection.",
            bottleneck="Long-term drift compensation under real operating conditions.",
            physics_involved="Thermal effects, material aging, noise, signal transduction, and environmental coupling.",
            engineering_involved="Embedded sensing, calibration models, edge processing, field validation, and reliability testing.",
            manufacturing_notes="Prototype can start with off-the-shelf sensors; manufacturable version needs robust packaging.",
            estimated_market_size="Large industrial automation market",
            novelty=7,
            technical_difficulty=7,
            ip_potential=7,
            market_size_score=8,
            manufacturing_feasibility=7,
            capital_required=4,
            time_required=5,
            chance_of_success=6,
            long_term_moat=7,
            team_fit=8,
        ),
        Opportunity(
            title="Affordable multimodal machine-health node",
            domain="Industrial Intelligence",
            problem_definition="Factories lack low-cost systems that combine vibration, acoustics, temperature, and electrical signals.",
            why_it_matters="Better machine state estimation can reduce downtime and unplanned failures.",
            existing_solutions="Single-mode condition monitoring, expensive predictive maintenance platforms, and manual inspections.",
            bottleneck="Reliable transfer across machine types and noisy environments.",
            physics_involved="Vibration, acoustics, heat transfer, current sensing, and mechanical wear.",
            engineering_involved="Sensor fusion, embedded systems, time-series modeling, and rugged device design.",
            manufacturing_notes="Early device can use commodity MEMS sensors; field trials are the hard part.",
            estimated_market_size="Large predictive maintenance market",
            novelty=6,
            technical_difficulty=6,
            ip_potential=6,
            market_size_score=8,
            manufacturing_feasibility=8,
            capital_required=4,
            time_required=4,
            chance_of_success=7,
            long_term_moat=6,
            team_fit=8,
        ),
        Opportunity(
            title="Portable low-cost spectroscopy for field identification",
            domain="Scientific Instruments",
            problem_definition="Many material and chemical measurements require expensive lab instruments.",
            why_it_matters="Field identification can improve recycling, agriculture, food safety, and industrial inspection.",
            existing_solutions="Benchtop spectroscopy, handheld NIR devices, visual inspection, and lab sampling.",
            bottleneck="Accuracy, calibration transfer, optics cost, and signal-to-noise ratio.",
            physics_involved="Light-matter interaction, absorption, scattering, detectors, and optical filtering.",
            engineering_involved="Optical design, electronics, calibration, embedded inference, and mechanical stability.",
            manufacturing_notes="Optical alignment and calibration are manufacturing risks.",
            estimated_market_size="Medium to large across multiple verticals",
            novelty=6,
            technical_difficulty=8,
            ip_potential=6,
            market_size_score=7,
            manufacturing_feasibility=5,
            capital_required=6,
            time_required=7,
            chance_of_success=5,
            long_term_moat=7,
            team_fit=5,
        ),
    ]
    session.add_all(opportunities)
    session.commit()
    for item in opportunities:
        session.refresh(item)

    session.add_all([
        Evidence(opportunity_id=opportunities[0].id, claim="Sensor drift is a major operational issue in industrial measurement.", source="Initial research hypothesis", evidence_level=0, confidence_percent=55),
        Assumption(opportunity_id=opportunities[0].id, statement="Drift can be inferred from internal sensor behavior plus environmental context.", limitation_type="engineering", evidence_level=0, proposed_test="Run controlled temperature and humidity drift experiment."),
        Experiment(opportunity_id=opportunities[0].id, hypothesis="Multisensor context can reduce apparent drift without manual recalibration.", critical_question="Can the model distinguish true signal from drift?", method="Expose sensors to controlled environmental changes and compare against reference readings.", equipment_required="Sensor modules, reference meter, chamber or improvised controlled environment, data logger.", success_criteria="At least 30 percent reduction in measurement error versus uncorrected baseline.", failure_modes="Model overfits, reference sensor is poor, environment is uncontrolled.", estimated_cost_inr=25000, estimated_timeline_days=21),
    ])
    session.commit()
