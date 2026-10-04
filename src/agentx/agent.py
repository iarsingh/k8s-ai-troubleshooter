TOOLS = ["read_events", "read_logs", "read_metrics", "search_runbook", "hypothesize"]
WRITES = ("kubectl apply", "kubectl delete", "drain",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    blob = " ".join(payload.get("events") or []).lower(); result = "image_pull" if "pull" in blob else "crashloop" if "backoff" in blob else "oom" if "oom" in blob else "unknown"
    return {"refused": False, "tools": TOOLS, "hypothesis": result, "applied": False, "needs_approval": False}
