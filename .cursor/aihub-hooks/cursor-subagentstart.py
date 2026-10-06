#!/usr/bin/env python3

"""AI Hub governance hook projection: cursor-subagentstart."""
import json
import sys

payload = json.load(sys.stdin)
if not isinstance(payload, dict):
    msg = "hook input must be a JSON object"
    raise TypeError(msg)
response = json.loads('{"permission":"allow"}')
json.dump(response, sys.stdout, ensure_ascii=False, separators=(",", ":"))
sys.stdout.write("\n")
