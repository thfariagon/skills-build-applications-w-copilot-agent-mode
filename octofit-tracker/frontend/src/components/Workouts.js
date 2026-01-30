import React, { useEffect, useState } from "react";

export default function Activities() {
  const [rows, setRows] = useState([]);
  const [error, setError] = useState("");

  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log("[Workouts] endpoint:", endpoint);

    async function load() {
      try {
        const res = await fetch(endpoint);
        const data = await res.json();

        console.log("[Workouts] raw data:", data);

        const items = Array.isArray(data) ? data : (data?.results ?? []);
        setRows(items);
      } catch (e) {
        console.error("[Workouts] fetch error:", e);
        setError(String(e));
      }
    }

    load();
  }, [endpoint]);

  return (
    <div className="card">
      <div className="card-body">
        <h3 className="card-title">Activities</h3>

        {error && <div className="alert alert-danger">{error}</div>}

        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>#</th>
                <th>Raw</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r, idx) => (
                <tr key={r?.id ?? idx}>
                  <td>{r?.id ?? idx + 1}</td>
                  <td><pre className="mb-0">{JSON.stringify(r, null, 2)}</pre></td>
                </tr>
              ))}
              {rows.length === 0 && (
                <tr>
                  <td colSpan="2" className="text-muted">
                    No data returned.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        <small className="text-muted">Endpoint: {endpoint}</small>
      </div>
    </div>
  );
}
