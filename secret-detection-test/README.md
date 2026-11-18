# Secret Detection Test Corpus

Purpose: a safe, synthetic corpus for exercising **14 secret-detection rules**.

Every credential-like value in this repository is fabricated and non-functional. These are pattern fixtures, not working credentials. Do not replace them with real credentials. No fixture calls a cloud API or authenticates anywhere.

## Contents

- `fixtures/` contains examples in dotenv, JSON, YAML, PEM-like, Python, and JavaScript formats.
- `rules.json` describes the 14 expected detector rules.
- `expected-findings.csv` maps each positive marker to a file and line.
- `fixtures/negative-controls/` contains examples that should not be reported as secrets (environment-variable references, documentation placeholders, and public identifiers).

## Validation guidance

1. Scan the repository recursively, including hidden files such as `.env.example`.
2. Confirm all rule IDs in `rules.json` have at least one finding.
3. Check that negative controls are not reported as exposed credentials.
4. Pattern matching should be followed by context/entropy/format checks. JWT-looking strings should be parsed as three base64url segments; provider tokens should be matched against provider-specific prefixes and expected character classes.
5. Treat `EXAMPLE`, `FAKE`, all-zero and `test` fixtures as synthetic test data. This repository deliberately does not contain valid cloud or SaaS credentials.

**Safety:** never deploy these files or use this corpus as application configuration.
