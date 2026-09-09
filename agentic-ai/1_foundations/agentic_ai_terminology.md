# Agentic AI Terminology

## Core Concepts

### Artificial Intelligence (AI)
AI is the field of creating computer systems that perform tasks requiring human-like intelligence, such as learning, reasoning, perception, and decision-making.

**Real-world example:** A fraud-detection system identifies unusual banking transactions.

### Generative AI (GenAI)
Generative AI creates new content such as text, images, code, audio, or video based on patterns learned from data.

**Real-world example:** ChatGPT writes an email, or an image model creates a product design.

### Large Language Model (LLM)
An LLM is a neural network trained on large amounts of text to understand and generate human-like language.

**Real-world example:** An LLM summarizes a legal document or writes Python code.

### Prompt
A prompt is the instruction or input given to an AI model to produce a response.

**Real-world example:** `Summarize this report in five bullet points.`

### Token
A token is a small unit of text processed by an LLM. It can be a word, part of a word, punctuation mark, or symbol.

**Real-world example:** The word `playing` may be split into tokens such as `play` and `ing`.

### Context
Context is the information provided to a model so it can understand the current task and respond appropriately.

**Real-world example:** A customer-support assistant receives the customer's previous messages and order details.

### Context Window
A context window is the maximum amount of text, tokens, instructions, and conversation history an LLM can process in one request.

**Real-world example:** A model with a large context window can analyze a long book or many source-code files at once.

### Temperature
Temperature controls how predictable or creative a model's output is. Lower values produce more consistent answers, while higher values produce more varied answers.

**Real-world example:** Use a low temperature for financial calculations and a higher temperature for brainstorming names.

## Knowledge and Retrieval

### Embedding
An embedding is a numerical representation of text, images, or other data that captures meaning and similarity.

**Real-world example:** Documents about `car insurance` and `vehicle coverage` receive similar embeddings.

### Vector Database
A vector database stores embeddings and enables similarity searches across large collections of data.

**Real-world example:** A company searches its internal policies to answer an employee's question.

### Retrieval-Augmented Generation (RAG)
RAG retrieves relevant information from external sources and gives it to an LLM before generating an answer.

**Real-world example:** A chatbot retrieves the latest company handbook section before answering an HR question.

### Grounding
Grounding connects an AI response to reliable data, sources, or current system state.

**Real-world example:** A medical assistant answers using approved clinical documents instead of relying only on the model's general knowledge.

### Hallucination
A hallucination occurs when an AI generates information that sounds plausible but is false, unsupported, or invented.

**Real-world example:** An LLM cites a research paper that does not actually exist.

## Agents and Workflows

### Tool
A tool is an external function or system that an AI can use to perform an action or obtain information.

**Real-world example:** An agent calls a weather API, searches a database, or sends an email.

### Function Calling
Function calling allows an LLM to request a predefined function using structured arguments. The application then executes the function.

**Real-world example:** The model requests `get_order_status(order_id=1234)`.

### Agent
An agent is a software system that uses an AI model to interpret a goal, decide what to do, use tools, and produce a result.

**Real-world example:** A travel agent checks flights, compares prices, and creates an itinerary.

### Agentic AI
Agentic AI refers to AI systems capable of pursuing goals through planning, decision-making, tool usage, and multi-step execution with limited human intervention.

**Real-world example:** An IT agent detects a failed service, investigates logs, restarts the service, and reports the result.

### Agentic Workflow
An agentic workflow is a structured sequence in which an AI system performs multiple steps, makes decisions, and possibly calls tools to complete a task.

**Real-world example:** Read an invoice, extract fields, validate totals, save the result to a database, and notify finance.

### Planning/orchestrator
Planning is the process of breaking a large goal into smaller steps and deciding their order.

**Real-world example:** To organize a meeting, an agent checks calendars, finds a common time, books a room, and sends invitations.

### Reasoning
Reasoning is the process of using available information to reach a conclusion or select an action.

**Real-world example:** An agent determines that a payment failed because the card expired and recommends the next action.

### Memory
Memory allows an AI system to retain useful information across steps or conversations.

**Real-world example:** A personal assistant remembers a user's preferred meeting times.

### Short-Term Memory
Short-term memory is information available during the current task or conversation.

**Real-world example:** An agent remembers the user's current order number while resolving a support request.

### Long-Term Memory
Long-term memory stores information for future interactions or tasks.

**Real-world example:** A learning assistant remembers a student's skill level and previous progress.

### Orchestration
Orchestration coordinates models, tools, agents, workflows, memory, and task execution.

**Real-world example:** A framework routes a request between a research agent, a writing agent, and a review agent.

### Multi-Agent System
A multi-agent system uses multiple specialized agents that cooperate to complete a larger task.

**Real-world example:** One agent researches market data, another analyzes it, and a third writes the report.

## Reliability and Application Development

### Human-in-the-Loop
Human-in-the-loop means a human reviews, approves, or corrects an AI action at an important point.

**Real-world example:** An AI prepares a bank transfer, but a manager must approve it before execution.

### Guardrails
Guardrails are rules, validations, and controls that keep an AI system within safe and allowed boundaries.

**Real-world example:** A support agent must not expose private customer data or issue refunds above a defined limit.

### Structured Output
Structured output requires the model to respond in a defined format such as JSON, a table, or a specific schema.

**Real-world example:** An invoice-extraction model returns:

```json
{
  "invoice_id": "INV-1001",
  "total": 2500
}
```

### API
An API is an interface that allows one software system to communicate with another.

**Real-world example:** An AI application uses a payment API to retrieve a transaction status.

### Inference
Inference is the process of using a trained model to generate a prediction or response for new input.

**Real-world example:** Sending a prompt to an LLM and receiving an answer is inference.

### Fine-Tuning
Fine-tuning adapts a pretrained model using additional task-specific examples.

**Real-world example:** A company fine-tunes a model to classify its internal support tickets.

### Evaluation
Evaluation measures how accurately, safely, reliably, and efficiently an AI system performs its task.

**Real-world example:** Testing whether a customer-support agent gives correct answers to 500 known questions.

### Observability
Observability provides visibility into an AI system's prompts, responses, tool calls, latency, errors, and costs.

**Real-world example:** Developers inspect why an agent repeatedly called the wrong database tool.

### Workflow Automation
Workflow automation executes predefined steps automatically, usually with limited decision-making.

**Real-world example:** Every new invoice is automatically moved from email to cloud storage.

### Agentic Automation
Agentic automation combines automation with dynamic decision-making, allowing the system to choose actions based on changing conditions.

**Real-world example:** An agent reads different types of invoices, identifies exceptions, and decides whether human review is needed.

## Simple Relationship

```text
AI
├── Machine Learning
├── Generative AI
│   └── Large Language Models
└── Agentic AI
    ├── LLM
    ├── Tools
    ├── Memory
    ├── Planning
    └── Workflows
```

## Traditional Automation vs. Agentic AI

### Traditional Automation

```text
Step 1 -> Step 2 -> Step 3 -> Step 4
```

The steps are predefined and usually do not change.

### Agentic Workflow

```text
Goal -> Observe -> Plan -> Use tools -> Evaluate result -> Continue or finish
```

The system can choose different steps depending on the situation.

## Key Difference to Remember

> An AI model generates an answer. An agent uses an AI model to accomplish a goal. Agentic AI refers to systems that can plan, act, use tools, and adapt across multiple steps.
