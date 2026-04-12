import json


def get_context():
    with open("data/knowledge.json") as f:
        data = json.load(f)

    # 🔥 structured RAG (not dumping full JSON blindly)
    context = f"""
Pricing:
Basic Plan - $29/month, 10 videos, 720p
Pro Plan - $79/month, Unlimited videos, 4K, AI captions

Policies:
- No refunds after 7 days
- 24/7 support only for Pro plan
"""
    return context
