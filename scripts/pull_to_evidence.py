import json, hashlib, datetime, pathlib, urllib.request

API_URL = "https://robust-respect-production-741b.up.railway.app/api"

base = pathlib.Path.home() / "HHI_Audits"
today = datetime.date.today().isoformat()
outdir = base / "evidence" / today
outdir.mkdir(parents=True, exist_ok=True)

# fetch runtime telemetry
with urllib.request.urlopen(API_URL) as r:
    runtime = json.loads(r.read().decode())

# map to evidence object
evidence = {
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "system": "HHI_Governance_Infrastructure_Layer",
    "control_id": "ISO27001-A.12",
    "event_type": "runtime_snapshot",
    "state": runtime.get("severity_label","unknown").lower(),
    "actor": "system",
    "authority_chain": "validated",
    "checksum": "",
    "trace_id": f"trace-{int(datetime.datetime.utcnow().timestamp())}",
    "severity": runtime.get("severity_label","UNKNOWN"),
    "enforcement_action": "none" if runtime.get("severity_level",0)==0 else "escalate",
    "scores": runtime.get("scores",{})
}

# write file
outfile = outdir / f"evidence_{int(datetime.datetime.utcnow().timestamp())}.json"
outfile.write_text(json.dumps(evidence, indent=2))

# checksum
digest = hashlib.sha256(outfile.read_bytes()).hexdigest()
evidence["checksum"] = digest
outfile.write_text(json.dumps(evidence, indent=2))

print(f"wrote {outfile}")
