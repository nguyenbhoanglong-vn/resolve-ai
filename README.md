# ResolveAI

AI-powered support ticket triage and management system.

## About

ResolveAI helps support teams automatically classify,
prioritize and summarize customer support tickets using
a large language model.

## Features

- Create support tickets
- AI ticket classification
- AI priority detection
- Automatic summarization
- Suggested support actions
- AI-generated response drafts
- Ticket status management
- Support dashboard
- REST API
- SQLite persistence

## Tech Stack

### Frontend

- React
- Vite
- JavaScript

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- SQLite

### AI

- OpenAI API

## Architecture

```text
React
  |
REST API
  |
FastAPI
  |
SQLAlchemy
  |
SQLite

FastAPI
  |
AI Service
  |
LLM API
