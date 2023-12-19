# MCQ Quiz Application

## Table of Contents

1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [Generating a Quiz](#generating-a-quiz)
    - [Submitting and Viewing Quiz Results](#submitting-and-viewing-quiz-results)
5. [Customization](#customization)
    - [OpenAI API Key](#openai-api-key)
    - [LangChain Configuration](#langchain-configuration)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

## 1. Introduction

The MCQ Quiz Application is a Python-based web application built using Streamlit, OpenAI Chat Completion API, and LangChain. This application allows users to interactively participate in quizzes on a topic of their choice, with dynamically generated questions and answers.

## 2. System Overview

The application comprises a backend logic written in Python, utilizing the Streamlit library for the frontend interface. LangChain is employed for dynamic quiz question generation, and the OpenAI Chat Completion API is used for generating answer options.

## 3. Installation

To install the required dependencies, run the following command:

```bash
pip install streamlit openai langchain
```
## 4. Usage

### 4.1 Running the Application
Execute the following command in your terminal to run the application:
```bash
streamlit run quiz_app.py
```
This will launch a local server, and you can access the application in your web browser at the specified URL.

### 4.2 Generating a Quiz
1. Enter your preferred quiz topic in the provided text input.
2. Specify the number of questions you want in the quiz.
3. Click the "Generate Quiz" button.

### 4.3 Submitting and Viewing Quiz Results
1. Answer each question by selecting one or more options.
2. Click the "Submit Quiz" button.
3. View your quiz results, including the correct and incorrect answers.

## 5. Customization
### 5.1 OpenAI API Key
Replace the API key in the line stating "YOUR_OPENAI_API_KEY_HERE" in the quiz_app.py file with your actual OpenAI API key.

### 5.2 LangChain Configuration
No additional configuration is required for LangChain. However, you can explore the LangChain documentation for advanced customization options.

## 6. Troubleshooting
If you encounter any issues, make sure you have a stable internet connection.
Check for updates to the application and libraries.

