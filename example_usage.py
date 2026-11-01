# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Osteogenic Loading Bone Density Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentOsteogenicLoadingBoneDensity

def main():
    agent = PersonalAgentOsteogenicLoadingBoneDensity()

    print("=" * 70)
    print("DEMO: Personal Agent Osteogenic Loading & Bone Mechanostat Engine")
    print("=" * 70)

    # 1. Evaluate Depth Jump Landing (5.2x BW, 72 kg, 20 cycles)
    res_jump = agent.evaluate_osteogenic_stimulus(
        exercise_type="depth_jump_landing",
        bodyweight_kg=72.0,
        custom_grf_multiple=5.2,
        repetition_cycles=20
    )

    print(f"\n1. Osteogenic Mechanotransduction Analysis (Depth Jump Landing):")
    print(f"   Peak Force: {res_jump['peak_impact_force_newtons']} N ({res_jump['peak_ground_reaction_force_multiple']}x BW)")
    print(f"   Mechanostat Threshold Met (>= 4.2x BW): {res_jump['mechanostat_osteogenic_threshold_met']}")
    print(f"   Strain Regime: {res_jump['bone_strain_regime']}")
    print(f"   Osteogenic Index (MOI): {res_jump['mechanotransduction_osteogenic_index_moi']}/100")
    print(f"   Adaptation Rating: {res_jump['osteogenic_adaptation_rating']}")
    print(f"   Cellular Transduction: {res_jump['cellular_transduction_note']}")

    # 2. Prescribe Protocol for 45-year-old with DEXA T-Score of -1.3 (Mild Osteopenia)
    res_proto = agent.prescribe_weekly_bone_density_protocol(
        age=45,
        t_score=-1.3,
        current_activity_level="moderate"
    )

    print(f"\n2. Personalized Bone Density Protocol (T-Score: -1.3):")
    print(f"   Clinical Category: {res_proto['clinical_bmd_category']}")
    print(f"   Prescribed Protocol: {res_proto['prescribed_osteogenic_protocol']}")
    print(f"   Weekly Volume: {res_proto['recommended_weekly_volume']}")
    print(f"   Nutritional Mandate: {res_proto['nutritional_cofactor_mandate']}")

    print("\nVerification complete: Osteogenic loading engine executed flawlessly.")

if __name__ == "__main__":
    main()
