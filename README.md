# HostIQ Paris - Airbnb Host Intelligence Platform

A data-driven dashboard for Airbnb hosts in Paris, providing pricing optimization and guest feedback analysis.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

HostIQ Paris helps Airbnb hosts optimize their listings through:

- **Smart Pricing Engine** - ML-based price predictions using Random Forest
- **Guest Feedback Intelligence** - NLP-powered review analysis with sentiment scoring
- **Portfolio Dashboard** - Visual analytics for multi-property hosts

## Features

### Dashboard Views
1. **Overview** - Key metrics, alerts, and property map
2. **Revenue** - Price optimization recommendations
3. **Quality & Actions** - Review insights and improvement suggestions

### Key Capabilities
- Price vs. predicted price comparison
- Sentiment analysis of guest reviews
- Automated identification of property advantages/disadvantages
- Actionable recommendations based on review patterns

## Project Structure

```
hostiq_app/
├── app.py                          # Streamlit application
├── property_data.csv               # Property-level data (one row per property)
├── host_data.csv                   # Host-level aggregated data
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment config
└── notebooks/
    ├── data_preparation.ipynb      # Data preprocessing pipeline
    ├── Smart Pricing Engine.ipynb  # ML pricing model
    └── Guest Feedback Intelligence System(paris_data).ipynb  # NLP analysis
```

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/pazgold9/hostiq-paris.git
   cd hostiq-paris/hostiq_app
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Local Development

```bash
cd hostiq_app
streamlit run app.py
```

The app will be available at `http://localhost:8501`

### Production Deployment (Render)

The app is configured for deployment on Render. Simply connect your GitHub repository and Render will automatically deploy using `render.yaml`.

**Live Demo:** [https://hostiq-paris.onrender.com](https://hostiq-paris.onrender.com)

## Data Pipeline

### 1. Smart Pricing Engine
- **Model:** Random Forest Regressor
- **Features:** 39 features including location, amenities, POI data, and host metrics
- **Performance:** RMSE $101.18, R² 0.52

### 2. Guest Feedback Intelligence
- **Sentiment Analysis:** DistilBERT-based sentiment scoring
- **Theme Extraction:** Regex-based identification of review themes
- **Languages:** English, French, German support

### 3. Data Preparation
Run `data_preparation.ipynb` to regenerate the processed CSV files from source data.

## Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly |
| ML Model | Scikit-learn (Random Forest) |
| NLP | Transformers (DistilBERT) |
| Deployment | Render |

## Screenshots

### Portfolio Dashboard
![Dashboard](docs/dashboard.png)

### Revenue Analysis
![Revenue](docs/revenue.png)

### Quality Insights
![Quality](docs/quality.png)

## API Reference

### Data Files

**property_data.csv** - Property-level data
| Column | Description |
|--------|-------------|
| property_id | Unique property identifier |
| host_id | Host identifier |
| price | Current listing price (€/night) |
| prediction | ML-predicted optimal price |
| review_sentiment | Sentiment score (0-1) |
| review_advantages | Identified positive themes |
| review_disadvantages | Identified negative themes |

**host_data.csv** - Aggregated host data
| Column | Description |
|--------|-------------|
| host_id | Unique host identifier |
| property_count | Number of properties |
| avg_sentiment | Average sentiment across properties |
| total_reviews | Total review count |
| quality_score | Overall quality metric |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Authors

- **Paz Goldfried** - Data Science & Development

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Airbnb for inspiration
- Databricks for cloud computing resources
- Course instructors for guidance

---

**Note:** This project was developed as part of an academic course. The data used is processed and aggregated; no raw scraped data is included in this repository.
