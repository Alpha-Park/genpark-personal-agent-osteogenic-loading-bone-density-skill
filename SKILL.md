---
name: genpark-personal-agent-osteogenic-loading-bone-density-skill
version: "1.0.0"
description: "Zero-dependency Frost's Mechanostat bone mechanotransduction modeler, ground reaction force (GRF) osteogenic threshold indexer, and axial loading protocol prescriptor."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Osteogenic Loading Bone Density Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI companions to model bone mechanotransduction, quantify ground reaction force multiples against Harold Frost's Mechanostat ($\ge 4.2\times$ bodyweight threshold), and prescribe axial osteogenic protocols.

## Agent In-Context Capabilities

- **Mechanostat Threshold Evaluation**: Assesses whether dynamic physical exercise exceeds the minimum effective strain ($\sim 1500 \ \mu\varepsilon$) required to down-regulate sclerostin and activate osteoblasts.
- **Mechanotransduction Osteogenic Index (MOI)**: Synthesizes dynamic impact magnitude and log-transformed repetition saturation into a 0-100 osteogenesis rating.
- **DEXA-Guided Staging**: Tailors mechanical loading cycles based on T-scores across Normal, Osteopenia, and Osteoporosis categories.

## Tools Summary

1. `evaluate_osteogenic_stimulus`: Computes peak force in Newtons, threshold achievement, and MOI score.
2. `prescribe_weekly_bone_density_protocol`: Outlines weekly mechanical loading volume and micronutrient cofactors.
