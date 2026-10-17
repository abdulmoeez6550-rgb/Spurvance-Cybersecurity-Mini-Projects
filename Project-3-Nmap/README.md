# Mini Project 3 — Nmap Network Scanning

## Objective
Learn basic network reconnaissance and port scanning using Nmap in an authorized local environment.

## Tools
- Nmap
- Windows PowerShell
- Python 3

## Target
127.0.0.1 (localhost)

All scans were performed against the local computer.

## Commands

Basic scan:
```powershell
nmap 127.0.0.1
```

Service version detection:
```powershell
nmap -sV 127.0.0.1
```

Start a local HTTP test server:
```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Scan the test server's port in another terminal:
```powershell
nmap -sV -p 8000 127.0.0.1
```

## Observations
- Nmap can identify open TCP ports.
- Service detection attempts to identify applications running on open ports.
- A temporary Python HTTP server was used to demonstrate a locally accessible service.

## Security Considerations
- Scan only systems you own or are authorized to test.
- Open ports indicate exposed services, not necessarily vulnerabilities.
- Close unnecessary services to reduce the attack surface.

## Result
Completed basic localhost port-scanning exercises and tested a temporary HTTP service.
