# -*- coding: utf-8 -*-
"""Personal Agent Osteogenic Loading Bone Density Skill.

Zero-dependency Frost's Mechanostat bone mechanotransduction modeler,
ground reaction force (GRF) osteogenic threshold indexer, and axial loading protocol prescriptor.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentOsteogenicLoadingBoneDensity:
    """Quantitative bone mineral density (BMD) mechanotransduction engine based on
    Harold Frost's Mechanostat theory and dynamic ground reaction force (GRF) thresholds."""

    # Dynamic GRF multiples by activity
    ACTIVITY_GRF_MAP = {
        "walking": 1.3,
        "jogging": 2.5,
        "running_sprint": 3.8,
        "depth_jump_landing": 5.2,
        "heavy_axial_deadlift_squat": 4.5,
        "heel_drops_stamping": 4.3,
        "jumping_rope": 3.2
    }

    def evaluate_osteogenic_stimulus(
        self,
        exercise_type: str = "depth_jump_landing",
        bodyweight_kg: float = 70.0,
        custom_grf_multiple: Optional[float] = None,
        repetition_cycles: int = 24
    ) -> Dict[str, Any]:
        """Calculates Mechanotransduction Osteogenic Index (MOI) and evaluates femoral neck /
        lumbar spine osteoblast remodeling threshold (>= 4.2x bodyweight)."""
        key = exercise_type.lower().replace(" ", "_")
        grf = custom_grf_multiple if custom_grf_multiple else self.ACTIVITY_GRF_MAP.get(key, 2.5)
        bw = max(30.0, float(bodyweight_kg))
        reps = max(1, int(repetition_cycles))

        # Absolute peak dynamic force in Newtons
        peak_force_newtons = round(bw * 9.81 * grf, 1)

        # Frost's Mechanostat Thresholds:
        # Minimum effective strain for osteogenesis ~ 1500 - 3000 microstrain
        # In vivo human bone modeling requires >= 4.2x bodyweight dynamic impact
        threshold_met = grf >= 4.2
        strain_tier = "Remodeling Trigger (Osteoblast Anabolism)" if threshold_met else (
            "Maintenance Lazy Zone (Sub-Threshold)" if grf >= 2.0 else "Bone Inactivity Resorption Risk"
        )

        # Mechanotransduction Osteogenic Index (MOI: 0 - 100)
        # Saturated logarithmically by repetition cycles (bone desensitizes after ~30-40 cycles)
        cycle_factor = math.log(1.0 + min(50, reps)) / math.log(51.0)
        moi_raw = (grf / 5.5) * 80.0 * cycle_factor
        moi = round(min(100.0, max(5.0, moi_raw)), 1)

        if moi >= 65.0:
            osteogenic_efficiency = "Superior Osteogenic Stimulus / High Bone Mineral Accretion"
        elif moi >= 40.0:
            osteogenic_efficiency = "Moderate Osteogenic Signal / Preservation of Cortical Thickness"
        else:
            osteogenic_efficiency = "Sub-Osteogenic / Insufficient Strain for Trabecular Remodeling"

        return {
            "exercise_type": exercise_type,
            "bodyweight_kg": bw,
            "peak_ground_reaction_force_multiple": grf,
            "peak_impact_force_newtons": peak_force_newtons,
            "repetition_cycles": reps,
            "mechanostat_osteogenic_threshold_met": threshold_met,
            "bone_strain_regime": strain_tier,
            "mechanotransduction_osteogenic_index_moi": moi,
            "osteogenic_adaptation_rating": osteogenic_efficiency,
            "cellular_transduction_note": (
                "Dynamic impacts generate fluid shear stress in osteocyte lacunar-canalicular network, "
                "down-regulating sclerostin and stimulating Wnt/beta-catenin osteogenesis."
            )
        }

    def prescribe_weekly_bone_density_protocol(
        self,
        age: int,
        t_score: float = -1.2,
        current_activity_level: str = "moderate"
    ) -> Dict[str, Any]:
        """Prescribes age-appropriate mechanical loading cycles and impact frequency
        based on DEXA T-Score classification."""
        if t_score >= -1.0:
            category = "Normal Bone Mineral Density"
            impact_protocol = "High-Impact Plyometrics & Heavy Axial Resistance (4.5x - 5.5x BW)"
            weekly_sets = "3 sessions / week of 30 dynamic loading cycles"
        elif t_score > -2.5:
            category = "Osteopenia (Low Bone Mass)"
            impact_protocol = "Progressive Heel Drops, Stamping, and Supervised Resistance Training (3.5x - 4.5x BW)"
            weekly_sets = "3 sessions / week of 20-30 controlled stamping cycles"
        else:
            category = "Osteoporosis (Fragility Risk)"
            impact_protocol = "Low-Impact Mechanostimulation (Whole-body vibration, walking with weight vest, balance stability)"
            weekly_sets = "Daily low-impact vibration + postural alignment exercises; avoid unmitigated sudden high impact"

        return {
            "chronological_age": age,
            "dexa_t_score": t_score,
            "clinical_bmd_category": category,
            "prescribed_osteogenic_protocol": impact_protocol,
            "recommended_weekly_volume": weekly_sets,
            "nutritional_cofactor_mandate": (
                "Ensure elemental Calcium (1000-1200 mg), Vitamin D3 (2000-4000 IU), Vitamin K2 MK-7 (100-200 mcg), "
                "and dietary protein >= 1.2 g/kg/day for collagen matrix mineralization."
            )
        }
