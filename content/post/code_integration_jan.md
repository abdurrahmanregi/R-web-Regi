---
title: "LLM, Chatbot, and running Python and R codes"  # Copy the title from your Medium post
date: "2025-08-10"  # Use the original publication date or today's date (format: YYYY-MM-DD)
author: "Regi Kusumaatmadja"  # Your name as it appears on Medium
summary: "Simple setup to let LLM in a chatbot to run Python and R codes. Usually, LLM only runs Python via an isolated VM, but not other languages."  # Write a 1-2 sentence teaser
---

### Intro
I am using Grok 4 in Jan (a chatbot-like environment, similar to ChatGPT) to directly run Python and R codes on my computer. Why do I do this? I wanted to reduce the 'hallucination' part of LLM. 

Think about it this way, if you use an LLM from a web-based app, such as chat.openai.com, grok.com, or gemini.google.com, it will run Python codes via an isolated VM. You can think of isolated VM as a 'sandbox' environment, where the LLM can run Python codes, but it cannot access your local files or run other languages such as R.

My idea here is to let the LLM run Python and R codes directly on my computer, so it can access my local files and run other languages. This way, I can reduce the 'hallucination' part of LLM, because it can access my local files, packages/libraries, and run other languages.

### Setup
First, let us setup the environment for Grok. The prompt initiation I use is the following
```text
You are a smart AI with deep reasoning capability that always tries to reason from first principles.
You have access to a set of tools to help you answer the user’s question. You can use only one tool per message, and you’ll receive the result of that tool in the user’s next response. To complete a task, use tools step by step—each step should be guided by the outcome of the previous one.
Tool Usage Rules:
1. Always provide the correct values as arguments when using tools. Do not pass variable names—use actual values instead.
2. You may perform multiple tool steps to complete a task.
3. Avoid repeating a tool call with exactly the same parameters to prevent infinite loops.
4. Think deeply and thoroughly. Use your own reasoning capability with high effort. Think sequentially. Think harder! Reflect. 
5. For web-related searches, leverage Tavily's tools (tavily-search for broad aggregation, tavily-extract for content pulls, tavily-crawl for multi-page scraping, tavily-map for site outlining) and Linkup's search-web (for deep, premium-sourced accuracy) complementarily. Prioritize Tavily for wide exploration to gather diverse overviews and initial URLs; use Linkup for deep verification and fact-checking on complex, academic, and/or business-specific queries. Chain tools sequentially: Start with tavily-search or search-web based on breadth vs. depth needs, then deepen by extracting/crawling with Tavily on results, alternating between APIs if outputs are incomplete, biased, or require cross-validation. Refine queries iteratively from prior outputs to ensure comprehensive, grounded responses.
6. For Python-based computations, data analysis, simulations, scripting tasks or others, use run_code_py to execute code on the local computer. This tool supports a stateful REPL environment with libraries including numpy, scipy, sympy, scikit-learn, pandas, matplotlib, nltk, beautifulsoup4, and others. Ensure code is properly formatted with correct indentation, import necessary libraries explicitly, and avoid operations that require internet access or external installations. Use this tool for tasks like numerical modeling, machine learning prototypes, data visualization, or web scraping simulations, chaining executions step-by-step based on previous outputs for iterative refinement.
7. For R-based statistical analysis, data manipulation, graphing, econometric tasks or others, use run_code_r to execute code on the local computer. This tool supports a stateful REPL environment with packages including data.table, ggplot2, fixest, parallel, and others. Ensure code is properly formatted, load necessary packages explicitly (e.g., library(data.table)), and avoid operations that require internet access or external installations. Use this tool for tasks like advanced regressions, parallel processing, data wrangling, or visualizations, selecting it over run_code_py when R's specialized statistical ecosystem is more suitable, and chain executions iteratively guided by prior results for complex workflows.
8. When choosing between run_code_py and run_code_r, assess the task's nature: Prefer run_code_r for statistics-heavy work (e.g., econometrics with fixest, fast data manipulation with data.table, or publication-quality plots with ggplot2), especially if the user mentions R or R-specific concepts. Prefer run_code_py for general scripting, numerical computations (e.g., with numpy/scipy), machine learning (e.g., scikit-learn), or text processing (e.g., nltk/beautifulsoup4), especially if Python is mentioned. If the user specifies a language, adhere strictly to it; if ambiguous, default to the tool whose libraries best match the task's core requirements, and consider chaining tools across languages only if a workflow explicitly benefits from both (e.g., Python for data prep, R for analysis), while avoiding unnecessary switches to prevent confusion or inefficiency.
```

Next, I set the following predefined parameters:
```json
{
  "temperature": 0.6,
  "top_p": 0.95,
  "top_k": 20
}
```

### Setup Local Python MCP
I create a Python file `run_code_py.py` as follows
```python
import sys
import logging
import io
from contextlib import redirect_stdout, redirect_stderr
from mcp.server.fastmcp import FastMCP

# Set up basic logging to stderr with flushing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', stream=sys.stderr)

mcp = FastMCP("Local Python Executor")

@mcp.tool(title="Execute Python Code")
def run_code_py(code: str) -> str:
    """
    Execute Python code and return the output.
    Supports libraries like pandas, numpy, etc.
    """
    logging.info(f"Received code to execute: {code}")
    sys.stderr.flush()
    out = io.StringIO()
    err = io.StringIO()
    try:
        with redirect_stdout(out), redirect_stderr(err):
            exec(code, {}, {})
        output = out.getvalue().strip()
        error = err.getvalue().strip()
        logging.info(f"Execution result: Output={output}, Error={error}")
        sys.stderr.flush()
        return f"Output:\n{output}\n\nErrors (if any):\n{error}" if output or error else "No output."
    except Exception as e:
        logging.error(f"Exception: {str(e)}")
        sys.stderr.flush()
        return f"Error: {str(e)}"

if __name__ == "__main__":
    logging.info("Server started on stdio...")
    sys.stderr.flush()
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        logging.error(f"Server error: {str(e)}")
        sys.stderr.flush()
```

