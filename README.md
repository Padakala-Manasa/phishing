# Phishing Detection Simulation

## Overview
This project is an AI-powered system designed to detect phishing URLs, specifically targeting fake streaming sites. It analyzes URL patterns and uses machine learning to classify URLs as legitimate or phishing.

## Features
- Parses URLs using `tldextract` to extract domain-related features.
- Trains a machine learning model with phishing datasets to classify URLs.
- Provides a user-friendly interface to test URLs for phishing.

---

## Tools and Technologies
- **Python 3.x**: Core programming language.
- **tldextract**: For extracting domain information from URLs.
- **scikit-learn**: For building and training the classification model.
- **Flask**: Backend framework for API development.
- **React**: Frontend framework for creating an interactive user interface.

---

## Dataset
The project uses a publicly available phishing dataset containing labeled URLs. The dataset includes:
- Legitimate URLs
- Phishing URLs

This data is used to train and validate the machine learning model.

---

## How It Works
1. **URL Parsing**: Extracts domain, subdomain, and suffix information using `tldextract`.
2. **Feature Extraction**: Converts URL components into meaningful features for the model.
3. **Model Training**: Trains a `RandomForestClassifier` from `scikit-learn` on the dataset.
4. **Prediction**: The trained model predicts whether a given URL is legitimate or phishing.

---

## Project Structure
```
PDetect/
├── backend/
│   ├── models/
│   │   ├── .gitkeep
│   │   ├── model.pkl
│   │   └── vectorizer.pkl
│   ├── templates/
│   ├── app.py               # Flask application
│   └── requirements.txt     # Backend dependencies
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── URLForm.jsx  # React component for URL input
│   │   ├── reel.jpg         # Static asset
│   │   ├── App.css          # Styling for the app
│   │   ├── App.js           # Main React component
│   │   ├── index.js         # Entry point for React app
│   │   └── index.css        # Global styles
│   ├── package.json         # Frontend dependencies
│   ├── package-lock.json
│   └── README.md            # Project documentation
├── venv/                    # Virtual environment for Python
├── train_model.py           # Script for training the model
```

---

## Getting Started

### Prerequisites
- Python 3.x
- Node.js and npm

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd PDetect
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Install Frontend Dependencies**
   ```bash
   cd ../frontend
   npm install
   ```

5. **Start the Backend Server**
   ```bash
   cd ../backend
   python app.py
   ```

6. **Start the Frontend Server**
   ```bash
   cd ../frontend
   npm start
   ```

7. **Access the Application**
   Open your browser and navigate to `http://localhost:3000`.

---

## Testing the System
- Enter a URL in the provided input field.
- The system will classify the URL as either "Legitimate" or "Phishing."

---

## Acknowledgments
Special thanks to the following resources for guidance and support:
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [tldextract Documentation](https://github.com/john-kurkowski/tldextract)

---

## License
This project is open-source and available under the [MIT License](LICENSE).
