# Smart Travel Planner

An AI-powered travel planning assistant that helps users research destinations and build practical trip plans through a conversational interface. The application combines a Streamlit frontend with a FastAPI backend and a tool-using agent workflow built with LangGraph and LangChain.

## Features

- **Conversational trip planning:** Ask for a travel plan using natural language.
- **Day-by-day itineraries:** Generate detailed itineraries with popular attractions and less-travelled destinations.
- **Destination research:** Search for attractions, restaurants, activities, and local transportation.
- **Weather information:** Retrieve current weather and forecast information for a destination.
- **Trip budgeting:** Estimate hotel costs, total expenses, and average daily budgets.
- **Currency conversion:** Convert amounts between currencies using exchange-rate data.
- **Agent workflow:** LangGraph connects the language model to travel and budgeting tools, allowing it to call tools when needed.
- **Conversation history:** The Streamlit interface displays messages from the current session.

## Architecture

```text
User
 |
 v
Streamlit Frontend (app.py)
 |
 | POST /query
 v
FastAPI Backend (main.py)
 |
 v
LangGraph Agent Workflow
 |
 +--> Groq or OpenAI Language Model
 |
 +--> Destination Search Tools
 +--> Weather Tools
 +--> Currency Conversion Tool
 +--> Expense Calculation Tools
 |
 v
Travel Plan Returned to Streamlit
```

## Technology Stack

- **Language:** Python 3.11+
- **Frontend:** Streamlit
- **Backend:** FastAPI, Uvicorn
- **Agent orchestration:** LangGraph
- **LLM integration:** LangChain, ChatGroq, ChatOpenAI
- **External services:** Google Places, Tavily Search, OpenWeatherMap, ExchangeRate-API
- **Validation and configuration:** Pydantic, PyYAML, python-dotenv

## Project Structure

```text
Smart-Travel-Planner/
├── agent/
│   └── agentic_workflow.py
├── config/
│   └── config.yaml
├── exception/
├── logger/
├── notebook/
│   └── experiments.ipynb
├── prompt_library/
│   └── prompt.py
├── tools/
│   ├── arthematic_operation_tool.py
│   ├── currency_conversion_tool.py
│   ├── expense_calculator_tool.py
│   ├── place_search_tool.py
│   └── weather_info_tool.py
├── utils/
│   ├── config_loader.py
│   ├── currency_converter.py
│   ├── expense_calculator.py
│   ├── model_loader.py
│   ├── place_search.py
│   ├── save_to_documents.py
│   └── weather_info.py
├── app.py
├── main.py
├── requirements.txt
├── setup.py
└── pyproject.toml
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mrhamxo/Smart-Travel-Planner.git
cd Smart-Travel-Planner
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root and add the credentials for the services you intend to use:

```dotenv
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key

GPLACES_API_KEY=your_google_places_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
EXCHANGE_RATE_API_KEY=your_exchangerate_api_key
```

Use the credentials for the services you enable. Never commit real API keys or your `.env` file to GitHub.

### 5. Run the FastAPI backend

Open a terminal in the project root and run:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

- Root endpoint: `http://127.0.0.1:8000/`
- Query endpoint: `POST http://127.0.0.1:8000/query`
- Interactive API documentation: `http://127.0.0.1:8000/docs`

The query endpoint accepts JSON in this format:

```json
{
  "query": "Plan a five-day trip to Goa with an estimated budget."
}
```

### 6. Run the Streamlit frontend

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run app.py
```

The frontend sends requests to the backend at `http://localhost:8000`. Keep the backend running while using the application.

## Model Configuration

The default model provider is Groq. Model names for Groq and OpenAI are defined in `config/config.yaml`.

To use a different provider, update the `model_provider` argument when creating `GraphBuilder` and configure the corresponding API key.

## Example Requests

Try asking the assistant:

- "Plan a five-day trip to Goa for two people."
- "Suggest attractions, restaurants, and activities in Istanbul."
- "What is the current weather in Islamabad?"
- "Estimate hotel costs for seven nights at $90 per night."
- "Convert 500 USD to CAD."
- "Prepare a daily budget for a ten-day trip."

## Notes and Limitations

- The frontend currently connects to a local backend at `http://localhost:8000`. Update `BASE_URL` in `app.py` if the backend is hosted elsewhere.
- API keys are required for the corresponding external services.
- Generated results depend on the selected language model, available tools, external API responses, and system instructions.
- This repository does not currently include a hosted deployment configuration. The instructions above are for running the application locally.
- Verify prices, opening hours, weather, transportation details, and travel requirements with the relevant providers before making bookings.

## Author

**Muhammad Hamza**

GitHub: [@mrhamxo](https://github.com/mrhamxo)