The idea of the above code is to setup a REPL environment for Grok to run Python codes locally. And, I setup the following `requirements.txt`
```text
pandas
numpy
scipy
scikit-learn
sympy
matplotlib
seaborn
requests
beautifulsoup4
nltk
spacy
textblob
opencv-python
scikit-image
mcp
e2b-mcp
fastapi
uvicorn
pydantic
modelcontextprotocol
fastmcp
```

You can, of course, have different libraries to be used. But I found these are the libraries I am using a lot. Here I am following the community suggestion to have isolated Python libraries. You can then just `uv pip install -r requirements.txt` to install all of the libraries.

Now, let us add the local Python MCP Server to Jan. Here is the JSON.
```json
{
  "command": "C:\\Users\\abdur\\Documents\\python-MCP\\venv\\Scripts\\python.exe",
  "args": [
    "-u",
    "C:\\Users\\abdur\\Documents\\python-MCP\\run_code_py.py"
  ],
  "env": {},
  "active": true
}
```

That's it for the local Python MCP setup!

### Setup Local R MCP
Next, let us setup the local R MCP. I create a file `run_code_r.R` as follows
```r
library(mcpr)

# Create a global environment to maintain state across tool calls
repl_env <- new.env(parent = globalenv())

# Define the run_code tool
run_code_tool <- new_tool(
  name = "run_code_r",
  description = "Execute arbitrary R code in a stateful REPL-like environment. Previous executions persist in the environment, similar to a console session. The tool captures and returns the output, including printed results or errors.",
  input_schema = schema(
    properties = properties(
      code = property_string(
        "Code", 
        "The R code to execute. Can be single or multi-line statements.",
        required = TRUE
      )
    )
  ),
  handler = function(input) {
    code_str <- input$code
    
    # Attempt to parse and execute the code
    tryCatch({
      # Capture output from evaluation and potential auto-printing
      output <- capture.output({
        parsed_code <- parse(text = code_str)
        result <- withVisible(eval(parsed_code, envir = repl_env))
        if (result$visible) {
          print(result$value)
        }
      })
      
      # Return the captured output as text
      response_text(paste(output, collapse = "\n"))
    }, error = function(e) {
      # Return error message if execution fails
      response_text(paste("Error:", e$message))
    })
  }
)

# Create the MCP server
r_code_server <- new_server(
  name = "run_code_r",
  description = "A server for running R code via MCP, providing a stateful code execution capability.",
  version = "1.0.0"
)

# Add the run_code tool to the server
r_code_server <- add_capability(r_code_server, run_code_tool)

# Serve the MCP server
serve_io(r_code_server)
```

The code uses a new package called `mcpr`. The main difference between R setup to the Python ones is that, for R, I have a global libraries. So no versioning for R (Oops!).

Now, let us add the local R MCP Server to Jan. Here is the JSON.
```json
{
  "command": "Rscript",
  "args": [
    "C:\\Users\\abdur\\OneDrive\\Work\\R-MCP\\run_code_r.R"
  ],
  "env": {},
  "active": true
}
```

That's it for the local R MCP setup!

### Usage and Examples
Now, we can use Grok in Jan, and ask it to run something using Python and R natively, in our computer.

Prompt:
```
Run a Monte Carlo simulation with 10,000 iterations to estimate \pi. use run_code_py tools
```

Grok's answer:
```
The Monte Carlo simulation with 10,000 iterations estimates π as approximately 3.1476.
```

and to answer the above, Grok is natively using `run_code_py`. See the following JSON argument and output.

Arguments:
```json
{"code":"import random\nn = 10000\ninside = 0\nfor _ in range(n):\n    x = random.uniform(-1, 1)\n    y = random.uniform(-1, 1)\n    if x**2 + y**2 <= 1:\n        inside += 1\npi_estimate = 4 * inside / n\nprint(pi_estimate)"}
```

Output:
```json
{
  "text": "Output:\n3.1476\n\nErrors (if any):\n",
  "type": "text"
}
```

I ask Grok again to now use `run_code_r` tools.

Prompt: 
```
Now do the same but with run_code_r tools
```

Grok's answer:
```
The Monte Carlo simulation with 10,000 iterations using R estimates π as approximately 3.1364.
```

and to answer the above, Grok is natively using `run_code_r`. See the following JSON argument and output.

Arguments:
```json
{"code":"n <- 10000\nx <- runif(n)\ny <- runif(n)\ninside <- sum(x^2 + y^2 <= 1)\npi_estimate <- 4 * inside / n\nprint(pi_estimate)"}
```

Output:
```json
{
  "text": "[1] 3.1364",
  "type": "text"
}
```

### Final Thoughts
A very exciting development in AI that I use at this moment! I think people can barely cheaply criticize AI by using the slur of `stochastic parrot` anymore. Haha!