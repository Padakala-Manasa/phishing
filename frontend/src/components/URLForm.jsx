import React, { useState } from "react";
import reel from './reel.jpg';

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `url=${encodeURIComponent(url)}`,
      });

      if (response.ok) {
        const data = await response.json();
        if (data.error) {
          setError(data.error);
        } else {
          setResult(data.result);
        }
      } else {
        setError("An error occurred");
      }
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div style={{ backgroundColor: "#121212", height: "100vh", display: "flex", justifyContent: "center", alignItems: "center", backgroundImage: `url(${reel})`, backgroundSize: "cover", backgroundPosition: "center" }}>
      <div style={{ backgroundColor: "#121212", padding: "20px", borderRadius: "10px", boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)" }}>
        <h1 style={{ fontSize: "48px", marginBottom: "10px", textAlign: "center", color: "#FF4500" }}>URL Phishing Prediction</h1>
        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
          <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Enter URL" required style={{ width: "150px", padding: "10px", marginBottom: "20px", border: "1px solid #1DB954", borderRadius: "5px", fontSize: "24px", color: "#E5E5E5", backgroundColor: "#121212" }} />
          <button type="submit" style={{ backgroundColor: "#FF4500", color: "#E5E5E5", padding: "10px 20px", border: "none", borderRadius: "5px", cursor: "pointer", transition: "background-color 0.2s ease-in-out", fontSize: "24px" }}>Predict</button>
        </form>
        {error && <p style={{ color: "#FFD700" }}>{error}</p>}
        {result && <p style={{ fontSize: "36px", color: "#FFD700" }}>{result}</p>}
      </div>
    </div>
  );
}

export default App;