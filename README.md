 Aegis AI: An AI-Powered Tool for Security Monitoring

Aegis AI is a project built to help security teams handle system logs more easily. Usually, checking through thousands of computer logs to find a hacker is a slow and tiring job for a human. This tool uses a group of AI "agents" that work together to do that work automatically.

## Live Link
You can see the project running here: https://aegis-soc-ai-zu8urcnzksljp32xzud6l4.streamlit.app/
(This works on both computers and phones.)

## What it does
Instead of just one AI, this project uses four different AI agents that talk to each other to solve a problem:

1. Detection: This agent looks through the raw logs and picks out anything that looks suspicious, like too many failed passwords.
2. Analysis: This agent takes the suspicious logs and figures out if they are a real threat or just a mistake.
3. Mitigation: If there is a real threat, this agent writes down the exact steps a person should take to fix the problem.
4. Reporting: This agent creates a simple summary for a manager to read so they know what happened.

## Tech used
* Frontend: Streamlit (This is what makes the website and dashboard).
* AI: Gemini 3.1 Flash Lite from Google (This acts as the "brain").
* Language: Python.
* Flow: A sequential chain where each AI agent passes its notes to the next one.

## How to run it yourself
1. Clone this repository.
2. Install the necessary tools by running:
   pip install -r requirements.txt
3. Start the application by running:
   python -m streamlit run app.py

