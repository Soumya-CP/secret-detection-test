# TESTCASE: SD-013 JWT-like three-segment token (synthetic; signature is not valid)
FAKE_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0LXVzZXIiLCJyb2xlIjoiYWRtaW4ifQ.ZmFrZS1zaWduYXR1cmUtZm9yLXRlc3Rpbmctb25seQ"

# Public identifier only; should not be reported as a secret.
PUBLIC_CLIENT_ID = "00000000-0000-0000-0000-000000000000"
