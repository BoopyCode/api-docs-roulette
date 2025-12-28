#!/usr/bin/env python3
# API Docs Roulette - Because guessing is faster than reading (sometimes)

import random
import sys
import json
from typing import Dict, List, Any

# The sacred texts of API documentation (mostly fiction)
DOCS_DB = {
    "endpoints": [
        {"path": "/api/v1/users", "method": "GET", "description": "Get users. Maybe."},
        {"path": "/api/v2/things", "method": "POST", "description": "Create a thing. Probably."},
        {"path": "/api/legacy/stuff", "method": "DELETE", "description": "Removes stuff. Or adds it. Who knows?"},
        {"path": "/graphql", "method": "POST", "description": "It's GraphQL, figure it out yourself."},
        {"path": "/health", "method": "GET", "description": "Returns 'OK' unless it doesn't."}
    ],
    "parameters": [
        "page", "limit", "sort", "filter", "q", "api_key", "secret", "magic_token",
        "callback", "format", "pretty", "debug", "no_cache", "timestamp", "signature"
    ],
    "responses": [
        {"status": 200, "body": {"data": [], "meta": {"count": 0}}},
        {"status": 400, "body": {"error": "Invalid something"}},
        {"status": 401, "body": {"error": "Not authorized (but we won't tell you why)"}},
        {"status": 404, "body": {"error": "Not found (or maybe it's just hiding)"}},
        {"status": 429, "body": {"error": "Too many guesses (I mean requests)"}},
        {"status": 500, "body": {"error": "Our bad, but you fix it"}}
    ],
    "tips": [
        "Try adding ?debug=true to everything",
        "The real API is at /api/v3 but docs say v1",
        "Authentication works randomly on Tuesdays",
        "Pagination is broken but documented as 'feature'",
        "The 'limit' parameter actually limits your patience"
    ]
}

def spin_roulette() -> Dict[str, Any]:
    """Spin the wheel of API misfortune!"""
    return {
        "endpoint": random.choice(DOCS_DB["endpoints"]),
        "params": random.sample(DOCS_DB["parameters"], k=random.randint(1, 4)),
        "response": random.choice(DOCS_DB["responses"]),
        "tip": random.choice(DOCS_DB["tips"]),
        "confidence": random.randint(1, 100)  # Percentage of docs being accurate
    }

def main() -> None:
    """Your daily dose of API documentation gambling."""
    print("\n🎰 API Docs Roulette - Spin to Win (or lose)!\n")
    
    result = spin_roulette()
    
    print(f"Endpoint: {result['endpoint']['method']} {result['endpoint']['path']}")
    print(f"Description: {result['endpoint']['description']}")
    print(f"\nTry these params: {', '.join(result['params'])}")
    print(f"\nExpected response: {json.dumps(result['response'], indent=2)}")
    print(f"\n💡 Pro tip: {result['tip']}")
    print(f"\n📊 Documentation confidence: {result['confidence']}% (good luck!)\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSmart choice. Reading the actual docs might work better.")
        sys.exit(0)
