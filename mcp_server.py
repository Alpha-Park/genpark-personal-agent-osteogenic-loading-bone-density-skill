# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Osteogenic Loading Bone Density Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentOsteogenicLoadingBoneDensity

mcp = FastMCP("PersonalAgentOsteogenicLoadingBoneDensity")
client = PersonalAgentOsteogenicLoadingBoneDensity()

@mcp.tool()
def evaluate_osteogenic_stimulus(
    exercise_type: str = "depth_jump_landing",
    bodyweight_kg: float = 70.0,
    custom_grf_multiple: float = 5.2,
    repetition_cycles: int = 24
) -> str:
    """Calculates Mechanotransduction Osteogenic Index (MOI) and evaluates 4.2x BW mechanostat threshold."""
    import json
    return json.dumps(client.evaluate_osteogenic_stimulus(
        exercise_type, bodyweight_kg, custom_grf_multiple, repetition_cycles
    ), indent=2)

@mcp.tool()
def prescribe_weekly_bone_density_protocol(
    age: int = 42,
    t_score: float = -1.2,
    current_activity_level: str = "moderate"
) -> str:
    """Prescribes mechanical loading protocol based on DEXA T-Score and age."""
    import json
    return json.dumps(client.prescribe_weekly_bone_density_protocol(
        age, t_score, current_activity_level
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
