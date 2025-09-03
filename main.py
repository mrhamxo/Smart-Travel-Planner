from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from agent.agentic_workflow import GraphBuilder   # Your custom graph workflow
import uvicorn

# --------------------------
# Initialize FastAPI app
# --------------------------
app = FastAPI()

# Allow CORS (important if your frontend runs on a different port/domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ For production, set specific domains instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# Define input request model
# --------------------------
class QueryRequest(BaseModel):
    """
    Request body for query endpoint.
    Example: {"query": "Plan a trip to Paris in December"}
    """
    query: str = Field(..., example="Plan a trip to Paris in December")
    
    
# --------------------------
# Home Route
# --------------------------
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Smart Travel Planner Agentic AI Application!"}

# --------------------------
# API Route
# --------------------------
@app.post("/query")   
async def query_travel_agent(request: QueryRequest):
    """
    API endpoint to handle user queries for the AI Travel Agent.
    """
    try:
        print(f"Incoming query: {request.query}")

        # Initialize GraphBuilder (agent workflow)
        graph = GraphBuilder(model_provider="groq")

        # Call the GraphBuilder (runs __call__)
        react_app = graph()

        # Optional: save the agentic workflow as a PNG graph
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        # ------------------------------
        # Pass user query to the agent
        # ------------------------------
        messages = {"messages": [request.query]}   # Wrap query in expected format
        output = react_app.invoke(messages)

        # ------------------------------
        # Extract final answer
        # ------------------------------
        if isinstance(output, dict) and "messages" in output:
            # Take the last AI response
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)

        # Return the agent's response
        return {"answer": final_output}

    except Exception as e:
        # Handle unexpected errors gracefully
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)