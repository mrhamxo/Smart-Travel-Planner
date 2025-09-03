from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool


class GraphBuilder():
    
    def __init__(self, model_provider: str = "groq"):
        """
        Initialize the GraphBuilder.
        - Load the LLM from the chosen provider (default = groq).
        - Load all tools (weather, place search, calculator, currency conversion).
        - Bind the tools to the LLM for tool calling.
        """
        
        # Load model using ModelLoader
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        # Initialize tools list
        self.tools = []
        
        # Load each tool category
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()
        
        # Extend tool list with all available tools
        self.tools.extend([* self.weather_tools.weather_tool_list, 
                           * self.place_search_tools.place_search_tool_list,
                           * self.calculator_tools.calculator_tool_list,
                           * self.currency_converter_tools.currency_converter_tool_list])
        
        # Bind the tools to the LLM (so the LLM can call them when needed)
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        # Placeholder for compiled graph
        self.graph = None
        
        # Load system prompt (defines the agent’s personality/role)
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self, state: MessagesState):
        """
        Main agent function (the 'brain').
        - Takes current conversation state (messages).
        - Prepends system prompt.
        - Sends to the LLM (with tools enabled).
        - Returns the response as new messages in the state.
        """
        
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question  # Add system prompt to context
        response = self.llm_with_tools.invoke(input_question)  # Call LLM with tool-binding
        
        return {"messages": [response]}
    
    def build_graph(self):
        """
        Build the LangGraph agent workflow:
        - Define nodes: agent + tools
        - Define edges: flow between agent <-> tools
        - Add conditional logic for when to call tools
        - Compile and return the graph
        """
        
        graph_builder = StateGraph(MessagesState)
        
        # Add nodes
        graph_builder.add_node("agent", self.agent_function)         # Agent reasoning node
        graph_builder.add_node("tools", ToolNode(tools=self.tools))  # Tools execution node
        
        # Add edges
        graph_builder.add_edge(START,"agent")                        # Start → Agent
        graph_builder.add_conditional_edges("agent", tools_condition) # Agent → Tool (if needed)
        graph_builder.add_edge("tools","agent")                      # Tools → Agent
        graph_builder.add_edge("agent",END)                          # Agent → End
        
        # Compile the graph
        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        """
        Allow the class instance to be called directly like a function.
        Example: graph = GraphBuilder("groq")()
        """
        return self.build_graph()
