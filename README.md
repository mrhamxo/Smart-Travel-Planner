# 🌍 Smart Travel Planner - Agentic AI Application

An intelligent, AI-powered travel planning assistant that creates comprehensive, personalized trip itineraries using LangGraph, multiple LLM providers, and real-time data from various APIs.

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg)](https://streamlit.io)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Tools & Integrations](#tools--integrations)
- [License](#license)
- [Author](#author)

## 🎯 Overview

Smart Travel Planner is an agentic AI application built with LangGraph that orchestrates multiple tools and APIs to generate detailed, actionable travel plans. The system intelligently combines weather forecasts, place recommendations, expense calculations, and currency conversions to provide comprehensive trip planning assistance.

### Key Highlights

- **Agentic Workflow**: Built on LangGraph for dynamic tool selection and multi-step reasoning
- **Multi-Provider LLM Support**: Works with Groq and OpenAI models
- **Real-Time Data**: Integrates with Google Places, OpenWeatherMap, and other live APIs
- **Dual Interface**: FastAPI backend + Streamlit frontend
- **Intelligent Fallbacks**: Google Places with Tavily Search fallback mechanism
- **Cost-Aware Planning**: Automatic expense calculation and currency conversion

## ✨ Features

### Travel Planning Capabilities

- 📍 **Comprehensive Itineraries**: Day-by-day travel plans with detailed schedules
- 🏨 **Hotel Recommendations**: Accommodations with approximate nightly costs
- 🎯 **Attraction Discovery**: Tourist hotspots and off-beat locations
- 🍽️ **Restaurant Suggestions**: Dining options with price ranges
- 🎭 **Activity Planning**: Local experiences and activities
- 🚗 **Transportation Guide**: Available modes of transport with details
- 💰 **Cost Breakdown**: Detailed expense estimation per day and total trip
- 🌤️ **Weather Forecasts**: Real-time weather data for destination planning
- 💱 **Currency Conversion**: Automatic currency exchange calculations

### Technical Features

- **Agentic Reasoning**: LangGraph-powered decision making
- **Tool Orchestration**: Intelligent selection and chaining of multiple tools
- **Conversational Interface**: Natural language query processing
- **Graph Visualization**: Auto-generated workflow diagrams
- **API-First Design**: RESTful backend with OpenAPI documentation
- **Responsive UI**: Clean, user-friendly Streamlit interface

## 🏗️ Architecture

```
┌─────────────────┐
│  Streamlit UI   │
│   (Frontend)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   FastAPI       │
│   (Backend)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   LangGraph     │
│  Agent Graph    │
└────────┬────────┘
         │
    ┌────┴────┬────────────┬──────────────┐
    ▼         ▼            ▼              ▼
┌────────┐ ┌──────┐ ┌──────────┐ ┌──────────────┐
│Weather │ │Place │ │Calculator│ │Currency      │
│Tools   │ │Search│ │Tools     │ │Converter Tool│
└────────┘ └──────┘ └──────────┘ └──────────────┘
```

### Workflow Diagram

The application generates a visual representation of the agentic workflow:

```
START → Agent → Tools (conditional) → Agent → END
              ↓                        ↑
              └────────────────────────┘
```

## 🔧 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### API Keys Required

You'll need to obtain API keys from the following services:

1. **OpenAI** (optional): [platform.openai.com](https://platform.openai.com/)
2. **Groq**: [console.groq.com](https://console.groq.com/)
3. **Google Places API**: [Google Cloud Console](https://console.cloud.google.com/)
4. **Tavily Search**: [tavily.com](https://tavily.com/)
5. **OpenWeatherMap**: [openweathermap.org](https://openweathermap.org/api)
6. **ExchangeRate API**: [exchangerate-api.com](https://www.exchangerate-api.com/)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-travel-planner.git
cd smart-travel-planner
```

### 2. Create Virtual Environment

```bash
python -m venv myenv

# On Windows
myenv\Scripts\activate

# On macOS/Linux
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package

```bash
pip install -e .
```

## ⚙️ Configuration

### 1. Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.name .env
```

Edit `.env` with your API keys:

```env
OPENAI_API_KEY="your-openai-key-here"
GROQ_API_KEY="your-groq-key-here"
GOOGLE_API_KEY="your-google-key-here"
GPLACES_API_KEY="your-google-places-key-here"
TAVILA_API_KEY="your-tavily-key-here"
OPENWEATHERMAP_API_KEY="your-openweather-key-here"
EXCHANGE_RATE_API_KEY="your-exchange-rate-key-here"
ALPHAVANTAGE_API_KEY="your-alphavantage-key-here"
```

### 2. Configuration File

The `config/config.yaml` file contains LLM settings:

```yaml
project:
  name: Smart Travel Planner 
  version: 0.0.1
  author: "Muhammad Hamza"
  description: "An agentic AI project using LangGraph"

llm:
  groq:
    provider: "groq"
    model: "openai/gpt-oss-120b"
  
  openai:
    provider: "openai"
    model: "o4-mini"
```

You can modify the model names and add additional parameters as needed.

## 🚀 Usage

### Running the Application

#### 1. Start the Backend Server

```bash
python main.py
```

The FastAPI server will start at `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Alternative Docs: `http://localhost:8000/redoc`

#### 2. Launch the Streamlit Frontend

In a new terminal (with the virtual environment activated):

```bash
streamlit run app.py
```

The Streamlit app will open in your browser at `http://localhost:8501`

### Example Queries

Try these sample queries in the application:

```
"Plan a 5-day trip to Paris in December"
"I want to visit Bali for a week, budget $2000"
"Create an itinerary for Tokyo focusing on cultural experiences"
"Plan a romantic getaway to Santorini for 4 days"
"What's the best way to spend 3 days in New York City?"
```

### Using the API Directly

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "Plan a trip to Goa for 5 days"}'
```

## 📚 API Documentation

### Endpoints

#### `GET /`
- **Description**: Health check endpoint
- **Response**: Welcome message

#### `POST /query`
- **Description**: Submit a travel planning query
- **Request Body**:
  ```json
  {
    "query": "Plan a trip to Paris for 5 days"
  }
  ```
- **Response**:
  ```json
  {
    "answer": "Detailed travel plan..."
  }
  ```

### Interactive Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation.

## 📁 Project Structure

```
smart-travel-planner/
│
├── agent/
│   ├── __init__.py
│   └── agentic_workflow.py      # LangGraph workflow definition
│
├── config/
│   ├── __init__.py
│   └── config.yaml              # LLM configuration
│
├── exception/
│   ├── __init__.py
│   └── exception_handling.py    # Custom exceptions
│
├── logger/
│   ├── __init__.py
│   └── logging.py               # Logging configuration
│
├── prompt_library/
│   ├── __init__.py
│   └── prompt.py                # System prompts
│
├── tools/
│   ├── __init__.py
│   ├── weather_info_tool.py     # Weather data fetching
│   ├── place_search_tool.py     # Place recommendations
│   ├── expense_calculator_tool.py # Cost calculations
│   └── currency_conversion_tool.py # Currency exchange
│
├── utils/
│   ├── __init__.py
│   ├── config_loader.py         # YAML config loader
│   ├── model_loader.py          # LLM initialization
│   ├── weather_info.py          # Weather API wrapper
│   ├── place_search.py          # Places API wrapper
│   ├── expense_calculator.py    # Calculator utilities
│   ├── currency_converter.py    # Currency API wrapper
│   └── save_to_documents.py     # Export functionality
│
├── notebook/
│   └── experiments.ipynb        # Development experiments
│
├── .env.name                    # Environment template
├── .env                         # Your API keys (git-ignored)
├── .gitignore
├── .python-version
├── main.py                      # FastAPI backend
├── app.py                       # Streamlit frontend
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
├── pyproject.toml
├── LICENSE
└── README.md
```

## 🛠️ Tools & Integrations

### LLM Providers

- **Groq**: Fast inference with open-source models
- **OpenAI**: GPT-4 and other models

### External APIs

| Service | Purpose | Documentation |
|---------|---------|---------------|
| Google Places | Attractions, restaurants, activities | [Docs](https://developers.google.com/maps/documentation/places/web-service) |
| Tavily Search | Fallback search engine | [Docs](https://docs.tavily.com/) |
| OpenWeatherMap | Weather forecasts | [Docs](https://openweathermap.org/api) |
| ExchangeRate API | Currency conversion | [Docs](https://www.exchangerate-api.com/docs) |

### Core Technologies

- **LangChain**: LLM orchestration framework
- **LangGraph**: Agentic workflow engine
- **FastAPI**: High-performance API framework
- **Streamlit**: Interactive web UI
- **Pydantic**: Data validation
- **uvicorn**: ASGI server

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Muhammad Hamza**

- Email: mr.hamxa942@gmail.com
- GitHub: [@mrhamxo](https://github.com/mrhamxo)

## 📞 Contact

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/mrhamxo/smart-travel-planner/issues) page
2. Create a new issue with detailed information
3. Contact the author via email

## 🗺️ Roadmap

- [ ] Add support for more LLM providers
- [ ] Implement user authentication
- [ ] Add trip export to PDF/Word
- [ ] Multi-language support
- [ ] Mobile app development
- [ ] Integration with booking platforms
- [ ] Social sharing features
- [ ] Trip history and favorites

---

**Made with ❤️ using LangGraph and AI**