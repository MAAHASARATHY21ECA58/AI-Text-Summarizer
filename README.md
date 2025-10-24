\# AI Text Summarizer



A \*\*Generative AI project\*\* that summarizes long text documents into concise summaries using Hugging Face Transformers and FastAPI.



\## Features

\- Summarizes long text using a pre-trained AI model

\- REST API for integration

\- Deployable on AWS EC2 or any server

\- Easy to extend for multiple documents or workflows



\## Project Structure

AI-Text-Summarizer/

│

├── summarizer\_app.py # FastAPI application

├── test\_summarizer.py # Sample test script

├── requirements.txt # Python dependencies

├── README.md # Project documentation

└── .gitignore # Ignore virtual environment, pycache, etc.





\## Installation

\## Getting Started (Local Setup) 💻

1\. \*\*Clone the repository\*\*

```bash

git clone https://github.com/<your-username>/AI-Text-Summarizer.git

cd AI-Text-Summarizer

2.Create and activate a virtual environment



bash

Copy code

python -m venv venv

\# Windows

venv\\Scripts\\activate

\# Linux/Mac

source venv/bin/activate

3.Install required packages



bash

Copy code

pip install -r requirements.txt

4.Run the FastAPI app



bash

Copy code

uvicorn summarizer\_app:app --reload

5.Test the API

Open your browser and go to http://127.0.0.1:8000/docs.

Use the /summarize/ endpoint to paste text and get a summary.



How to Use

API Endpoint: POST /summarize/



Example Request:



json

Copy code

{

&nbsp; "text": "Artificial Intelligence (AI) is a field of computer science that enables machines to mimic human intelligence..."

}

Example Response:



json

Copy code

{

&nbsp; "summary": "AI is a branch of computer science that enables machines to replicate human intelligence."

}

Quick Test Locally:

Run the test script to see a sample summary:



bash

Copy code

python test\_summarizer.py





Deploying on AWS EC2 ☁️

Launch an Ubuntu EC2 instance.



SSH into your server:



bash

Copy code

ssh -i "your-key.pem" ubuntu@<EC2\_PUBLIC\_IP>

Update packages \& install Python and Git:



bash

Copy code

sudo apt update \&\& sudo apt upgrade -y

sudo apt install python3 python3-pip git -y

Clone your repository:



bash

Copy code

git clone https://github.com/<your-username>/AI-Text-Summarizer.git

cd AI-Text-Summarizer

Set up virtual environment \& install dependencies:



bash

Copy code

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Run FastAPI on the public IP:



bash

Copy code

uvicorn summarizer\_app:app --host 0.0.0.0 --port 8000

Open your EC2 security group and allow inbound traffic on port 8000.



Access your API online at: http://<EC2\_PUBLIC\_IP>:8000/docs.



Optional Enhancements ✨

Summarize multiple documents (batch processing)



Add a web interface for non-technical users



Automate summarization using n8n



Make it production-ready with nginx + Gunicorn and HTTPS



Tech Stack 🛠️

Python 3.10+



Hugging Face Transformers (pipeline("summarization"))



FastAPI



Uvicorn (ASGI server)



AWS EC2 for cloud deployment (optional)



This project is beginner-friendly, portfolio-ready, and a great example of combining AI, Python, and cloud deployment skills.



