import { useEffect, useMemo, useState } from 'react';

type Opportunity = {
  id: number;
  title: string;
  domain: string;
  problem_definition: string;
  why_it_matters: string;
  bottleneck: string;
  priority_score: number;
  score_explanation: string;
  novelty: number;
  technical_difficulty: number;
  ip_potential: number;
  market_size_score: number;
  manufacturing_feasibility: number;
  capital_required: number;
  time_required: number;
  chance_of_success: number;
  long_term_moat: number;
  team_fit: number;
};

type Evidence = {
  id: number;
  claim: string;
  source: string;
  evidence_level: number;
  confidence_percent: number;
};

type Assumption = {
  id: number;
  statement: string;
  limitation_type: string;
  proposed_test: string;
};

type Experiment = {
  id: number;
  hypothesis: string;
  critical_question: string;
  estimated_cost_inr: number;
  estimated_timeline_days: number;
};

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export default function App() {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([]);
  const [evidence, setEvidence] = useState<Evidence[]>([]);
  const [assumptions, setAssumptions] = useState<Assumption[]>([]);
  const [experiments, setExperiments] = useState<Experiment[]>([]);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    Promise.all([
      fetch(`${API_BASE}/opportunities`).then((res) => res.json()),
      fetch(`${API_BASE}/evidence`).then((res) => res.json()),
      fetch(`${API_BASE}/assumptions`).then((res) => res.json()),
      fetch(`${API_BASE}/experiments`).then((res) => res.json()),
    ])
      .then(([opps, ev, assump, exp]) => {
        setOpportunities(opps);
        setEvidence(ev);
        setAssumptions(assump);
        setExperiments(exp);
      })
      .catch((err) => setError(String(err)));
  }, []);

  const topOpportunity = useMemo(() => {
    return [...opportunities].sort((a, b) => b.priority_score - a.priority_score)[0];
  }, [opportunities]);

  return (
    <main className="page">
      <section className="hero">
        <p className="eyebrow">DAEDALUS v0.1</p>
        <h1>Technology Compass</h1>
        <p>
          A disciplined operating system for ranking deep-tech opportunities,
          tracking evidence, challenging assumptions, and designing falsifiable experiments.
        </p>
      </section>

      {error && <div className="error">API error: {error}</div>}

      <section className="grid metrics">
        <Metric label="Opportunities" value={opportunities.length} />
        <Metric label="Evidence Claims" value={evidence.length} />
        <Metric label="Assumptions" value={assumptions.length} />
        <Metric label="Experiments" value={experiments.length} />
      </section>

      {topOpportunity && (
        <section className="card highlight">
          <p className="eyebrow">Current highest-ranked opportunity</p>
          <h2>{topOpportunity.title}</h2>
          <p>{topOpportunity.score_explanation}</p>
          <strong>Priority score: {topOpportunity.priority_score}/10</strong>
        </section>
      )}

      <section className="card">
        <h2>Opportunity Atlas</h2>
        <div className="tableWrap">
          <table>
            <thead>
              <tr>
                <th>Problem</th>
                <th>Domain</th>
                <th>Bottleneck</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {opportunities.map((item) => (
                <tr key={item.id}>
                  <td><strong>{item.title}</strong><br />{item.problem_definition}</td>
                  <td>{item.domain}</td>
                  <td>{item.bottleneck}</td>
                  <td>{item.priority_score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="grid two">
        <section className="card">
          <h2>Evidence Register</h2>
          {evidence.map((item) => (
            <article className="mini" key={item.id}>
              <strong>{item.claim}</strong>
              <p>Evidence level: {item.evidence_level} · Confidence: {item.confidence_percent}%</p>
              <small>{item.source}</small>
            </article>
          ))}
        </section>

        <section className="card">
          <h2>Assumption Library</h2>
          {assumptions.map((item) => (
            <article className="mini" key={item.id}>
              <strong>{item.statement}</strong>
              <p>Limitation: {item.limitation_type}</p>
              <small>Test: {item.proposed_test}</small>
            </article>
          ))}
        </section>
      </section>

      <section className="card">
        <h2>Experiment Planner</h2>
        {experiments.map((item) => (
          <article className="mini" key={item.id}>
            <strong>{item.hypothesis}</strong>
            <p>{item.critical_question}</p>
            <small>Cost: ₹{item.estimated_cost_inr.toLocaleString('en-IN')} · Timeline: {item.estimated_timeline_days} days</small>
          </article>
        ))}
      </section>
    </main>
  );
}

function Metric({ label, value }: { label: string; value: number }) {
  return (
    <div className="card metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}
