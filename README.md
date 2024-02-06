# RotMG-Tokens
Extract accessToken and clientToken from RotMG client

This simple script uses a MITM proxy to capture all verify requests from the RotMG client and extracts user tokens. Please ensure you have mitmproxy correctly configured; run in destination folder: §mitmproxy -s app.py
