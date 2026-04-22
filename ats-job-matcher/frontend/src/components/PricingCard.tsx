export function PricingCard() {
  return (
    <div className="card">
      <h3>Pricing</h3>
      <div className="grid two">
        <div className="card">
          <h4>Free</h4>
          <p className="small">3 matches, basic optimization, limited downloads.</p>
        </div>
        <div className="card">
          <h4>Pay-as-you-go</h4>
          <p className="small">$2 per matched job package (resume + cover letter + PDF/DOCX).</p>
        </div>
      </div>
      <div className="card" style={{ marginTop: 12 }}>
        <h4>Pro — $20/month</h4>
        <p className="small">Up to 100 matches/month, unlimited docs, priority processing, analytics.</p>
      </div>
    </div>
  );
}
