# LangChain Search Agent - AI-Powered Networking Assistant

This project is a simple LangChain project generator that helps you learn about people by automatically gathering and analyzing their professional and social media presence. It combines LangChain, OpenAI's GPT models, and various web scraping tools to create meaningful insights about a person. It leverages the ReAct agent strategy to orchestrate the workflow and Langchain tools to scrape the web.

## Features

- **LinkedIn Profile Analysis**: Automatically finds and scrapes LinkedIn profiles to gather professional information
- **Twitter Integration**: Discovers and analyzes recent tweets to understand a person's current interests and activities
- **Smart Summary Generation**: Creates concise summaries and interesting facts about people by combining multiple data sources
- **Automated Web Search**: Uses Tavily Search API to intelligently find relevant social media profiles

## Technical Stack

- **LangChain**: For orchestrating the AI workflow and agent creation
- **OpenAI GPT-4**: Powers the intelligent analysis and summary generation
- **Tavily Search API**: For accurate web search results
- **Python**: Core programming language

## How It Works

1. Takes a person's name as input
2. Uses specialized agents to find their LinkedIn and Twitter profiles
3. Scrapes relevant information from both platforms
4. Generates a comprehensive summary including:
   - Brief professional overview
   - Interesting facts about the person
   - Recent activities and interests based on social media

## Usage

The main functionality is accessed through the `search_agent()` function:
