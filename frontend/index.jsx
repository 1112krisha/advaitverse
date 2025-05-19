import React from "react";
import ReactDOM from "react-dom/client";
import "./styles.css";

// Import generated components
import Dashboard from "./components/dashboard.jsx";
import Reports from "./components/reports.jsx"; // Add others as generated

function App() {
  return (
    <div className="min-h-screen bg-white p-8 space-y-6">
      <h1 className="text-4xl font-bold text-center text-orange-600">AdvaitVerse</h1>
      <Dashboard />
      <Reports />
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
