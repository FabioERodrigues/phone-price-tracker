# 📱 Tech Price Intelligence Pipeline

An automated, end-to-end data engineering pipeline that tracks real-time market prices for consumer electronics using official platform APIs.

## 🏗️ Architecture

* **Orchestration:** GitHub Actions triggers a daily, headless Python pipeline.
* **Data Ingestion:** Integrates with the official **eBay Browse API** (OAuth 2.0 Client Credentials flow) to retrieve authenticated, control-sampled pricing data.
* **Data Storage:** SQLite database, version-controlled directly within the repository.
* **Visualization:** Interactive **Streamlit** dashboard hosted locally to track historical price trends and live market averages.

## 🛠️ Technical Challenges & Solutions


* **Authentication & Compliance:** Transitioned from fragile HTML web scraping to an official REST API integration, ensuring compliance with enterprise Terms of Service while managing Base64 credential encoding and OAuth token lifecycles.
* **Environment Management:** Utilized Python virtual environments (`.venv`) and a `requirements.txt` file to ensure seamless cross-platform dependency consistency between local development and the cloud server.
* **CI/CD Automation:** Built a fully autonomous GitHub Actions workflow, completely eliminating the need for manual daily data collection.

## 🚀 Future Roadmap

* **Pipeline Refactoring:** Separate the ingestion logic from the data transformation logic by introducing a dedicated `pipeline.py` orchestration script.
* **Database Scaling:** Migrate from local SQLite to a cloud-hosted PostgreSQL instance (e.g., Supabase) for larger scale historical data retention.
* **Cloud Deployment:** Deploy the Streamlit dashboard to Streamlit Community Cloud for 24/7 web access.
* **Alerting System:** Implement a notification framework to trigger alerts when device prices drop below a specified "bargain" threshold.