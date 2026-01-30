import React from "react";
import { BrowserRouter as Router, Routes, Route, NavLink, Navigate } from "react-router-dom";

import Activities from "./components/Activities";
import Leaderboard from "./components/Leaderboard";
import Teams from "./components/Teams";
import Users from "./components/Users";
import Workouts from "./components/Workouts";

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <span className="navbar-brand">OctoFit Tracker</span>

          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#octofitNav"
            aria-controls="octofitNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon" />
          </button>

          <div className="collapse navbar-collapse" id="octofitNav">
            <ul className="navbar-nav ms-auto">
              {[
                ["Activities", "/activities"],
                ["Workouts", "/workouts"],
                ["Users", "/users"],
                ["Teams", "/teams"],
                ["Leaderboard", "/leaderboard"],
              ].map(([label, to]) => (
                <li className="nav-item" key={to}>
                  <NavLink
                    className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}
                    to={to}
                  >
                    {label}
                  </NavLink>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>

      <main className="container mt-4">
        <Routes>
          <Route path="/" element={<Navigate to="/activities" replace />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
