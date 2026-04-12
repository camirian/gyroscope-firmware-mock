# Context: DO-254 Firmware Compliance Sandbox
# Reason: Enforces strict Python execution parity for RvC compliance generation.
FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Layer 1: Core interaction tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
