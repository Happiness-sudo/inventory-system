# Inventory Management System

## Description
This is a simple Flask REST API for managing inventory.
Users can add, view, update, and delete items.
It also fetches product data from OpenFoodFacts API.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests pytest
python app.py