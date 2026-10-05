from agentx.progression import k8s_rca

def test_k8s_rca_oom():
    out = k8s_rca(["CrashLoopBackOff"], ["oom killed"], {"mem": 99}, ["raise memory after leak confirmed"])
    assert "OOM" in out["hypothesis"]
    assert out["applied"] is False

