yaml/advancement.yaml:
# Flow RPG Advancement System
# Version: 2.0-restructured
# Rebalanced milestone progression and character development

advancement_system:
  philosophy:
    core_concept: "Frequent rewards with bounded progression"
    design_principles:
      - "Reward every session to maintain engagement"
      - "Horizontal growth through Minor Milestones"
      - "Vertical growth through Major Milestones"
      - "Player choice drives character development"
      - "No automatic stat increases that break math"
      - "Major power spikes arrive early enough to enjoy"

  campaign_length:
    sessions: "8-12"
    philosophy: "Campaign-length game system designed for complete story arcs"
    retirement: "Characters retire or transition to NPCs around session 12"

  milestone_schedule:
    minor:
      frequency: "Every session"
      total_expected: "8-12 in typical campaign"
      philosophy: "Horizontal growth and specialization"

    moderate:
      frequency: "Every 3 sessions"
      first: "Session 3"
      second: "Session 6"
      third: "Session 9"
      total_expected: "3 in typical campaign"
      philosophy: "Significant capability expansion"

    major:
      frequency: "Sessions 5 and 10"
      first: "Session 5"
      second: "Session 10"
      total_expected: "2 in typical campaign"
      philosophy: "Transformative evolution - regional heroes, then legendary figures"

# ============================================
# MINOR MILESTONES
# ============================================

minor_milestones:
  frequency: "Every session"
  philosophy: "Small rewards that add up over time"
  
  triggers:
    - "Complete single session"
    - "Meaningful roleplay moment"
    - "Creative problem solving"
    - "Party cooperation success"

  options:
    skill_development:
      advance_skill:
        description: "Improve one skill by one tier"
        limit: "Maximum Professional (+1) with minor"
        progression:
          - "Untrained (-2) → Novice (-1)"
          - "Novice (-1) → Competent (0)"
          - "Competent (0) → Professional (+1)"
        note: "Higher tiers require Moderate/Major milestones, OR use deepen_expertise option below"

      deepen_expertise:
        description: "Advance Professional (+1) to Expert (+2) through dedication"
        requirement: "Use TWO consecutive minor milestones on the same skill"
        progression: "Professional (+1) → Expert (+2)"
        rationale: "Archetypes start with Professional skills, but standard minor cap prevents advancement. This option allows dedicated specialists to reach Expert through sustained effort."
        example: "Fighter with Combat Professional (+1) uses minor at sessions 1 and 2 to reach Combat Expert (+2)"
        note: "Must commit both milestones before starting - track 'Working toward Expert in [Skill]' on character sheet"

      new_skill:
        description: "Learn new skill"
        starting_level: "Novice (-1)"
        requirement: "Must have used or observed skill"
    
    attribute_adjustment:
      description: "Redistribute attributes"
      mechanic: "+1 to one, -1 to another"
      limit: "Total points unchanged"
      examples:
        - "Lower Grace -1, raise Mind +1"
        - "Reduce Might -1, increase Will +1"
    
    combat_edges:
      description: "Minor combat improvements"
      philosophy: "Specialization, not raw power increase"

      list:
        weapon_technique:
          effect: "Special maneuver with weapon type"
          examples:
            - "Sword: Parry grants +1 defense"
            - "Axe: Cleave hits adjacent enemy"
            - "Bow: Called shot targets weak points"

        armor_adaptation:
          effect: "Reduce specific penalty from armor"
          examples:
            - "Swimming in light armor"
            - "Spellcasting in medium armor"
            - "Stealth in heavy armor"

        combat_style:
          effect: "+1 to specific combat situation"
          examples:
            - "Dueling (1v1 combat)"
            - "Skirmishing (hit and run)"
            - "Formation fighting (with allies)"
        
        quick_draw:
          effect: "Switch weapons free"
          limit: "Once only"
        
        combat_reflexes:
          effect: "+1 to defense rolls"
          limit: "Once only"
        
        fast_movement:
          effect: "+1 zone movement"
          limit: "Once only"
        
        precise_strike:
          effect: "Reroll one damage die per attack"
          limit: "Once only"
        
        flow_harmony:
          effect: "+1 maximum Flow"
          limit: "Three times maximum"
        
        defensive_fighter:
          effect: "+1 Guard in Defensive stance"
          limit: "Once only"
    
    skill_edges:
      description: "+1 to specific skill application"
      examples:
        combat:
          - "Dueling (one-on-one)"
          - "Formation fighting (with allies)"
          - "Mounted combat"
        
        stealth:
          - "Urban environments"
          - "Moving silently"
          - "Hiding in place"
        
        sorcery:
          - "Specific spell school"
          - "Ritual magic"
          - "Counterspelling"
        
        social:
          - "Specific social class"
          - "Intimidation"
          - "Seduction"
    
    calling_exploration:
      description: "Deepen calling understanding"
      options:
        - "Minor mechanical benefit"
        - "Narrative permission expansion"
        - "Roleplay development reward"
  
  appropriate_challenges:
    after_0_3_minor:
      - "Local threats (bandits, wolves)"
      - "Small-scale problems"
      - "Village-level threats"
    
    after_4_6_minor:
      - "Regional dangers"
      - "Organized opposition"
      - "Town-level threats"

# ============================================
# MODERATE MILESTONES
# ============================================

moderate_milestones:
  frequency: "Every 3 sessions"
  philosophy: "Significant capability without breaking math"

  triggers:
    - "Complete story arc"
    - "Defeat significant antagonist"
    - "Major character development"
    - "World-changing decision"

  schedule:
    first:
      timing: "Session 3"
      context: "Players feeling competent"
    second:
      timing: "Session 6"
      context: "Mid-campaign power spike"
    third:
      timing: "Session 9"
      context: "Approaching legendary status"
  
  options:
    choose_one:
      description: "Select ONE improvement per moderate milestone"

      defensive_mastery:
        guard_increase:
          effect: "+3 Guard"
          description: "Improved defensive training"
        damage_reduction:
          effect: "+1 DR (stacks with armor)"
          description: "Toughened body"
        vitality_increase:
          effect: "+2 Vitality"
          description: "Enhanced endurance"

      skill_mastery:
        advance_to_expert:
          from: "Professional (+1)"
          to: "Expert (+2)"
          description: "True expertise - pinnacle of mortal achievement"
          limit: "Total modifier capped at +5 with attributes"
          note: "Expert is the final skill tier"

        new_professional:
          description: "Gain new skill at Professional (+1)"
          requirement: "Related to recent adventures"

        skill_specialization:
          effect: "Choose 3 specific applications, gain +1"
          example: "Combat: Dueling, Mounted, Defensive"

      attribute_improvement:
        description: "Increase one attribute by +1"
        limit: "Maximum +3 total"
        note: "Counts toward skill cap of +5"
    
    signature_move:
      description: "Create personalized technique"
      components:
        name: "Unique to character"
        effect: "Combines existing abilities"
        cost: "1 less Flow than normal (minimum 0)"
        narrative: "Dramatic description"
      
      examples:
        fighter:
          name: "Thundering Charge"
          base_technique: "Charge attack"
          enhancement: "Knocks prone"
          normal_cost: 3
          signature_cost: 2
        
        wizard:
          name: "Prismatic Cascade"
          base_spell: "Fireball"
          enhancement: "Random energy type"
          normal_cost: 1
          signature_cost: 0
        
        rogue:
          name: "Shadow Dance"
          base_technique: "Stealth + Attack"
          enhancement: "Teleport behind"
          normal_cost: 3
          signature_cost: 2
    
    advanced_technique:
      description: "Gain powerful ability"
      requirement: "Flow +3 to use"
      
      combat_techniques:
        whirlwind_strike: "Attack all adjacent"
        perfect_parry: "Negate all damage from source"
        devastating_blow: "Double damage dice"
        combat_flow: "Extra Flow on criticals"
      
      magic_techniques:
        metamagic_mastery: "Apply 2 metamagics"
        spell_combo: "Cast 2 spells in turn"
        flow_channeling: "Convert Vitality to Flow"
      
      skill_techniques:
        skill_mastery: "Auto-succeed once/scene"
        team_coordination: "Grant allies your skill bonus"
        perfect_timing: "Act out of turn order"
    
    calling_evolution:
      description: "Enhance calling benefits"
      options:
        modified_trigger: "Easier or additional trigger"
        secondary_benefit: "Minor additional effect"
        narrative_expansion: "New permission type"
      
      example:
        original: "Guardian gains Flow when ally damaged"
        evolved: "Also gains Flow when healing ally"
  
  appropriate_challenges:
    after_first_moderate:
      - "Regional threats"
      - "Organized armies"
      - "Young dragons"
      - "City-level dangers"
    
    after_second_moderate:
      - "National threats"
      - "Powerful organizations"
      - "Adult dragons"
      - "Planar incursions"

# ============================================
# MAJOR MILESTONES
# ============================================

major_milestones:
  frequency: "Sessions 5 and 10"
  philosophy: "Transformative power achieved while still actively playing"

  triggers:
    - "Defeat major villain"
    - "Save significant population"
    - "Fundamental character transformation"
    - "Complete epic quest"

  schedule:
    first:
      timing: "Session 5"
      context: "Players feel truly heroic"
      significance: "Regional heroes"

    second:
      timing: "Session 10"
      context: "Campaign approaching climax"
      significance: "Legendary figures"
      note: "Final major milestone - campaign concludes around session 12"

    design_note: "Earlier timing ensures players enjoy transformative powers throughout the campaign"

  options:
    choose_one:
      description: "Select ONE transformative improvement"

      legendary_capability:
        perfect_skill:
          effect: "One skill to Expert (+2) if not already"
          plus: "Gain +1 edge in that skill"
          description: "Perfect mastery with specialization"
          limit: "Total modifier still capped at +5"

        attribute_excellence:
          effect: "One attribute to +3, or two attributes +1 each"
          description: "Peak mortal capability"
          limit: "Maximum +3, no supernatural levels"

        vitality_transcendence:
          effect: "+5 Vitality and death saves at advantage"
          description: "Incredibly hard to kill"

      subsystem_mastery:
        description: "Gain or master an archetype subsystem"
        examples:
          - "Combat Techniques from Fighter"
          - "Metamagic from Wizard"
          - "Divine Domain from Cleric"
        benefit: "Full access even without archetype"
    
    calling_transformation:
      complete_change:
        description: "Adopt new calling entirely"
        requirement: "Major story justification"
        example: "Guardian becomes Champion after loss"
      
      calling_synthesis:
        description: "Merge two callings"
        effect: "Both benefits at 75% effectiveness"
        example: "Guardian + Scholar = Protective Sage"
      
      calling_transcendence:
        description: "Rise above calling limits"
        effect: "Lose calling, gain +1 all attributes"
        narrative: "Achieved perfect balance"
    
    legendary_technique:
      description: "Ultimate ability"
      requirement: "Flow +6 to use"
      
      combat:
        unstoppable_assault: "Attack cannot miss"
        death_blow: "Instant kill <50% Vitality"
        battlefield_control: "Reposition all combatants"
        perfect_defense: "Immune to damage for round"
      
      magic:
        reality_break: "Ignore one rule of magic"
        dual_casting: "Cast two spells simultaneously"
        permanent_effect: "Make one spell permanent"
      
      skill:
        impossible_task: "Succeed at impossible"
        inspire_legend: "Grant major bonus to all allies"
        perfect_knowledge: "Know anything about topic"
    
    mythic_edge:
      description: "Supernatural capability"
      
      examples:
        immortal_body:
          effect: "Don't age, immune to disease"
          narrative: "Blessed by gods"
        
        planar_step:
          effect: "Teleport at will (1 Flow)"
          narrative: "Tear reality's fabric"
        
        true_sight:
          effect: "See through all deceptions"
          narrative: "Pierce the veil"
        
        legendary_presence:
          effect: "Enemies must save or flee"
          narrative: "Overwhelming aura"
  
  paragon_paths:
    description: "Specialized evolution at first Major"
    choice: "Defines legendary identity"
    
    examples:
      weapon_master:
        archetype: "Fighter"
        benefits:
          - "All weapons become +1 magical"
          - "Invent new combat techniques"
          - "Cannot be disarmed"
        narrative: "Every weapon sings in your hands"
      
      archmage:
        archetype: "Wizard"
        benefits:
          - "Reduce all spell costs by 1"
          - "Cast signature spell at will"
          - "Sense all magic within mile"
        narrative: "Magic itself bends to your will"
      
      shadow_lord:
        archetype: "Rogue"
        benefits:
          - "Become shadow (incorporeal) 1/scene"
          - "See in absolute darkness"
          - "Teleport between shadows"
        narrative: "Darkness serves you"
      
      divine_champion:
        archetype: "Paladin"
        benefits:
          - "Radiant aura damages evil"
          - "Resurrect once per week"
          - "Smite ignores all defenses"
        narrative: "Living saint walking the earth"
  
  appropriate_challenges:
    after_first_major:
      - "Continental threats"
      - "Demon lords"
      - "Ancient dragons"
      - "Deities' avatars"
    
    after_second_major:
      - "World-ending threats"
      - "Primordial entities"
      - "Gods themselves"
      - "Multiversal dangers"

# ============================================
# EDGES SYSTEM
# ============================================

edges_system:
  description: "Minor improvements providing growth variety"
  introduction: "Alternative to skill/attribute advancement"
  
  categories:
    combat_edges:
      description: "Martial improvements"
      acquisition: "Minor milestones"
      stacking: "Some stack, some don't"
    
    skill_edges:
      description: "Specialized applications"
      acquisition: "Minor milestones"
      stacking: "Different specializations stack"
    
    flow_edges:
      description: "Resource management"
      acquisition: "Minor milestones"
      stacking: "Limited stacking"
    
    social_edges:
      description: "Interaction benefits"
      acquisition: "Minor milestones or roleplay"
      examples:
        reputation: "+1 with specific group"
        contact: "Ally in specific location"
        language: "Learn new language"
    
    equipment_edges:
      description: "Gear improvements"
      acquisition: "Milestone or quest reward"
      examples:
        heirloom_weapon: "Weapon gains minor magic"
        masterwork_tools: "+1 to craft/profession"
        lucky_charm: "Reroll one die per scene"
  
  edge_chains:
    description: "Edges that build on each other"
    
    example_chain_martial:
      1_weapon_focus: "+1 damage with type"
      2_weapon_specialization: "+1 to hit with type"
      3_weapon_mastery: "Critical on 12+ with type"
    
    example_chain_defensive:
      1_tough: "+2 Guard"
      2_very_tough: "+2 more Guard"
      3_incredibly_tough: "+2 more Guard, +1 DR"
    
    example_chain_magical:
      1_flow_harmony: "+1 max Flow"
      2_flow_resonance: "+1 more max Flow"
      3_flow_mastery: "+1 more max, start at +1"

# ============================================
# CAMPAIGN PROGRESSION
# ============================================

campaign_progression:
  typical_timeline:
    sessions_1_2:
      name: "Finding Your Feet"
      milestones: "2 minor"
      typical_modifier: "+0 to +2"
      challenges: "Local threats, bandits, wild animals"
      power_level: "Competent adventurers"

    sessions_3_4:
      name: "Regional Recognition"
      milestones: "1 moderate (session 3), 2 minor total"
      typical_modifier: "+2 to +3"
      challenges: "Organized threats, minor villains"
      power_level: "Local heroes"

    sessions_5_6:
      name: "True Heroes"
      milestones: "1 major (session 5), 1 moderate (session 6), 2 minor total"
      typical_modifier: "+3 to +4"
      challenges: "Regional dangers, young dragons"
      power_level: "Regional champions"

    sessions_7_9:
      name: "Legendary Rise"
      milestones: "1 moderate (session 9), 3 minor total"
      typical_modifier: "+4 to +5"
      challenges: "National threats, powerful organizations"
      power_level: "Famous heroes"

    sessions_10_12:
      name: "Legendary Status"
      milestones: "1 major (session 10), 2-3 minor total"
      typical_modifier: "+5 (at cap)"
      challenges: "World-ending threats, demon lords, ancient dragons"
      power_level: "Legendary heroes"
      note: "Campaign concludes - characters retire at peak power"
  
  power_scaling:
    philosophy: "Bounded accuracy - TN 8 stays relevant throughout"

    skill_caps:
      total_maximum: "+5 (attribute + skill + edges)"
      breakdown:
        attribute: "+3 max (peak natural human)"
        skill: "+2 max (Expert level)"
        edges: "+1 from specializations"

      design_note: "Capped at +5 to maintain challenge throughout 8-12 sessions"

    progression_comparison:
      session_1:
        typical_roll: "2d6 + 0 to +2 (average 7-9)"
        vs_tn_8: "42-58% success"
        note: "Challenging but achievable"

      session_5_with_major:
        typical_roll: "2d6 + 3 to +4 (average 10-11)"
        vs_tn_8: "72-83% success"
        note: "Heroic competence, still meaningful risk"

      session_10_with_two_majors:
        typical_roll: "2d6 + 5 (average 12)"
        vs_tn_8: "97.2% success"
        note: "Legendary mastery - nearly automatic success (only fail on snake eyes 1,1)"
        design_note: "At +5 cap, TN 8 becomes trivial. GMs should use TN 10+ for meaningful challenges at peak power."

    guard_progression:
      starting: "10-13 (based on attributes)"
      session_5: "10-16 (if choosing Guard boosts)"
      session_10: "10-19 (if maximizing defense)"
      note: "No automatic scaling with milestones"
  
  enemy_scaling:
    principle: "Enemies scale with party milestone count"
    reasoning: "PCs should feel growth while maintaining challenge"
    campaign_note: "Designed for 0-12 milestone range (8-12 session campaigns)"

    henchman_total:
      note: "Combined Guard + Vitality"
      formula: "Guard 7 + milestones, Vitality 5 + milestones"
      milestone_0_2: 12
      milestone_3_5: 16
      milestone_6_8: 20
      milestone_9_plus: 24

    elite_total:
      note: "Combined Guard + Vitality"
      formula: "Guard 40 + (milestones × 8), Vitality 70 + (milestones × 14)"
      milestone_0_2: 110
      milestone_3_5: 154
      milestone_6_8: 198
      milestone_9_plus: 242

# ============================================
# ADVANCEMENT VARIANTS
# ============================================

advancement_variants:
  individual_advancement:
    description: "PCs advance separately"
    pros: "Rewards active players"
    cons: "Power gaps, complexity"
    implementation: "Track milestones individually"
  
  xp_hybrid:
    description: "Use XP for minor, milestones for major"
    pros: "Granular progress feeling"
    cons: "More bookkeeping"
    implementation: "100 XP per minor milestone"
  
  achievement_based:
    description: "Specific goals grant advancement"
    pros: "Clear objectives"
    cons: "Can feel videogamey"
    examples:
      - "Defeat 10 orcs: Combat Edge"
      - "Save 3 villages: Guardian calling benefit"
      - "Discover 5 ruins: Lore skill increase"
  
  narrative_only:
    description: "Pure story-based advancement"
    pros: "Maximum flexibility"
    cons: "Can feel arbitrary"
    implementation: "GM awards when appropriate"

# ============================================
# RETIREMENT AND LEGACY
# ============================================

retirement_legacy:
  when_to_retire:
    mechanical: "After 2 major milestones (sessions 10-12)"
    narrative: "Character achieves life goal"
    player_choice: "Always player's decision"
    design_note: "Characters naturally conclude around session 12 at peak power (+5 cap)"
  
  retirement_benefits:
    become_npc:
      description: "Character becomes world figure"
      benefit: "Influences campaign"
    
    found_organization:
      description: "Establish lasting institution"
      benefit: "Creates ally network"
    
    mentor_next:
      description: "Train new character"
      benefit: "New PC starts with bonus"
  
  legacy_system:
    description: "Retired character's impact"
    
    mechanical_legacy:
      student: "New PC starts with extra edge"
      heir: "Inherit legendary item"
      inspired: "Start with higher attribute"
    
    narrative_legacy:
      reputation: "Known as hero's successor"
      connections: "Access to hero's allies"
      mission: "Continue hero's work"

# ============================================
# ADVANCEMENT GUIDELINES
# ============================================

advancement_guidelines:
  core_principles:
    - "Skills are cheaper to improve than attributes"
    - "Specialization beats generalization early"
    - "Guard/Vitality increases are valuable but not mandatory"
    - "Flow techniques multiply effectiveness"

  recommended_progression:
    sessions_1_3:
      priority_1: "Get primary skill to Professional (+1)"
      priority_2: "Pick up combat edge or technique"
      priority_3: "Shore up weaknesses with new skills"
      avoid: "Spreading too thin across many skills"

    session_3_moderate:
      fighter_types:
        recommended: "+3 Guard or signature move"
        alternative: "Skill to Expert (+2)"

      caster_types:
        recommended: "Metamagic or skill mastery"
        alternative: "+1 to casting attribute"

      skill_experts:
        recommended: "Skill specializations"
        alternative: "New Professional skill"

    session_5_major:
      optimal_choices:
        combat_focused: "Perfect skill (Expert + edge) or subsystem mastery"
        magic_focused: "Attribute excellence (casting stat to +3) or legendary technique"
        balanced: "Attribute excellence (two attributes +1) or Vitality transcendence"

      good_choices:
        - "Perfect skill for primary specialty"
        - "Attribute to +3 if not at cap"
        - "Subsystem mastery to gain new capabilities"

      situational_choices:
        - "Vitality transcendence (good for frontline, okay for others)"
        - "Calling transformation (only with narrative justification)"

    sessions_6_10:
      strategy: "Reach +5 cap and fill gaps"
      minors: "Edges, techniques, skill variety"
      session_6_moderate: "Whatever you didn't take at session 3"
      session_9_moderate: "Final skill/attribute push to cap"
      session_10_major: "Complete your build vision - this is your final transformative choice"

  archetype_specific:
    fighter:
      early: "Combat to Professional (+1), weapon techniques"
      mid: "Guard increases, Combat to Expert (+2)"
      late: "Might to +3, battlefield control, signature moves"

    wizard:
      early: "Metamagic, lore skills, Sorcery to Professional (+1)"
      mid: "Mind or Awareness attribute increases, spell combos"
      late: "Casting attribute to +3, Sorcery to Expert (+2), legendary techniques"

    rogue:
      early: "Sneak attack, urban specialization, Grace increases"
      mid: "Finesse/Stealth to Professional (+1), shadow techniques"
      late: "Grace to +3, death mark, impossible dodge"

    cleric:
      early: "Healing techniques, medicine skill, Will increases"
      mid: "Sorcery to Professional (+1), domain powers"
      late: "Will to +3, divine mastery, resurrection"

  custom_build_path:
    advantage: "Can optimize from start"
    sessions_1_2: "Define your niche with skills"
    session_3: "Take what archetypes can't get (moderate milestone)"
    session_5: "Adopt subsystem to catch up (major milestone)"
    sessions_6_10: "Reach +5 cap in primary area"
    session_10: "Final legendary power (major milestone)"
    result: "Become exactly what you envision"

  common_mistakes:
    spreading_thin: "Too many skills at Novice"
    ignoring_defense: "No Guard/Vitality boosts"
    hoarding_flow: "Not learning techniques"
    attribute_obsession: "Attributes over skills"

  reaching_the_cap_early:
    reality: "Specialists hit +5 in primary stat by sessions 3-5"

    this_is_intentional: "Bounded accuracy REQUIRES capping vertical growth"

    why_it_happens:
      optimizer_path: "Attribute +2 (start) + Skill +2 (Expert) + Edge +1 = +5 total"
      timing: "Can achieve by session 3 with focused choices"
      example: "Fighter: Might +3, Combat +2 = +5 by session 3-5"

    why_this_is_good:
      bounded_accuracy: "Without cap, +8 modifiers break TN 8 (97% success = not meaningful)"
      campaign_length: "System designed for 8-12 sessions, not infinite progression"
      peak_power: "You've achieved mortal mastery - this is the goal!"

    what_to_do_after:
      philosophy: "Shift from vertical to horizontal growth"

      options:
        secondary_skills:
          effect: "Develop new capabilities"
          examples: ["Combat specialist learns Lore", "Wizard learns Athletics"]
          benefit: "Become versatile, not just powerful"

        techniques_and_abilities:
          effect: "Gain new tactical options"
          examples: ["Metamagic", "Combat techniques", "Gambits"]
          benefit: "More ways to solve problems"

        survivability:
          effect: "Increase Guard and Vitality"
          benefit: "Live long enough to use your mastery"

        edges_and_specializations:
          effect: "Narrow but deep expertise"
          examples: ["Dueling +1", "Urban Stealth +1"]
          benefit: "Excel in specific situations"

        legendary_powers:
          effect: "Gain transformative abilities at Major milestones"
          examples: ["Subsystem mastery", "Mythic edges", "Paragon paths"]
          benefit: "Transcend mortal limits in special ways"

    player_satisfaction:
      reframe: "You're not 'done' - you've graduated to mastery"
      comparison: "Like martial arts: black belt isn't the end, it's when real training begins"
      growth: "Sessions 5-12 are about becoming the complete master, not just the skilled specialist"

    examples:
      kara_the_fighter:
        session_3: "Hits +5 in Combat (Might +3, Combat +2)"
        sessions_4_9: "Learns Athletics, Command, gains 4 combat techniques, increases Guard to 23"
        session_10: "Still +5 in Combat, but now a versatile battlefield commander"
        satisfaction: "Master of combat AND tactical leader"

      aldric_the_wizard:
        session_5: "Hits +5 in Sorcery (Mind +3, Sorcery +2)"
        sessions_6_10: "Learns Lore +3, gains 6 metamagics, increases Vitality"
        session_10: "Still +5 in Sorcery, but reshapes reality with metamagic mastery"
        satisfaction: "Archmage who bends magic itself"

  power_budget:
    minor_milestone: "Worth about +0.3 to +0.5 modifier equivalent"
    moderate_milestone: "Worth about +1 modifier or significant capability"
    major_milestone: "Worth about +1 to +2 modifier plus transformative power"

    campaign_total: "Characters progress from +0 to +5 over 8-12 sessions"
    note: "Smaller per-milestone gains, but more frequent rewards maintain engagement"

# ============================================
# DOWNTIME ADVANCEMENT
# ============================================

downtime_activities:
  description: "Progress between adventures"
  time_units: "Weeks or months"
  
  training:
    description: "Improve skills"
    mechanics:
      cost: "Gold and time"
      benefit: "Progress toward next tier"
      requirement: "Trainer of higher skill"
  
  research:
    description: "Gain knowledge"
    mechanics:
      cost: "Access to library/sage"
      benefit: "Information or spell"
      requirement: "Lore or Investigation"
  
  crafting:
    description: "Create items"
    mechanics:
      cost: "Materials and time"
      benefit: "Equipment or consumables"
      requirement: "Appropriate Craft skill"
  
  networking:
    description: "Build connections"
    mechanics:
      cost: "Social investment"
      benefit: "Contacts and reputation"
      requirement: "Social skills"
  
  recovery:
    description: "Heal lasting injuries"
    mechanics:
      cost: "Time and possibly gold"
      benefit: "Remove conditions"
      requirement: "Medicine or magic"

yaml/character.yaml:
# Flow RPG Character System
# Version: 1.0-complete
# Character creation, species, archetypes, and callings

character_creation:
  process:
    step_1_attributes:
      action: "Choose starting array"
      options: ["standard", "specialized", "balanced"]
      arrays:
        standard: [2, 1, 1, 0, 0, -1]
        specialized: [3, 2, 0, 0, -1, -2]
        balanced: [1, 1, 1, 0, 0, 0]
    
    step_2_species:
      action: "Select species for attribute bonus and traits"
      options: ["human", "elf", "dwarf", "halfling"]
    
    step_3_build_type:
      action: "Choose between archetype (pre-built profession) or custom build"
      options:
        archetype:
          description: "Select a pre-built profession with defined skills, equipment, and progression path"
          choices: ["fighter", "ranger", "paladin", "rogue", "wizard", "cleric", "bard"]
        custom_build:
          description: "Build your own character with flexible skill and equipment choices"
          note: "Can later adopt archetype abilities through milestones"
    
    step_4_calling:
      action: "Select inner motivation providing Flow benefits"
      options: ["advocate", "guardian", "exemplar", "seeker", "scholar", "sentinel", "enthusiast", "champion", "mediator"]
    
    step_5_derived_values:
      calculate:
        - "Guard"
        - "Vitality"
        - "Flow starting value"
        - "Movement zones"
    
    step_6_details:
      add:
        - "Name and background"
        - "Connections to other characters"
        - "Personal goals"
        - "Equipment from archetype"

# ============================================
# SPECIES
# ============================================

species:
  design_note: "Species attribute bonuses respect the +3 attribute cap. If starting array already has +3 in an attribute, apply bonus elsewhere."

  human:
    name: "Human"
    description: "Versatile and ambitious, adapting to any challenge"

    attribute_bonus:
      choice: "any"
      amount: 1
    
    species_traits:
      versatile:
        effect: "Start with one extra skill at Novice (-1)"
        type: "character_creation"
      
      determined:
        effect: "When at negative Flow, next successful action gains +1 additional Flow"
        type: "flow_generation"
      
      adaptable:
        effect: "During any rest, may swap one Competent skill with another"
        type: "flexibility"
    
    natural_callings: "Any - humans show no pattern"
    natural_archetypes: "Any - human flexibility"
    
  elf:
    name: "Elf"
    description: "Graceful people attuned to magic and nature"
    
    attribute_bonus:
      choice: ["grace", "awareness"]
      amount: 1
    
    species_traits:
      fey_grace:
        effect: "When you roll 11+ on any check, gain +1 Flow (once per round)"
        type: "flow_generation"
      
      magical_affinity:
        effect: "Can sense magic within Near range without Sorcery skill (but need skill for details)"
        type: "perception"
      
      elven_focus:
        effect: "When casting spells, ignore the first point of armor penalty"
        type: "spellcasting"
    
    natural_callings: ["scholar", "seeker", "mediator"]
    natural_archetypes: ["wizard", "ranger", "bard"]
    
  dwarf:
    name: "Dwarf"
    description: "Sturdy mountain folk known for resilience and craftsmanship"
    
    attribute_bonus:
      choice: ["might", "will"]
      amount: 1
    
    species_traits:
      stone_endurance:
        effect: "Once per scene, reduce damage from one attack by 2 (stacks with armor)"
        type: "defense"
      
      craftwise:
        effect: "When examining worked materials, ask one question GM must answer truthfully"
        type: "information"
      
      steady_stance:
        effect: "Switching from Defensive stance costs no Flow (stubborn immovability)"
        type: "stance"
    
    natural_callings: ["sentinel", "guardian", "advocate"]
    natural_archetypes: ["fighter", "paladin", "cleric"]
    
  halfling:
    name: "Halfling"
    description: "Small, nimble folk with remarkable luck and courage"
    
    attribute_bonus:
      choice: ["will", "presence"]
      amount: 1
    
    species_traits:
      lucky:
        effect: "Once per scene, reroll any single die (keep new result)"
        type: "reroll"
      
      brave_heart:
        effect: "When an ally goes to negative Flow, immediately gain +1 Flow"
        type: "flow_generation"
      
      small_but_mighty:
        effect: "Move through enemy zones without provoking. When successfully Hide, enemies get -2 to detect"
        type: "mobility"
    
    natural_callings: ["enthusiast", "guardian", "mediator"]
    natural_archetypes: ["rogue", "bard", "cleric"]

# ============================================
# ARCHETYPES
# ============================================

archetypes:
  philosophy:
    core_concept: "Optional starting packages, not restrictive classes"

    key_principles:
      - "Archetypes are jumpstart templates, not mandatory paths"
      - "Can diverge from archetype at any milestone"
      - "Can adopt archetype features later through Custom Build"
      - "No penalties for abandoning archetype progression"
      - "Mix and match abilities through techniques.yaml"

    flexibility:
      at_creation: "Choose archetype OR custom build"
      during_play: "Every milestone offers complete freedom"
      subsystem_access: "Any character can learn any subsystem"
      no_multiclassing: "No need - all options always available"

    design_note: "This achieves the 'unicorn' of RPG design - true character freedom without multiclassing complexity"

  archetype_benefits:
    immediate:
      - "Pre-selected skills that work together"
      - "Starting equipment package"
      - "Thematic starting edge"
      - "Access to subsystem without prerequisites"

    ongoing:
      - "Suggested advancement paths (never mandatory)"
      - "Narrative framework for character"
      - "Quick character creation for new players"

  divergence_examples:
    fighter_becomes_scholar:
      starting: "Fighter with Combat Techniques"
      progression: "Takes Lore skill, learns Metamagic"
      result: "Spell blade without multiclassing"

    wizard_becomes_warrior:
      starting: "Wizard with Metamagic"
      progression: "Takes Combat skill, learns Techniques"
      result: "Battle mage through natural growth"

    custom_matches_archetype:
      starting: "Custom Build"
      progression: "Adopts Fighter techniques over time"
      result: "Effectively a Fighter, built organically"
  fighter:
    name: "Fighter"
    description: "Master of weapons and combat techniques"

    starting_skills:
      combat:
        level: "professional"
        modifier: 1
      athletics:
        level: "novice"
        modifier: -1
      command:
        level: "novice"
        modifier: -1

    archetype_feature:
      name: "Weapon Training"
      effect: "+1 to hit with all weapons"
      note: "Represents fundamental martial discipline and combat accuracy"

    starting_edge:
      choice: ["weapon_focus", "tough"]
      weapon_focus: "+1 damage with chosen weapon type"
      tough: "+2 Guard"
    
    starting_equipment:
      armor: "medium"
      weapon: "martial weapon and shield"
      gear: ["Adventurer's kit", "50 coins"]
    
    unique_subsystem:
      name: "Combat Techniques"
      description: "Start with immediate access to combat techniques"
      reference: "See techniques.yaml for full list"
      starting_access: "One basic combat technique at creation"
      progression: "Can continue learning or switch to other subsystems"
    
    natural_callings: ["champion", "guardian", "sentinel"]
    
  ranger:
    name: "Ranger"
    description: "Wilderness expert and skilled hunter"

    starting_skills:
      combat:
        level: "novice"
        modifier: -1
      survival:
        level: "professional"
        modifier: 1
      investigate:
        level: "novice"
        modifier: -1

    archetype_feature:
      name: "Weapon Training"
      effect: "+1 to hit with all weapons"
      note: "Rangers are trained combatants with excellent aim"

    starting_edge:
      choice: ["fast_movement", "precise_strike"]
      fast_movement: "+1 zone of movement"
      precise_strike: "Reroll one damage die per attack"
    
    starting_equipment:
      armor: "light"
      weapon: "bow and hunting knife"
      gear: ["Tracking kit", "Camping gear", "30 coins"]
    
    unique_subsystem:
      name: "Favored Terrain"
      description: "Gain bonuses in specific environments"
      progression: "Add new terrains at milestones"
    
    natural_callings: ["seeker", "scholar", "sentinel"]
    
  paladin:
    name: "Paladin"
    description: "Divine warrior and inspiring leader"

    starting_skills:
      combat:
        level: "novice"
        modifier: -1
      medicine:
        level: "novice"
        modifier: -1
      command:
        level: "professional"
        modifier: 1

    archetype_feature:
      name: "Divine Grace"
      effect: "+1 to all saving rolls, +4 Guard, start each scene at +1 Flow"
      note: "Divine protection shields from harm, strengthens resolve, and provides blessed energy"

    spellcasting:
      tradition: "divine"
      access: "Can cast divine spells regardless of attributes"
      focus: "Protection and smiting"
    
    starting_equipment:
      armor: "heavy"
      weapon: "weapon and holy symbol"
      gear: ["Healing kit", "Religious texts", "40 coins"]
    
    unique_subsystem:
      name: "Divine Oath"
      description: "Sworn oath provides power and restrictions"
      progression: "Oath evolves with major milestones"
    
    natural_callings: ["advocate", "guardian", "champion"]
    
  rogue:
    name: "Rogue"
    description: "Skilled infiltrator and versatile expert"

    starting_skills:
      stealth:
        level: "professional"
        modifier: 1
      finesse:
        level: "professional"
        modifier: 1
      deceive:
        level: "novice"
        modifier: -1

    archetype_feature:
      name: "Dual Expertise"
      effect: "Two Professional skills instead of one"
      note: "Rogues' defining trait - extreme skill specialization"
    
    starting_equipment:
      armor: "light"
      weapon: "daggers and shortbow"
      gear: ["Thieves' tools", "Disguise kit", "60 coins"]
    
    unique_subsystem:
      name: "Gambits"
      description: "High-risk, high-reward special actions"
      progression: "Unlock new gambits through heists"
    
    natural_callings: ["seeker", "enthusiast", "scholar"]
    
  wizard:
    name: "Wizard"
    description: "Master of arcane knowledge and magical theory"

    starting_skills:
      sorcery:
        level: "professional"
        modifier: 1
      lore:
        level: "professional"
        modifier: 1
      investigate:
        level: "novice"
        modifier: -1

    archetype_feature:
      name: "Arcane Battery"
      effect: "Maximum Flow increased to +7, start each scene at +2 Flow"
      note: "Greater magical reserves and charged energy allow casting powerful spells immediately"

    spellcasting:
      tradition: "arcane"
      access: "Can cast arcane spells regardless of attributes"
      focus: "Versatility and power"
    
    starting_equipment:
      armor: "none"
      weapon: "staff or wand"
      gear: ["Spellbook", "Component pouch", "Scholarly tools", "30 coins"]
    
    unique_subsystem:
      name: "Metamagic"
      description: "Start with immediate access to metamagic"
      reference: "See techniques.yaml for full list"
      starting_access: "One basic metamagic at creation"
      progression: "Can continue learning or explore other subsystems"
    
    natural_callings: ["scholar", "seeker", "advocate"]
    
  cleric:
    name: "Cleric"
    description: "Channel of divine power and spiritual healer"

    starting_skills:
      medicine:
        level: "professional"
        modifier: 1
      sorcery:
        level: "novice"
        modifier: -1
      empathy:
        level: "professional"
        modifier: 1

    archetype_feature:
      name: "Divine Grace"
      effect: "+1 to all saving rolls, +4 Guard, start each scene at +1 Flow"
      note: "Divine protection shields from harm, strengthens resolve, and provides blessed energy"

    spellcasting:
      tradition: "divine"
      access: "Can cast divine spells regardless of attributes"
      focus: "Healing and support"
    
    starting_equipment:
      armor: "medium"
      weapon: "mace and holy symbol"
      gear: ["Healer's kit", "Holy water", "Religious garments", "35 coins"]
    
    unique_subsystem:
      name: "Divine Domain"
      description: "Deity grants specialized powers"
      progression: "Domain powers expand at milestones"
    
    natural_callings: ["guardian", "mediator", "advocate"]
    
  bard:
    name: "Bard"
    description: "Performer, storyteller, and magical artist"

    starting_skills:
      perform:
        level: "professional"
        modifier: 1
      deceive:
        level: "novice"
        modifier: -1
      sorcery:
        level: "novice"
        modifier: -1

    archetype_feature:
      name: "Versatile Experience"
      effect: "One additional Novice skill of your choice, +4 Guard, start each scene at +1 Flow"
      note: "Bards learn from their travels, magical performance builds resilience and energy"

    spellcasting:
      tradition: "performance"
      access: "Can cast performance magic regardless of attributes"
      focus: "Inspiration and manipulation"
    
    starting_equipment:
      armor: "light"
      weapon: "rapier and dagger"
      gear: ["Musical instrument", "Costume", "Bardic lore collection", "45 coins"]
    
    unique_subsystem:
      name: "Bardic Inspiration"
      description: "Grant allies bonus dice through performance"
      progression: "Inspiration die size increases with milestones"
    
    natural_callings: ["enthusiast", "mediator", "seeker"]

# ============================================
# CUSTOM BUILD
# ============================================

custom_build:
  name: "Custom Build"
  description: "Superior flexibility and customization for experienced players"

  starting_skills:
    selection: "Choose 4 skills (more than any archetype!)"
    distribution:
      competent:
        number: 1
        modifier: 0
        note: "Your primary skill focus"
      novice:
        number: 3
        modifier: -1
        note: "Broader base than archetypes"
    restrictions: "No skill may start above Competent (0)"
    advantage: "Start with 4 skills vs archetype's 3"

  starting_edges:
    selection: "Choose TWO from universal list (double archetype bonus!)"
    universal_edges:
      tough:
        effect: "+2 Guard"
        description: "Natural resilience"

      quick:
        effect: "+1 zone of movement"
        description: "Fast on your feet"

      alert:
        effect: "+1 to initiative rolls"
        description: "Always ready"

      versatile:
        effect: "One additional Novice skill"
        description: "Broad experience"

      focused:
        effect: "+1 to rolls with your Competent skill"
        description: "Specialized training"

      connected:
        effect: "Start with helpful NPC contact"
        description: "Social network"

      wealthy:
        effect: "Double starting coins (200 total)"
        description: "Family resources or past success"

      talented:
        effect: "Choose one skill to advance faster (half milestone cost)"
        description: "Natural aptitude"

  starting_equipment:
    budget: 150
    note: "50% more than most archetypes!"
    suggestions:
      combat_focused:
        - "Medium armor (40 coins)"
        - "Martial weapon (20 coins)"
        - "Shield (10 coins)"
        - "Adventurer's kit (30 coins)"

      skill_focused:
        - "Light armor (20 coins)"
        - "Simple weapon (10 coins)"
        - "Professional tools (30 coins)"
        - "Adventurer's kit (30 coins)"
        - "10 coins remaining"

      magic_focused:
        - "No armor (0 coins)"
        - "Focus item (20 coins)"
        - "Component pouch (20 coins)"
        - "Scholarly tools (30 coins)"
        - "Adventurer's kit (30 coins)"

  progression:
    flexibility: "Complete freedom in milestone choices"

    subsystem_access:
      description: "Can learn any archetype subsystem through milestones"
      requirement: "Narrative justification and/or training"
      examples:
        - "Learn Combat Techniques from Fighter mentor"
        - "Develop Metamagic through magical research"
        - "Gain Bardic Inspiration by studying performance"
        - "Acquire Divine Oath through religious dedication"

    magic_access:
      description: "Can gain spellcasting if meeting requirements"
      options:
        attribute_based: "Meet tradition requirements (see magic_access)"
        milestone_based: "Spend moderate milestone to gain Sorcery skill"
        training_based: "Learn from mentor with proper narrative"

    archetype_adoption:
      description: "Can fully adopt an archetype at Moderate Milestone"
      effect: "Gain archetype's unique subsystem and progression options"
      restriction: "Must meet narrative requirements"
      note: "Keeps all previously gained abilities"

# ============================================
# CALLINGS
# ============================================

callings:
  advocate:
    name: "The Advocate"
    core_drive: "The world must be made right"
    fear: "Being corrupt, defective, or wrong"
    desire: "To be good, right, accurate, and virtuous"
    
    flow_benefit:
      name: "Righteous Revelation"
      trigger: "When you or ally reveals truth or exposes deception"
      effect: "Gain +1 Flow"
      limit: "No limit per scene"
    
    narrative_permission:
      name: "Truth Sense"
      effect: "Always know when someone is lying about wrongdoing or corruption"
      requirement: "No roll needed"
    
    stress_behavior: "Becomes critical and perfectionist"
    growth_direction: "Learns to accept imperfection"
    
    calling_equipment:
      item: "Seal of Truth"
      effect: "Once per scene, force someone to answer honestly"
    
  guardian:
    name: "The Guardian"
    core_drive: "I exist to help others"
    fear: "Being unloved or unwanted"
    desire: "To feel loved and needed by others"
    
    flow_benefit:
      name: "Protective Surge"
      trigger: "When you successfully defend or heal an ally"
      effect: "Gain +1 Flow"
      limit: "Twice per scene"
    
    narrative_permission:
      name: "Helper's Intuition"
      effect: "Always know when someone genuinely needs help, even if hiding it"
      requirement: "No roll needed"
    
    stress_behavior: "Becomes possessive and martyrlike"
    growth_direction: "Learns healthy boundaries"
    
    calling_equipment:
      item: "Guardian's Token"
      effect: "Can take damage meant for another at any range once per scene"
    
  exemplar:
    name: "The Exemplar"
    core_drive: "Success proves my worth"
    fear: "Being worthless without achievements"
    desire: "To feel valuable and worthwhile"
    
    flow_benefit:
      name: "Victory Rush"
      trigger: "Any critical success (13+)"
      effect: "Gain +1 additional Flow beyond normal critical"
      limit: "No limit"
    
    narrative_permission:
      name: "Victory Sense"
      effect: "Instinctively know the 'win condition' of any situation"
      requirement: "No roll needed"
    
    stress_behavior: "Becomes ruthlessly competitive"
    growth_direction: "Learns intrinsic worth"
    
    calling_equipment:
      item: "Trophy of Excellence"
      effect: "Reroll one failed roll per scene"
    
  seeker:
    name: "The Seeker"
    core_drive: "I must find my true self"
    fear: "Having no identity or significance"
    desire: "To find themselves and their significance"
    
    flow_benefit:
      name: "Authentic Insight"
      trigger: "When you discover something important about yourself or others"
      effect: "Gain +2 Flow"
      limit: "Twice per scene"
    
    narrative_permission:
      name: "Soul Reading"
      effect: "Once per scene, ask deep personal question that must be answered honestly"
      requirement: "Target may be cryptic"
    
    stress_behavior: "Becomes self-absorbed and melancholic"
    growth_direction: "Learns to connect authentically"
    
    calling_equipment:
      item: "Mirror of Truth"
      effect: "See through any disguise or illusion once per scene"
    
  scholar:
    name: "The Scholar"
    core_drive: "Knowledge reveals truth"
    fear: "Being incompetent or overwhelmed"
    desire: "To be capable and understanding"
    
    flow_benefit:
      name: "Prepared Mind"
      trigger: "When you apply knowledge to solve a problem"
      effect: "Gain +1 Flow"
      limit: "Three times per scene"
    
    narrative_permission:
      name: "Contingency Planning"
      effect: "Once per scene, declare you prepared for this exact situation"
      requirement: "Produce relevant tool, fact, or preparation"
    
    stress_behavior: "Becomes detached and nihilistic"
    growth_direction: "Learns to engage emotionally"
    
    calling_equipment:
      item: "Scholar's Codex"
      effect: "Ask GM one question about any topic, receive useful answer"
    
  sentinel:
    name: "The Sentinel"
    core_drive: "Loyalty and vigilance keep us safe"
    fear: "Being without support or security"
    desire: "To have security and support"
    
    flow_benefit:
      name: "Defensive Vigilance"
      trigger: "When you spot danger before it strikes"
      effect: "Gain +1 Flow"
      limit: "Twice per scene"
    
    narrative_permission:
      name: "Danger Sense"
      effect: "Cannot be surprised or ambushed, always act in first round"
      requirement: "Even if caught off-guard"
    
    stress_behavior: "Becomes paranoid and reactive"
    growth_direction: "Learns to trust"
    
    calling_equipment:
      item: "Sentinel's Ward"
      effect: "+2 Guard against first attack each scene"
    
  enthusiast:
    name: "The Enthusiast"
    core_drive: "Life is an adventure to experience"
    fear: "Being trapped in pain or deprivation"
    desire: "To be satisfied and content"
    
    flow_benefit:
      name: "Joyful Flow"
      trigger: "When you gain Flow from any source"
      effect: "Adjacent ally also gains +1 Flow"
      limit: "No limit"
    
    narrative_permission:
      name: "Silver Lining"
      effect: "Always find something positive/useful in any situation"
      requirement: "Provides actual mechanical or narrative benefit"
    
    stress_behavior: "Becomes manic and scattered"
    growth_direction: "Learns to face difficulty"
    
    calling_equipment:
      item: "Lucky Charm"
      effect: "Turn one failure into partial success per scene"
    
  champion:
    name: "The Champion"
    core_drive: "Strength protects what matters"
    fear: "Being controlled, vulnerable, or weak"
    desire: "To be self-reliant and in control"
    
    flow_benefit:
      name: "Protective Dominance"
      trigger: "When you defeat or intimidate an enemy threatening allies"
      effect: "Gain +1 Flow"
      limit: "Twice per scene"
    
    narrative_permission:
      name: "Unshakeable Will"
      effect: "Intimidation attempts against you automatically fail"
      requirement: "Project strength that cannot be undermined"
    
    stress_behavior: "Becomes domineering and aggressive"
    growth_direction: "Learns vulnerability is strength"
    
    calling_equipment:
      item: "Champion's Banner"
      effect: "Allies in same zone gain +1 damage"
    
  mediator:
    name: "The Mediator"
    core_drive: "Harmony brings peace to all"
    fear: "Loss of connection, separation, conflict"
    desire: "To have inner and outer peace"
    
    flow_benefit:
      name: "Harmony Restoration"
      trigger: "First time each scene you help resolve any conflict"
      effect: "You and all involved gain +1 Flow"
      limit: "Once per scene"
    
    narrative_permission:
      name: "Universal Understanding"
      effect: "Understand basic meaning/emotion of any communication"
      requirement: "Regardless of language barriers"
    
    stress_behavior: "Becomes passive and avoidant"
    growth_direction: "Learns healthy conflict"
    
    calling_equipment:
      item: "Peace Bond"
      effect: "Prevent one act of violence per scene through mystical compulsion"

# ============================================
# DERIVED VALUES
# ============================================

derived_values:
  guard:
    formula: "12 + max(might, grace, will)"
    description: "Ablative defense, refreshes between scenes"
    recovery:
      between_scenes: "Full restoration"
      rally_action: "1d6 once per scene"
    progression: "Increased through milestone choices, not automatically"
    design_note: "Base 12 + highest attribute ensures all builds have survivability. Will inclusion helps casters use mental fortitude for defense."

  vitality:
    formula: "10 + will"
    description: "Core health, serious injury threshold"
    recovery:
      natural: "1 per hour of rest"
      magical: "Varies by spell"
    progression: "Increased through milestone choices, not automatically"
  
  flow:
    starting: 0
    range: [-3, 6]
    reset: "Between scenes"
  
  movement:
    base_zones_per_turn: 1
    modifiers:
      no_armor: 2
      fast_movement_edge: "+1"
      halfling_size: "Can move through enemies"
    double_move: "2 zones if no other action"
  
  initiative:
    determination: "By stance"
    order:
      1: "Aggressive"
      2: "Balanced"
      3: "Defensive"
    tiebreaker: "Highest Grace, then players before NPCs"
  
  carrying_capacity:
    light_load: "might + 5 items"
    medium_load: "might + 10 items (encumbered)"
    heavy_load: "might + 15 items (heavily encumbered)"

# ============================================
# CALLING EVOLUTION
# ============================================

calling_evolution:
  minor_milestone:
    options:
      - "Deepen understanding of current calling"
      - "Gain minor related benefit (GM discretion)"
      - "Explore calling through roleplay"
  
  moderate_milestone:
    options:
      - "Evolve interpretation of calling"
      - "Modify Flow benefit trigger slightly"
      - "Add minor secondary benefit"
  
  major_milestone:
    transformation:
      description: "Complete calling change or synthesis"
      requirements:
        - "Extensive roleplay groundwork"
        - "Major narrative turning point"
        - "Table agreement"
      
      options:
        single_calling_evolution:
          description: "Calling transforms to adjacent type"
          example: "Guardian → Advocate (protecting individuals → fighting systemic injustice)"
        
        calling_synthesis:
          description: "Merge two callings into unique hybrid"
          example: "Guardian + Scholar = Battle Medic (protection through preparation)"
          benefit: "Keep both Flow benefits at 75% effectiveness"
        
        calling_transcendence:
          description: "Rise above calling limitations"
          effect: "Lose calling benefits, gain +1 to all attributes (respecting +3 cap)"
          narrative: "Achieved perfect balance"
          note: "Excellent for generalists, brings all attributes closer to peak"

# ============================================
# MAGIC ACCESS
# ============================================

magic_access:
  universal_rule:
    statement: "If archetype provides Sorcery skill, can cast regardless of attributes"
    affected_archetypes: ["wizard", "cleric", "paladin", "bard"]
  
  alternative_access:
    arcane_tradition:
      requirement: "mind + awareness >= 2"
      description: "Academic magical study"
      spell_types: ["Arcane", "Ritual", "Metamagic"]
    
    divine_tradition:
      requirement: "will + presence >= 2"
      description: "Faith-based channeling"
      spell_types: ["Divine", "Healing", "Smiting"]
    
    primal_tradition:
      requirement: "awareness + will >= 2"
      description: "Natural world attunement"
      spell_types: ["Nature", "Elemental", "Shapeshifting"]
    
    performance_tradition:
      requirement: "presence + grace >= 2"
      description: "Magic through artistic expression"
      spell_types: ["Enchantment", "Illusion", "Inspiration"]

yaml/combat.yaml:
# Flow RPG Combat System
# Version: 1.0-complete
# Combat mechanics, stances, techniques, and health

combat_system:
  overview:
    typical_length: "3-5 rounds"
    turn_structure: "Stance-based initiative"
    flow_importance: "Central to all combat actions"
    zones: "Abstract positioning system"

# ============================================
# STANCES
# ============================================

stances:
  aggressive:
    name: "Aggressive Stance"
    philosophy: "Strike first, strike hard"
    when_to_use: "When you need to end fights quickly, press tactical advantage, or seize initiative"

    turn_order: 1

    flow_generation:
      successful_attack: 1
      note: "Removed charging bonus for balance"

    modifiers:
      damage_bonus: 1
      defense_penalty: -1

    movement:
      requirement: "Must move toward nearest enemy if able"
      charge:
        description: "Move 2+ zones and attack"
        bonus: "+2 damage"

    special_ability:
      name: "Overwhelming Assault"
      effect: "Critical hits generate +1 additional Flow"

    tactical_notes: "High risk, high reward - generates Flow through decisive action"

    restrictions:
      heavy_armor: "None - all armor types can use aggressive stance"
  
  balanced:
    name: "Balanced Stance"
    philosophy: "Adapt and overcome"
    when_to_use: "When facing unpredictable threats, maintaining flexibility, or learning enemy capabilities"

    turn_order: 2

    flow_generation:
      excellence:
        trigger: "Any roll of 10+ (natural, before modifiers)"
        amount: 1
        note: "Rewards solid rolls, about 42% chance"
    
    modifiers:
      damage_bonus: 0
      defense_bonus: 0
    
    movement:
      freedom: "Complete movement choice"
      flexibility: "No restrictions or requirements"
    
    special_ability:
      name: "Tactical Flexibility"
      effect: "Once per combat, switch stance as free action"

    tactical_notes: "Rewards skill and adaptability - no bonuses or penalties, but generates Flow from excellence and can adjust to changing battlefield conditions"

    advantages:
      - "Most versatile option"
      - "No penalties"
      - "Good for uncertain situations"
  
  defensive:
    name: "Defensive Stance"
    philosophy: "Patience and protection"
    when_to_use: "When threatened, protecting allies, buying time for preparation, or facing overwhelming offense"

    turn_order: 3
    
    flow_generation:
      being_attacked:
        trigger: "Targeted by attack"
        amount: 1
        limit: "Once per round total (not per attacker)"
        note: "First time you're attacked each round, gain +1 Flow regardless of how many attackers"
      successful_defense:
        trigger: "Successfully defend"
        amount: 1
        limit: "No limit"
    
    modifiers:
      damage_penalty: -1
      defense_bonus: 4
      damage_reduction: 2
    
    movement:
      disengage: "Can leave engagement without provoking"
      retreat: "Free movement away from enemies"
    
    special_ability:
      name: "Perfect Counter"
      effect: "On critical defense success, make free counterattack"

    tactical_notes: "Generates Flow reliably through being targeted - turns enemy aggression into resource advantage while protecting yourself and allies"

stance_interactions:
  switching:
    cost: 0
    action_type: "Free action at turn start"
    limit: "Once per turn normally"
    exception: "Balanced stance can switch mid-combat once"
  
  stance_dancing:
    description: "Advanced technique of switching stances tactically"
    requirements: "Moderate milestone technique"
    benefit: "Switch stance as reaction for 1 Flow"
  
  team_tactics:
    formation_fighting:
      requirement: "All allies in same stance"
      benefit: "+1 to all rolls"
    
    complementary_stances:
      aggressive_defensive: "Aggressive draws attacks, Defensive generates Flow"
      balanced_support: "Balanced switches to fill gaps"

# ============================================
# ZONES AND MOVEMENT
# ============================================

zones:
  ranges:
    engaged:
      distance: "0 - Wrestling/sword range"
      description: "In direct combat with specific opponents"
      weapon_use:
        melee: "Normal"
        thrown: "-2 penalty"
        ranged: "Cannot use"
      movement: "Cannot move past enemies without special ability"
    
    close:
      distance: "1 - Across a room (30 feet)"
      description: "Throwing range, near combat"
      weapon_use:
        melee: "Cannot attack"
        thrown: "+1 Flow on hit"
        ranged: "Normal"
      movement: "Can engage or stay at range"
    
    far:
      distance: "2 - Across a hall (60 feet)"
      description: "Bow range, safe from melee"
      weapon_use:
        melee: "Cannot attack"
        thrown: "Cannot reach"
        ranged: "+1 damage"
      movement: "Must move twice to engage"
    
    extreme:
      distance: "3+ - Shouting distance (120+ feet)"
      description: "Beyond normal combat"
      weapon_use:
        melee: "Cannot affect"
        thrown: "Cannot affect"
        ranged: "-2 to hit"
      movement: "Effectively out of combat"
  
  movement_rules:
    standard: 
      zones_per_turn: 1
      action_cost: "Move action"
    
    double_move:
      zones_per_turn: 2
      action_cost: "Full turn"
      restriction: "No other actions"
    
    modifiers:
      no_armor: "+1 zone per turn"
      fast_movement_edge: "+1 zone per turn"
      difficult_terrain: "-1 zone per turn"
      halfling: "Move through enemy zones"
  
  zone_control:
    blocking:
      description: "Enemies cannot move past you"
      exception: "Special abilities or size difference"
    
    overwatch:
      description: "Threaten area with ranged weapon"
      effect: "Free attack if enemy enters"
      cost: "Ready action"

# ============================================
# HEALTH AND DAMAGE
# ============================================

health_system:
  guard:
    formula: "12 + max(might, grace, will)"

    function:
      - "Ablative defense layer"
      - "Represents dodging, armor, luck, and mental fortitude"
      - "First to take damage"

    design_note: "Will added to formula allows casters to use mental fortitude for defense"

    recovery:
      between_scenes: "Full restoration"
      rally_action:
        effect: "Recover 1d6 Guard"
        limit: "Once per scene"
        action_cost: "Full action"

    progression:
      method: "Through milestone choices, not automatic"
      options: "See advancement.yaml for Guard increase options"

    design_note: "Base 12 + attribute ensures 2-3 hit survivability. Will inclusion gives casters 15+ Guard."

    armor_bonus:
      medium_armor: "+2 Guard at scene start"
      special_abilities: "Various edges grant +2"
  
  vitality:
    formula: "10 + will"

    function:
      - "Core health"
      - "Serious injury threshold"
      - "Death trigger at 0"

    recovery:
      natural: "1 per hour of rest"
      medical: "Medicine check restores 1d6"
      magical: "Varies by spell level"

    progression:
      method: "Through milestone choices, not automatic"
      options: "See advancement.yaml for Vitality increase options"
    
    damage_consequences:
      half_vitality: "Visible injuries"
      zero_vitality: "Unconscious and dying"
      negative_vitality: "Death saves required"

damage_resolution:
  order:
    1: "Roll damage dice"
    2: "Add modifiers (attribute, milestone bonus, etc.)"
    3: "Subtract armor damage reduction"
    4: "Apply to Guard first"
    5: "Excess damage goes to Vitality"
    6: "Check for death/dying if Vitality = 0"
  
  damage_scaling:
    philosophy: "Damage increases through choices, not automatically"

    options:
      weapon_focus: "Minor milestone: +1 damage with weapon type"
      improved_casting: "Moderate milestone: +1d6 spell damage"
      legendary_strike: "Major milestone: Critical on 11+ with chosen weapon"

    note: "See advancement.yaml for specific damage improvement options"
  
  damage_types:
    physical:
      description: "Normal weapon damage"
      reduction: "Armor applies fully"

    elemental:
      description: "Fire, cold, lightning, etc."
      reduction: "Armor applies half"
      special: "May have ongoing effects"

    psychic:
      description: "Mental damage"
      reduction: "Armor doesn't apply"
      defense: "Will-based resistance"

    true:
      description: "Cannot be reduced"
      reduction: "Nothing applies"
      rarity: "Very rare, high-level only"

  critical_hits:
    trigger: "Attack roll meets or exceeds critical threshold"
    threshold: "13 + (total_modifier ÷ 3, rounded down)"

    effect_in_combat:
      damage: "Roll damage normally, then add +1d6 bonus damage"
      flow: "+1 Flow as normal for critical success"
      narrative: "Describe exceptional impact"

    important_note: "Critical hits do NOT double damage dice"

    design_rationale:
      reason: "Prevents one-shot kills while keeping crits special"
      math: "At +5 cap, crits add 3.5 average bonus (not doubling 10+ damage)"
      balance: "Single crit won't drop a PC from full to death"

    examples:
      longsword_crit:
        normal_damage: "2d6+3 (average 10)"
        critical_damage: "2d6+3 + 1d6 (average 13.5)"
        note: "+3.5 bonus, not double to 20"

      fireball_crit:
        normal_damage: "2d6+2 (average 9)"
        critical_damage: "2d6+2 + 1d6 (average 12.5)"
        note: "Spells also add +1d6, not double"

    special_abilities:
      sneak_attack_interaction:
        rule: "Sneak Attack dice are NOT added to crit bonus"
        example: "2d6+2 (weapon) + 2d6 (sneak) + 1d6 (crit) = 5d6+2"
        note: "See techniques.yaml for full Sneak Attack rules"

      critical_techniques:
        some_abilities: "May have special crit interactions"
        reference: "See individual technique descriptions"

death_and_dying:
  unconscious:
    trigger: "Vitality reaches 0"
    effect: "Fall unconscious, begin dying"
    duration: "Until stabilized or dead"
  
  death_saves:
    roll: "2d6 + Will"
    timing: "Start of each turn while dying"

    results:
      5_or_less:
        effect: "Lose 1 Vitality"
        description: "Getting worse"

      6_to_7:
        effect: "Stable this round"
        description: "Holding on"

      8_to_10:
        effect: "Stabilize at 0 Vitality"
        description: "Unconscious but stable"

      11_plus:
        effect: "Conscious at 1 Vitality"
        description: "Heroic recovery"

    design_note: "Will modifier makes death saves less random"

    success_rate_examples:
      will_0:
        modifier: "+0"
        stabilize_8_plus: "42% chance per round"
        survive_one_round: "72% chance (6+ keeps you alive)"

      will_2:
        modifier: "+2"
        stabilize_8_plus: "58% chance per round"
        survive_one_round: "83% chance"
        note: "Typical cleric/paladin - very resilient"

      will_5:
        modifier: "+5"
        stabilize_8_plus: "91% chance per round"
        survive_one_round: "97% chance"
        note: "Late campaign - death saves are reliable"

    practical_guidance:
      low_will: "Around 50/50 to stabilize each round - allies should help!"
      mid_will: "Likely to stabilize in 1-2 rounds on your own"
      high_will: "Very hard to kill - will probably stabilize"

  death:
    trigger: "Vitality reaches -3"
    effect: "Character dies"
    prevention: "Stabilization or healing"
  
  stabilization:
    medicine_check: 
      tn: 8
      effect: "Stop dying process"
    
    magical_healing:
      effect: "Any healing stabilizes and restores Vitality"
    
    first_aid:
      description: "Narrative stabilization"
      gm_discretion: true

# ============================================
# ARMOR SYSTEM
# ============================================

armor:
  none:
    damage_reduction: 0
    penalties:
      grace: 0
      flow: "None"
    benefits:
      flow_generation: "+1 when taking damage"
      spellcasting: "+1 to Sorcery checks"
      movement: "+1 zone per turn"
    description: "Maximum mobility and magical attunement"
  
  light:
    damage_reduction: 1
    penalties:
      grace: 0
      flow: "None"
      spellcasting: 0
    benefits:
      initiative: "+1 to act sooner in stance"
      stealth: "No penalty to Stealth"
    description: "Balance of protection and mobility"
    examples: ["Leather", "Padded", "Hide"]
  
  medium:
    damage_reduction: 2
    penalties:
      grace: -1
      flow: "None"
      spellcasting: 0
    benefits:
      guard: "+2 Guard at scene start"
      balance: "No stance restrictions"
    description: "Versatile protection"
    examples: ["Chain shirt", "Scale mail", "Breastplate"]
  
  heavy:
    damage_reduction: 4
    penalties:
      grace: -2
      flow: "None"
      spellcasting: -2
      movement: "Maximum 1 zone per turn (cannot be increased by edges)"
    benefits:
      knockback_immunity: "Cannot be moved by attacks"
      damage_reduction: "Highest protection (DR 4)"
    description: "Maximum protection at significant mobility cost"
    examples: ["Full plate", "Splint mail"]
    design_note: "DR 4 means average attack (7 damage) still deals 3 damage"
  
  shields:
    buckler:
      guard_bonus: 1
      special: "Can use with two-handed weapons"
    
    standard:
      guard_bonus: 2
      special: "Standard defensive tool"
    
    tower:
      guard_bonus: 3
      special: "Provides cover, -1 to attacks"

# ============================================
# WEAPONS
# ============================================

weapons:
  categories:
    light:
      damage: "2d6"
      attributes: ["grace", "might"]
      special: "+1 to Finesse actions"
      examples: ["Dagger", "Shortsword", "Rapier"]
    
    medium:
      damage: "2d6+1"
      attributes: ["might", "grace"]
      special: "Balanced, no special rules"
      examples: ["Longsword", "Mace", "Spear"]
    
    heavy:
      damage: "2d6+2"
      attributes: ["might"]
      special: "-1 Grace while wielding"
      examples: ["Greatsword", "Maul", "Greataxe"]
    
    reach:
      damage: "2d6"
      attributes: ["might", "grace"]
      special: "Attack from Close range"
      examples: ["Pike", "Halberd", "Whip"]
    
    thrown:
      damage: "2d6"
      range: "Close"
      special: "+1 Flow at Close range"
      examples: ["Javelin", "Throwing axe", "Dagger"]
    
    ranged:
      damage: "2d6"
      range: "Far"
      special: "+1 damage at Far, -2 when Engaged"
      examples: ["Bow", "Crossbow", "Sling"]
  
  weapon_properties:
    versatile:
      description: "Use one or two-handed"
      effect: "+1 damage when two-handed"
    
    finesse:
      description: "Use Grace instead of Might"
      effect: "Choice of attribute"
    
    loading:
      description: "Requires action to reload"
      effect: "Every other turn firing"
    
    ammunition:
      description: "Requires arrows/bolts"
      effect: "Track ammo (optional)"
  
  quality_levels:
    standard:
      bonus: 0
      cost: "Base price"
    
    fine:
      bonus: "+1 to hit OR damage"
      cost: "×5 price"
    
    masterwork:
      bonus: "+1 to hit AND damage"
      cost: "×10 price"
    
    legendary:
      bonus: "+2 to hit and damage, special property"
      cost: "Priceless"

# ============================================
# COMBAT ACTIONS
# ============================================

combat_actions:
  basic_actions:
    attack:
      roll: "2d6 + attribute + combat"
      typical: 
        melee: "might + combat"
        ranged: "grace + combat"
      target: "TN 8 normally"
      success: "Roll damage"
    
    defend:
      roll: "2d6 + grace + combat"
      effect: "+2 Guard until next turn"
      critical: "Gain +1 Flow"
    
    maneuver:
      roll: "2d6 + attribute + skill"
      examples:
        - "Reposition for advantage"
        - "Create environmental hazard"
        - "Disarm opponent"
      success: "Situational benefit + possible Flow"
    
    rally:
      effect: "Recover 1d6 Guard"
      limit: "Once per scene"
      action: "Full action, no roll"
    
    move:
      effect: "Change position by 1 zone"
      combine: "Can move and take another action"
  
  reactions:
    counter:
      trigger: "Attacked in Defensive stance"
      cost: "1 Flow"
      roll: "Opposed combat check"
      success: "Negate attack, possibly counter"
    
    interpose:
      trigger: "Adjacent ally attacked"
      cost: "1 Flow"
      effect: "Become target instead"
      requirement: "Defensive stance"
    
    opportunity_attack:
      trigger: "Enemy leaves engagement"
      requirement: "Ready action or special ability"
      effect: "Free attack at -2"
  
  full_actions:
    charge:
      requirement: "Aggressive stance"
      effect: "Move 2 zones + attack with +2 damage"
      flow: "+2 Flow if successful"
    
    full_defense:
      effect: "+4 to defense, +2 Guard"
      duration: "Until next turn"
      limit: "No other actions"
    
    aim:
      effect: "+2 to next ranged attack"
      requirement: "Don't move"

# ============================================
# COMBAT TECHNIQUES
# ============================================

combat_techniques:
  acquisition:
    philosophy: "No attribute gates - anyone can learn"
    method: "Milestone advancement"
    training: "Narrative justification helpful"
  
  basic_techniques:
    available_to: "Anyone"
    no_flow_cost:
      - "Strike (standard attack)"
      - "Defend (increase Guard)"
      - "Maneuver (tactical advantage)"
      - "Rally (recover Guard)"
  
  minor_milestone_techniques:
    requirement: "1+ minor milestones"
    
    riposte:
      trigger: "After successful Defend"
      effect: "Immediately Strike"
      cost: "1 Flow"
    
    press_advantage:
      trigger: "While Flow positive"
      effect: "+1d6 damage"
      cost: "Passive while condition met"
    
    defensive_mastery:
      effect: "Defensive stance grants +3 defense"
      cost: "Passive improvement"
    
    quick_recovery:
      effect: "Regain 1d6 Guard between rounds"
      cost: "1 Flow"
      limit: "Once per combat"
  
  moderate_milestone_techniques:
    requirement: "Flow +3 to activate"
    
    whirlwind_strike:
      effect: "Hit all adjacent enemies"
      cost: "3 Flow"
      damage: "Normal weapon damage to each"
    
    perfect_parry:
      effect: "Negate all damage from one source"
      cost: "2 Flow"
      timing: "Reaction"
    
    devastating_blow:
      effect: "Double damage dice"
      cost: "3 Flow"
      limit: "Once per scene"
    
    combat_flow:
      effect: "Extra Flow on any critical"
      cost: "Passive once learned"
  
  major_milestone_techniques:
    requirement: "Flow +6 to activate"
    
    unstoppable_assault:
      effect: "Next attack cannot miss"
      cost: "6 Flow"
      damage: "Maximum damage"
    
    death_blow:
      effect: "Instant kill if target below 50% Vitality"
      cost: "6 Flow"
      save: "Will TN 12 to reduce to normal damage"
    
    battlefield_control:
      effect: "Reposition all combatants"
      cost: "6 Flow"
      limit: "Once per scene"

# ============================================
# SIGNATURE MOVES
# ============================================

signature_moves:
  description: "Personalized techniques that define your fighting style"
  philosophy: "Earned power that represents mastery and personal style"

  creation:
    when: "Moderate milestone"
    timing_note: "Awarded at session 4 typically, when character identity is established"
    components:
      - "Name (personal to character)"
      - "Mechanical effect (based on existing technique)"
      - "Flow cost (1 less than normal technique, minimum 0)"
      - "Narrative description (how it looks and feels)"

    creation_guidelines:
      base_technique: "Choose any technique you know as foundation"
      discount: "Costs 1 Flow less than normal (minimum 0)"
      restrictions: "Must have used the base technique successfully in play"
      balance: "Should feel earned through character development"

    examples:
      riposte_signature:
        base: "Riposte (normally 1 Flow)"
        signature_cost: 0
        name: "Example: 'Viper's Response'"
        requirement: "Must have successfully used Riposte at least twice"

      press_advantage_signature:
        base: "Press Advantage (normally passive at Flow +2)"
        signature_version: "Activates at Flow +1 instead"
        name: "Example: 'Relentless Assault'"
        requirement: "Must have maintained Flow +2 in multiple combats"
  
  examples:
    fighter_magnus:
      name: "Thunder Strike"
      effect: "Attack all enemies in zone"
      normal_cost: 3
      signature_cost: 2
      description: "Spins weapon in devastating arc"
    
    wizard_aldric:
      name: "Arcane Eruption"
      effect: "3d6 force damage in Close range"
      normal_cost: 2
      signature_cost: 1
      description: "Raw magic explodes outward"
    
    cleric_elena:
      name: "Divine Grace"
      effect: "Heal 2d6 to all allies in zone"
      normal_cost: 3
      signature_cost: 2
      description: "Golden light restores allies"
  
  evolution:
    minor_improvement:
      when: "2 milestones after creation"
      options:
        - "Reduce cost by 1 (minimum 0)"
        - "Add minor effect"
        - "Increase range/area"
    
    major_improvement:
      when: "Major milestone"
      options:
        - "Double effect"
        - "Remove limit"
        - "Add dramatic narrative permission"

# ============================================
# ENVIRONMENTAL COMBAT
# ============================================

environmental_factors:
  difficult_terrain:
    effect: "-1 zone movement"
    examples: ["Mud", "Rubble", "Thick vegetation"]
  
  hazardous_terrain:
    effect: "1d6 damage when entering"
    examples: ["Fire", "Acid", "Spikes"]
  
  cover:
    partial:
      effect: "+1 defense"
      examples: ["Low wall", "Large tree"]
    
    full:
      effect: "+2 defense, can't be targeted by some attacks"
      examples: ["Building corner", "Fortification"]
  
  elevation:
    higher_ground:
      effect: "+1 to attacks, +1 damage with ranged"
    
    lower_ground:
      effect: "-1 to attacks against higher opponents"
  
  visibility:
    darkness:
      effect: "-2 to attacks without darkvision"
    
    fog:
      effect: "Cannot target beyond Close range"
    
    blinding_light:
      effect: "-1 to all actions for 1 round"

# ============================================
# RETREAT AND ESCAPE
# ============================================

retreat_mechanics:
  overview:
    description: "Combat doesn't always end in victory or death"
    philosophy: "Provide meaningful options for escape without encouraging cowardice"

  fighting_withdrawal:
    description: "Orderly retreat while defending"
    requirement: "All party members use Defensive stance"
    effect: "Party can disengage from combat"
    cost: "Each character loses 1 Flow"

    procedure:
      1: "All party members switch to Defensive stance"
      2: "Each member loses 1 Flow (can go negative)"
      3: "Party moves 1 zone away as coordinated action"
      4: "Enemies may make one final attack at -2"

    tactical_note: "Coordinated defense allows escape, but costs momentum"

  rout:
    description: "Panicked flight from overwhelming danger"
    trigger: "Half or more of party at 0 Guard"
    alternative_trigger: "All party members agree to flee"

    effect: "Party scatters and escapes"
    consequences:
      immediate: "Enemies get one free attack per party member"
      flow: "All party members drop to -3 Flow"
      narrative: "Must regroup at safe location"

    recovery: "Party must take short rest before regaining Flow or continuing"

  tactical_retreat:
    description: "Abandoning position while minimizing losses"
    requirement: "At least one party member remains at positive Guard"

    method: "Party designates rear guard"
    rear_guard:
      role: "Covers party escape"
      benefit: "Party members escape without attacks"
      cost: "Rear guard faces all enemies alone for 1 round"
      reward: "Rear guard gains +2 Flow for bravery"

    design_note: "Creates heroic moments while enabling escape"

  pursuit:
    description: "Enemies chasing fleeing party"
    gm_discretion: true

    factors:
      enemy_motivation: "How much do they want to catch you?"
      terrain: "Can party lose them in complex environment?"
      speed: "Do enemies move faster?"

    escape_check:
      roll: "2d6 + grace or survival"
      tn: "10 for determined pursuit, 8 for casual"
      success: "Party escapes clean"
      failure: "Another encounter at disadvantage"

# ============================================
# SOCIAL COMBAT
# ============================================

social_combat:
  overview:
    description: "Conflicts resolved through words not weapons"
    uses_stances: true
    uses_flow: true
    health: "Composure instead of Guard/Vitality"
  
  composure:
    formula: "will + presence + 5"
    function: "Social resilience and resolve"
    recovery: "Full between scenes"
    at_zero: "Convinced, flees, or surrenders"
  
  social_stances:
    aggressive:
      approach: "Direct argument, intimidation"
      flow: "+1 on successful social attacks"
      vulnerability: "Easier to provoke"
    
    balanced:
      approach: "Negotiation, finding common ground"
      flow: "Normal generation"
      flexibility: "Can adapt approach"
    
    defensive:
      approach: "Listening, gathering information"
      flow: "+1 when learning secrets"
      advantage: "Harder to persuade"
  
  social_damage:
    formula: "1d6 + presence or relevant attribute"
    reduction: "Will provides 'social armor'"
    consequences: "Belief changes, agreements, revelations"

yaml/core_rules.yaml:
# Flow RPG Core Rules
# Version: 1.0-complete
# Last Updated: 2024

metadata:
  game_name: "Flow RPG"
  version: "1.0-complete"
  complexity: "rules-moderate"
  dice_system: "2d6"
  design_philosophy:
    - "Elegance over complexity"
    - "Perceived simplicity over dumb-simple"
    - "Narrative-first with tactical depth option"
    - "Flow as central unifying mechanic"
    - "Fail-forward built into resolution"
    - "65% baseline success rate"

# ============================================
# CORE RESOLUTION MECHANICS
# ============================================

resolution_system:
  basic_roll:
    formula: "2d6 + attribute + skill"
    range: 
      dice: [2, 12]
      attribute: [-5, 5]
      skill: [-2, 8]
    
  target_numbers:
    trivial: 
      value: 6
      success_rate_base: 91.7
      description: "Routine tasks under pressure"
    easy: 
      value: 7
      success_rate_base: 83.3
      description: "Basic professional work"
    standard: 
      value: 8
      success_rate_base: 72.2
      description: "Challenging professional tasks"
    hard: 
      value: 10
      success_rate_base: 41.7
      description: "Expert-level challenges"
    extreme: 
      value: 12
      success_rate_base: 16.7
      description: "Near-impossible feats"
    legendary: 
      value: 14
      success_rate_base: 2.8
      description: "Mythic achievements"
    
  success_tiers:
    failure:
      range: "6 or less"
      effect: "Action fails"
      flow_change: "+1 to opponent or creates consequence"
      narrative: "Complication or setback occurs"
    
    partial_success:
      range: "7-9"
      effect: "Success with cost or complication"
      flow_change: "No automatic change"
      narrative: "Yes, but..."
    
    full_success:
      range: "10-12"
      effect: "Complete success as intended"
      flow_change: "No automatic change"
      narrative: "Yes, and..."
    
    critical_success:
      base_threshold: 13
      scaling_rule: "13 + (total_modifier ÷ 3, rounded down)"
      effect: "Exceptional success with benefits"
      flow_change: "+1 Flow to character"
      narrative: "Yes, and something exceptional"

      threshold_examples:
        modifier_0_2: "Crit on 13+ (16.7% chance)"
        modifier_3_5: "Crit on 14+ (8.3% chance)"
        note: "With +5 max modifier, critical threshold caps at 14+, maintaining 8.3% crit rate throughout campaign"

      design_rationale: "Keeps crits rare and exciting throughout progression. With +5 cap and 14+ threshold, crits stay at healthy 8.3% rate even at peak power. Without scaling, high modifiers would crit 70%+ of the time, making them the default outcome rather than special moments."
    
    enhanced_success:
      trigger: "Beat TN by 5+"
      effect: "Gain advantage on next roll"
      flow_change: "Normal for tier"
      narrative: "Minor narrative permission"
    
    legendary_success:
      trigger: "Beat TN by 8+"
      effect: "Major narrative impact"
      flow_change: "+2 Flow total"
      narrative: "Major narrative permission"

  advantage_disadvantage:
    advantage:
      mechanic: "Roll 3d6, keep highest 2"
      sources:
        - "Superior position"
        - "Ally assistance"
        - "Enhanced success carry-over"
        - "Appropriate tools/preparation"
    
    disadvantage:
      mechanic: "Roll 3d6, keep lowest 2"
      sources:
        - "Poor position"
        - "Injured or exhausted"
        - "Inappropriate tools"
        - "Environmental hindrance"
    
    multiple_dice:
      rule: "Advantages and disadvantages cancel 1:1"
      maximum: "Never roll more than 4d6 total"

# ============================================
# FLOW SYSTEM
# ============================================

flow_system:
  basics:
    range: 
      minimum: -3
      maximum: 6
    starting_flow: 0
    reset: "Between scenes"
    
  starting_exceptions:
    none: "All callings now start at 0 Flow"
    
  flow_states:
    negative:
      range: [-3, -1]
      description: "Disrupted, struggling, disadvantage"
      effects:
        - "Cannot cast spells (except Will-based)"
        - "Narrative shows exhaustion/struggle"
        - "-1 to initiative order"
    
    neutral:
      range: [0, 0]
      description: "Balanced, ready, baseline"
      effects:
        - "No modifiers"
        - "Standard options available"
    
    positive:
      range: [1, 3]
      description: "In the flow, momentum building"
      effects:
        - "Can activate Flow techniques"
        - "Narrative shows confidence"
    
    high_positive:
      range: [4, 6]
      description: "Perfect flow, commanding presence"
      effects:
        - "Can activate advanced techniques"
        - "Narrative shows mastery"
        - "+1 to all rolls while maintained"
  
  generation_sources:
    universal:
      critical_success:
        trigger: "Reach critical threshold (see critical_success scaling rule)"
        amount: 1
        limit: "No limit"
        note: "Threshold scales with total modifier: 13 + (modifier ÷ 3)"
      
      taking_damage:
        trigger: "Take any damage to Guard or Vitality"
        amount: 1
        limit: "No limit"
        note: "New rule for balance"
    
    stance_specific:
      aggressive:
        successful_attack:
          trigger: "Hit with attack"
          amount: 1
          limit: "No limit"
        
        charging:
          trigger: "Move 2+ zones toward enemy"
          amount: 2
          limit: "Once per turn"
      
      balanced:
        critical_only:
          trigger: "Any critical success"
          amount: 1
          limit: "Stacks with universal"
      
      defensive:
        being_attacked:
          trigger: "Targeted by attack"
          amount: 1
          limit: "Once per round"
        
        successful_defense:
          trigger: "Successfully defend"
          amount: 1
          limit: "No limit"
    
    magic_specific:
      
      ritual_completion:
        trigger: "Complete 10+ minute ritual"
        amount: 3
        limit: "Once per scene"
    
    calling_specific:
      note: "See character.yaml for calling-specific triggers"
  
  expenditure:
    enhance_roll:
      cost: 1
      effect: "+1 to roll per Flow spent"
      limit: "Maximum +3"
    
    combat_techniques:
      basic: 
        cost: 1
        examples: ["Riposte", "Press Advantage"]
      moderate: 
        cost: 2
        examples: ["Whirlwind Strike", "Perfect Parry"]
      advanced: 
        cost: 3
        examples: ["Death Blow", "Battlefield Control"]
    
    spells:
      tier_0_cantrip:
        cost: 0
        note: "Flow-neutral magic"
      tier_1_basic:
        cost: 0
      tier_2_advanced: 
        cost: -1
      tier_3_expert: 
        cost: -2
      tier_4_master: 
        cost: -3
    
    narrative_advantages:
      minor:
        cost: 1
        examples: ["Recall useful fact", "Spot hidden detail"]
      moderate:
        cost: 2
        examples: ["Retroactive preparation", "Lucky coincidence"]
      major:
        cost: 3
        examples: ["Deus ex machina", "Legendary deed"]
    
    stance_switching:
      cost: 0
      note: "Free action, was -1 in original"

# ============================================
# SCENE STRUCTURE
# ============================================

scene_resolution:
  phases:
    1_setup:
      gm_actions:
        - "Describe situation and environment"
        - "Establish stakes and dangers"
        - "Position participants"
      player_actions:
        - "Ask clarifying questions"
        - "Declare initial stance/approach"
    
    2_engagement:
      structure: "Varies by scene type"
      types:
        combat: "See combat.yaml"
        social: "See social_combat rules"
        exploration: "Skill challenges"
        mixed: "Combine systems as needed"
    
    3_resolution:
      flow_reset: "All Flow returns to 0"
      guard_recovery: "Full Guard restoration"
      consequences: "Apply lasting effects"
      experience: "Note for milestone consideration"

  scene_types:
    combat:
      typical_length: "3-5 rounds"
      flow_range: [-3, 6]
      stance_based: true
      reference: "combat.yaml"
    
    social:
      typical_length: "3-7 exchanges"
      flow_range: [-2, 4]
      stance_based: true
      uses_composure: true
    
    exploration:
      typical_length: "4-6 skill checks"
      flow_range: [-1, 3]
      stance_based: false
      clock_based: true
    
    downtime:
      typical_length: "Narrative"
      flow_range: [0, 1]
      stance_based: false
      project_based: true

# ============================================
# ATTRIBUTES
# ============================================

attributes:
  range:
    minimum: -2
    maximum: 3
    average: 0
    note: "Capped at +3 to maintain bounded accuracy. Represents peak natural human capability without supernatural enhancement."
  
  physical:
    might:
      description: "Physical force, strength, endurance"
      primary_uses:
        - "Melee damage"
        - "Lifting/breaking"
        - "Physical intimidation"
      defensive_use: "Resist physical effects"
    
    grace:
      description: "Precision, agility, coordination"
      primary_uses:
        - "Ranged attacks"
        - "Dodging/acrobatics"
        - "Fine manipulation"
      defensive_use: "Avoid attacks"
  
  mental:
    mind:
      description: "Reasoning, intellect, knowledge"
      primary_uses:
        - "Spell precision"
        - "Investigation"
        - "Logical argument"
      defensive_use: "Resist deception"
    
    awareness:
      description: "Perception, intuition, attunement"
      primary_uses:
        - "Spell power"
        - "Detecting danger"
        - "Reading people"
      defensive_use: "Avoid ambush"
  
  social:
    will:
      description: "Fortitude, determination, spiritual power"
      primary_uses:
        - "Spell persistence"
        - "Resisting control"
        - "Death saves"
      defensive_use: "Mental fortitude"
    
    presence:
      description: "Charisma, magnetism, social influence"
      primary_uses:
        - "Spell drama"
        - "Leadership"
        - "Performance"
      defensive_use: "Social composure"
  
  starting_arrays:
    standard:
      values: [2, 1, 1, 0, 0, -1]
      description: "Well-rounded character"
    
    specialized:
      values: [3, 2, 0, 0, -1, -2]
      description: "Focused expertise"
    
    balanced:
      values: [1, 1, 1, 0, 0, 0]
      description: "No weaknesses"

# ============================================
# SKILLS
# ============================================

skills:
  skill_caps:
    total_modifier_maximum: "+5"
    formula: "Attribute + Skill + Edges ≤ 5"

    breakdown:
      attribute_max: "+3 (natural human limits)"
      skill_max: "+2 (Expert level)"
      edge_bonus: "+1 from specializations"

    design_rationale:
      - "Maintains bounded accuracy - prevents unlimited modifier inflation"
      - "97.2% success rate at cap vs TN 8 (nearly automatic - only fail on 1,1)"
      - "Supports 8-12 session campaigns perfectly"
      - "GMs should use TN 10-12 for meaningful challenges at peak power"

    bounded_accuracy_reality:
      philosophy: "Hard cap prevents runaway progression, but creates new challenge"

      success_rates_vs_tn_8:
        at_plus_0: "58.3% (7+ on 2d6)"
        at_plus_2: "86.1% (5+ on 2d6)"
        at_plus_3: "91.7% (4+ on 2d6)"
        at_plus_5: "97.2% (3+ on 2d6 - only fail on snake eyes)"

      the_problem:
        description: "Even with +5 cap, TN 8 becomes trivial at peak power"
        solution: "GMs must use higher TNs for late-game challenges"

      tn_scaling_guidance:
        sessions_1_3: "TN 8 for standard challenges (+0 to +2 modifiers: 58-86% success)"
        sessions_4_6: "TN 8-10 mix (+3 to +4 modifiers: 72-91% at TN 8)"
        sessions_7_12: "TN 10-12 standard (+5 modifier: 72% at TN 10, 42% at TN 12)"
        note: "Peak power heroes need harder challenges to feel meaningful risk"

      vs_alternative_caps:
        plus_4_cap: "Would give 91.7% vs TN 8 (4+ on 2d6) - better sweet spot"
        plus_3_cap: "Would give 83.3% vs TN 8 (5+ on 2d6) - too restrictive"
        plus_6_cap: "Would give 97.2% vs TN 8 (3+ on 2d6) - same problem as +5"
        design_tension: "+5 cap allows heroic growth but requires GM TN adjustment"

    examples:
      optimized_fighter:
        might: "+3"
        combat_expert: "+2"
        weapon_focus: "+1"
        total: "+6 (over cap, choose which bonuses apply)"
        note: "In practice: Use Might +3, Combat +2 for total +5"
        reality: "At +5, hits TN 8 97% of the time - GM should use TN 10+ in late game"

      skilled_rogue:
        grace: "+3"
        stealth_expert: "+2"
        urban_specialist: "+1"
        total: "+6 (over cap, must choose which bonuses apply)"
        note: "Can apply urban specialist (+1) OR grace+stealth (+5), not both beyond cap"

  progression_tiers:
    1_untrained:
      modifier: -2
      description: "No formal training"
      advancement: "Starting only"

    2_novice:
      modifier: -1
      description: "Basic understanding"
      advancement: "Starting or minor milestone"

    3_competent:
      modifier: 0
      description: "Professional capability"
      advancement: "Starting or minor milestone"

    4_professional:
      modifier: 1
      description: "Skilled practitioner"
      advancement: "Minor milestone"

    5_expert:
      modifier: 2
      description: "Pinnacle of mortal capability"
      advancement: "Moderate milestone"
      note: "Final skill tier - represents peak human achievement"

    design_note: "Master tier (+3) removed to maintain bounded accuracy throughout 8-12 session campaigns. Expert represents the absolute peak of human capability without becoming superhuman."
  
  skill_list:
    physical:
      combat:
        description: "Fighting, weapons, tactical positioning"
        key_attributes: ["might", "grace"]
        specializations: ["Melee", "Ranged", "Defensive"]
      
      athletics:
        description: "Running, climbing, swimming, strength"
        key_attributes: ["might", "grace"]
        specializations: ["Climbing", "Swimming", "Jumping"]
      
      stealth:
        description: "Hiding, sneaking, avoiding detection"
        key_attributes: ["grace", "awareness"]
        specializations: ["Urban", "Wilderness", "Social"]
      
      survival:
        description: "Tracking, foraging, navigation"
        key_attributes: ["awareness", "will"]
        specializations: ["Forest", "Desert", "Arctic"]
      
      finesse:
        description: "Lockpicking, sleight of hand, precision"
        key_attributes: ["grace", "mind"]
        specializations: ["Lockpicking", "Pickpocket", "Forgery"]
    
    mental:
      lore:
        description: "History, academics, specialized knowledge"
        key_attributes: ["mind", "awareness"]
        specializations: ["History", "Arcana", "Religion"]
      
      medicine:
        description: "Healing, anatomy, treating injuries"
        key_attributes: ["mind", "awareness"]
        specializations: ["Surgery", "Herbalism", "Diagnosis"]
      
      craft:
        description: "Making, repairing, engineering"
        key_attributes: ["mind", "grace"]
        specializations: ["Smithing", "Alchemy", "Engineering"]
      
      investigate:
        description: "Searching, analyzing, finding clues"
        key_attributes: ["mind", "awareness"]
        specializations: ["Crime Scenes", "Research", "Tracking"]
      
      sorcery:
        description: "Magical theory and spellcasting"
        key_attributes: ["mind", "awareness", "will", "presence"]
        specializations: ["Arcane", "Divine", "Primal"]
    
    social:
      persuade:
        description: "Convincing through reason and charm"
        key_attributes: ["presence", "mind"]
        specializations: ["Diplomacy", "Seduction", "Logic"]
      
      deceive:
        description: "Lying, disguise, misdirection"
        key_attributes: ["presence", "mind"]
        specializations: ["Lies", "Disguise", "Forgery"]
      
      perform:
        description: "Entertainment, inspiration, art"
        key_attributes: ["presence", "grace"]
        specializations: ["Music", "Oratory", "Dance"]
      
      command:
        description: "Leadership, intimidation, authority"
        key_attributes: ["presence", "will"]
        specializations: ["Military", "Intimidation", "Inspiration"]
      
      empathy:
        description: "Understanding emotions and motivations"
        key_attributes: ["awareness", "presence"]
        specializations: ["Detect Lies", "Therapy", "Animal Handling"]
  
  approach_determines_attribute:
    note: "The specific approach determines which attribute pairs with skill"
    examples:
      intimidation:
        might: "Physical threats"
        mind: "Logical consequences"
        presence: "Force of personality"
      
      athletics:
        might: "Raw power application"
        grace: "Acrobatic maneuvers"
        will: "Endurance tests"

# ============================================
# DICE CONVENTIONS
# ============================================

dice_conventions:
  standard_roll:
    formula: "2d6 + modifiers"
    average: 7
    range: [2, 12]
  
  advantage:
    formula: "3d6, keep highest 2"
    average: 8.46
    improvement: "+1.46 average"
  
  disadvantage:
    formula: "3d6, keep lowest 2"
    average: 5.54
    penalty: "-1.46 average"
  
  damage_dice:
    exploding:
      trigger: "Natural 6 on damage die"
      effect: "Roll again and add"
      milestone_requirement: 10
      stacks: true
  
  special_dice:
    flow_die:
      when: "Spending 3+ Flow on single roll"
      effect: "Add 1d6 to roll"
      color: "Different color die"
    
    calling_die:
      when: "Acting in perfect alignment with calling"
      effect: "Add 1d6, 6s count as two successes"
      limit: "Once per scene"

yaml/equipment.yaml:
# Flow RPG Equipment System
# Version: 1.0-complete
# Weapons, armor, items, and economy

equipment_system:
  philosophy:
    core_concept: "Equipment enhances but doesn't define characters"
    design_principles:
      - "Simple categories with meaningful choices"
      - "Equipment grows with characters"
      - "Quality matters more than quantity"
      - "Integration with Flow system"

# ============================================
# WEAPONS
# ============================================

weapons:
  categories:
    light_weapons:
      damage: "2d6"
      attribute_options: ["might", "grace"]
      special_property: "+1 to Finesse-based actions"
      weight: "Light"
      cost: "10-30 coins"
      
      examples:
        dagger:
          damage: "2d6"
          range: "Close when thrown"
          special: "Concealable"
          cost: 10
        
        shortsword:
          damage: "2d6"
          special: "Quick draw"
          cost: 20
        
        rapier:
          damage: "2d6"
          attribute: "grace only"
          special: "+1 to parry"
          cost: 30
        
        hand_axe:
          damage: "2d6"
          range: "Close when thrown"
          special: "Tool use"
          cost: 15
    
    medium_weapons:
      damage: "2d6+1"
      attribute_options: ["might", "grace"]
      special_property: "Balanced, no special rules"
      weight: "Medium"
      cost: "30-50 coins"
      
      examples:
        longsword:
          damage: "2d6+1"
          special: "Versatile (2d6+2 two-handed)"
          cost: 40
        
        mace:
          damage: "2d6+1"
          attribute: "might only"
          special: "Ignores 1 DR"
          cost: 35
        
        spear:
          damage: "2d6+1"
          special: "Reach, can brace"
          cost: 30
        
        battle_axe:
          damage: "2d6+1"
          special: "Brutal critical (+2 damage)"
          cost: 45
    
    heavy_weapons:
      damage: "2d6+2"
      attribute: "might only"
      special_property: "-1 Grace while wielding"
      weight: "Heavy"
      two_handed: true
      cost: "50-100 coins"
      
      examples:
        greatsword:
          damage: "2d6+2"
          special: "Cleave (hit 2 adjacent on crit)"
          cost: 75
        
        maul:
          damage: "2d6+2"
          special: "Knockback on hit"
          cost: 60
        
        greataxe:
          damage: "2d6+2"
          special: "Devastating critical (×3 on 12+)"
          cost: 80
        
        polearm:
          damage: "2d6+2"
          special: "Reach, brace, trip"
          cost: 70
    
    reach_weapons:
      damage: "2d6"
      attribute_options: ["might", "grace"]
      special_property: "Attack from Close range"
      weight: "Medium"
      cost: "40-60 coins"
      
      examples:
        pike:
          damage: "2d6"
          special: "Extra reach (2 zones)"
          two_handed: true
          cost: 50
        
        halberd:
          damage: "2d6"
          special: "Versatile damage types"
          two_handed: true
          cost: 55
        
        whip:
          damage: "2d6"
          attribute: "grace only"
          special: "Disarm, trip, grab"
          cost: 40
        
        lance:
          damage: "2d6"
          special: "+2 damage on charge"
          mounted: "Required for full effect"
          cost: 60
    
    thrown_weapons:
      damage: "2d6"
      range: "Close"
      special_property: "+1 Flow when hit at Close range"
      weight: "Light"
      returning: "Some enchanted versions"
      cost: "5-20 coins each"
      
      examples:
        javelin:
          damage: "2d6"
          range: "Close or Far at -2"
          quantity: "Bundle of 3"
          cost: 15
        
        throwing_axe:
          damage: "2d6"
          special: "Can use in melee"
          quantity: "Bundle of 3"
          cost: 18
        
        chakram:
          damage: "2d6"
          attribute: "grace only"
          special: "Returns on miss"
          cost: 20
        
        sling_bullet:
          damage: "2d6"
          range: "Far with sling"
          quantity: "Pouch of 20"
          cost: 5
    
    ranged_weapons:
      damage: "2d6"
      range: "Far"
      special_property: "+1 damage at Far, -2 when Engaged"
      weight: "Medium"
      ammunition: "Required"
      cost: "30-150 coins"
      
      examples:
        shortbow:
          damage: "2d6"
          attribute: "grace only"
          range: "Far"
          special: "Quick shot"
          ammo: "Arrows"
          cost: 30
        
        longbow:
          damage: "2d6"
          attribute: "grace only"
          range: "Far or Extreme"
          special: "+1 damage"
          ammo: "Arrows"
          cost: 60
        
        crossbow:
          damage: "2d6+1"
          attribute: "mind or grace"
          range: "Far"
          special: "Loading (every other turn)"
          ammo: "Bolts"
          cost: 80
        
        heavy_crossbow:
          damage: "2d6+2"
          range: "Far or Extreme"
          special: "Loading, ignores 2 DR"
          ammo: "Bolts"
          cost: 150
  
  weapon_properties:
    versatile:
      description: "Use one or two-handed"
      one_handed: "Normal damage"
      two_handed: "+1 damage"
    
    finesse:
      description: "Use Grace instead of Might"
      benefit: "Attribute choice flexibility"
    
    loading:
      description: "Requires action to reload"
      limitation: "Attack every other turn"
      benefit: "Usually higher damage"
    
    reach:
      description: "Attack from further away"
      benefit: "Strike from Close range"
    
    brutal:
      description: "Devastating wounds"
      benefit: "Extra critical damage"
    
    defensive:
      description: "Aids in defense"
      benefit: "+1 to defensive actions"
  
  weapon_quality:
    crude:
      modifier: "-1 to hit"
      cost_multiplier: 0.5
      description: "Poorly made"
    
    standard:
      modifier: 0
      cost_multiplier: 1
      description: "Normal quality"
    
    fine:
      modifier: "+1 to hit OR damage"
      cost_multiplier: 5
      description: "Excellent craftsmanship"
    
    masterwork:
      modifier: "+1 to hit AND damage"
      cost_multiplier: 10
      description: "Artisan creation"
    
    legendary:
      modifier: "+2 to hit and damage"
      cost_multiplier: "Priceless"
      special: "Unique properties"
      description: "Weapons of legend"

# ============================================
# ARMOR
# ============================================

armor:
  types:
    no_armor:
      damage_reduction: 0
      penalties:
        grace: 0
        flow: "None"
      benefits:
        flow_when_hit: "+1 Flow when taking damage"
        spellcasting_bonus: "+1 to Sorcery checks"
        extra_movement: "+1 zone per turn"
      cost: 0
      description: "Clothing only"
    
    light_armor:
      damage_reduction: 1
      penalties:
        grace: 0
        flow: "None"
        spellcasting: 0
      benefits:
        initiative: "+1 to act sooner in stance"
        stealth_capable: "No Stealth penalty"
      cost: "20-50 coins"
      
      examples:
        padded:
          dr: 1
          special: "Quiet"
          cost: 20
        
        leather:
          dr: 1
          special: "Flexible"
          cost: 30
        
        studded_leather:
          dr: 1
          special: "+1 vs. slashing"
          cost: 40
        
        hide:
          dr: 1
          special: "Natural camouflage"
          cost: 35
    
    medium_armor:
      damage_reduction: 2
      penalties:
        grace: -1
        flow: "None"
        spellcasting: -1
      benefits:
        guard_bonus: "+1 Guard at scene start"
        balanced: "No stance restrictions"
      cost: "50-150 coins"
      
      examples:
        chain_shirt:
          dr: 2
          special: "Concealable under clothes"
          cost: 80
        
        scale_mail:
          dr: 2
          special: "+1 vs. piercing"
          cost: 100
        
        breastplate:
          dr: 2
          special: "Vital protection"
          cost: 120
        
        ring_mail:
          dr: 2
          special: "Flexible"
          cost: 90
    
    heavy_armor:
      damage_reduction: 4
      penalties:
        grace: -2
        flow: "-1 to all Flow generation"
        spellcasting: -3
      benefits:
        knockback_immunity: "Cannot be moved"
        damage_reduction: "Highest available"
      cost: "200-500 coins"
      
      examples:
        splint_mail:
          dr: 4
          special: "Reinforced joints"
          cost: 250
        
        banded_mail:
          dr: 4
          special: "Distributed weight"
          cost: 300
        
        half_plate:
          dr: 4
          special: "Good mobility for heavy"
          cost: 400
        
        full_plate:
          dr: 4
          special: "+1 DR vs. all"
          cost: 500
  
  shields:
    buckler:
      guard_bonus: 1
      special: "Can use with two-handed"
      cost: 15
      weight: "Light"
    
    small_shield:
      guard_bonus: 1
      special: "Quick to ready"
      cost: 20
      weight: "Light"
    
    medium_shield:
      guard_bonus: 2
      special: "Standard protection"
      cost: 30
      weight: "Medium"
    
    large_shield:
      guard_bonus: 2
      special: "Provides partial cover"
      cost: 40
      weight: "Medium"
    
    tower_shield:
      guard_bonus: 3
      special: "Full cover, -1 to attacks"
      cost: 60
      weight: "Heavy"

# ============================================
# ADVENTURING GEAR
# ============================================

adventuring_gear:
  kits:
    adventurers_kit:
      contents:
        - "Backpack"
        - "Bedroll"
        - "Rations (1 week)"
        - "Rope (50 ft)"
        - "Torches (10)"
        - "Waterskin"
        - "Basic tools"
      cost: 25
      weight: "Medium load"
    
    dungeoneers_kit:
      contents:
        - "Everything in adventurer's kit"
        - "Grappling hook"
        - "Hammer and pitons (10)"
        - "Crowbar"
        - "Chalk"
        - "10-foot pole"
      cost: 50
      weight: "Heavy load"
    
    healers_kit:
      contents:
        - "Bandages"
        - "Herbs"
        - "Salves"
        - "Surgical tools"
      uses: 10
      benefit: "+1 to Medicine checks"
      cost: 40
    
    thieves_tools:
      contents:
        - "Lockpicks"
        - "Small mirror"
        - "File"
        - "Tension wrenches"
      benefit: "Required for lockpicking"
      quality:
        standard: 
          cost: 30
          bonus: 0
        masterwork:
          cost: 150
          bonus: "+1 to Finesse"
    
    disguise_kit:
      contents:
        - "Makeup"
        - "Wigs"
        - "Costume pieces"
        - "False papers"
      benefit: "Required for disguise"
      uses: 10
      cost: 35
  
  consumables:
    healing_potion:
      effect: "Restore 2d6 Vitality"
      action: "Drink as action"
      cost: 50
      rarity: "Common"
    
    antidote:
      effect: "Cure poison"
      action: "Drink as action"
      cost: 30
      rarity: "Common"
    
    alchemists_fire:
      effect: "1d6 fire damage, ongoing"
      action: "Throw at Close range"
      cost: 25
      rarity: "Common"
    
    smoke_bomb:
      effect: "Obscure vision in zone"
      action: "Throw or drop"
      cost: 20
      rarity: "Common"
    
    flash_powder:
      effect: "Blind for 1 round"
      action: "Throw at Close range"
      cost: 30
      rarity: "Uncommon"
  
  tools_and_utilities:
    rope:
      types:
        hemp:
          length: "50 feet"
          strength: "Standard"
          cost: 5
        silk:
          length: "50 feet"
          strength: "Superior, lighter"
          cost: 25
    
    light_sources:
      torch:
        duration: "1 hour"
        radius: "Close range"
        cost: 1
      
      lantern:
        duration: "6 hours per oil"
        radius: "Close range, directed"
        cost: 15
      
      sunrod:
        duration: "6 hours"
        radius: "Close range"
        cost: 10
    
    climbing_gear:
      grappling_hook:
        benefit: "+1 to climbing"
        cost: 10
      
      climbers_kit:
        benefit: "+2 to climbing"
        cost: 40
      
      pitons:
        quantity: 10
        benefit: "Secure climbing"
        cost: 5

# ============================================
# MAGIC ITEMS
# ============================================

magic_items:
  rarity_tiers:
    common:
      power: "Minor benefits"
      cost: "50-200 coins"
      availability: "Major cities"
    
    uncommon:
      power: "Useful abilities"
      cost: "200-1000 coins"
      availability: "Specialist shops"
    
    rare:
      power: "Significant advantages"
      cost: "1000-5000 coins"
      availability: "Special order"
    
    very_rare:
      power: "Powerful effects"
      cost: "5000-25000 coins"
      availability: "Quest rewards"
    
    legendary:
      power: "Campaign-changing"
      cost: "Priceless"
      availability: "Unique artifacts"
  
  enhancement_bonuses:
    plus_1:
      weapons: "+1 hit and damage"
      armor: "+1 DR"
      cost_multiplier: 10
      rarity: "Uncommon"
    
    plus_2:
      weapons: "+2 hit and damage"
      armor: "+2 DR"
      cost_multiplier: 50
      rarity: "Rare"
    
    plus_3:
      weapons: "+3 hit and damage"
      armor: "+3 DR"
      cost_multiplier: 200
      rarity: "Very rare"
  
  weapon_properties:
    flaming:
      effect: "+1d6 fire damage"
      cost: "+2000 coins"
      rarity: "Rare"
    
    frost:
      effect: "+1d6 cold damage"
      cost: "+2000 coins"
      rarity: "Rare"
    
    shock:
      effect: "+1d6 lightning damage"
      cost: "+2000 coins"
      rarity: "Rare"
    
    keen:
      effect: "Critical on 11+"
      cost: "+3000 coins"
      rarity: "Rare"
    
    vorpal:
      effect: "Behead on natural 12"
      cost: "Priceless"
      rarity: "Legendary"
    
    returning:
      effect: "Returns when thrown"
      cost: "+1500 coins"
      rarity: "Uncommon"
  
  armor_properties:
    fortification:
      light: "25% crit negation"
      moderate: "50% crit negation"
      heavy: "75% crit negation"
      cost: "+1000/3000/5000"
    
    glamered:
      effect: "Appears as clothing"
      cost: "+1500 coins"
      rarity: "Uncommon"
    
    ethereal:
      effect: "No spellcasting penalty"
      cost: "+4000 coins"
      rarity: "Rare"
    
    invulnerability:
      effect: "DR 5 once per scene"
      cost: "Priceless"
      rarity: "Legendary"
  
  wondrous_items:
    stat_boosters:
      belt_of_might:
        effect: "+1 Might"
        cost: 2000
        rarity: "Rare"
      
      gloves_of_grace:
        effect: "+1 Grace"
        cost: 2000
        rarity: "Rare"
      
      headband_of_mind:
        effect: "+1 Mind"
        cost: 2000
        rarity: "Rare"
    
    utility_items:
      bag_of_holding:
        effect: "Holds 500 lbs, weighs 15"
        cost: 1500
        rarity: "Uncommon"
      
      boots_of_speed:
        effect: "+1 zone movement"
        cost: 2500
        rarity: "Rare"
      
      cloak_of_protection:
        effect: "+1 to all defenses"
        cost: 1000
        rarity: "Uncommon"
      
      ring_of_flow:
        effect: "+1 maximum Flow"
        cost: 3000
        rarity: "Rare"

# ============================================
# EQUIPMENT PROGRESSION
# ============================================

equipment_progression:
  bonding_system:
    description: "Equipment grows with use"
    
    stages:
      familiar:
        uses: "10 successful uses"
        benefit: "+1 to specific action"
      
      trusted:
        uses: "25 successful uses"
        benefit: "Ignore 1 on damage/defense"
      
      bonded:
        uses: "50 successful uses"
        benefit: "Counts as +1 magical"
      
      legendary:
        uses: "100 successful uses"
        benefit: "Unique magical property"
  
  milestone_upgrades:
    minor_milestone:
      options:
        - "Repair and improve gear"
        - "Add minor modification"
        - "Acquire quality version"
    
    moderate_milestone:
      options:
        - "Commission masterwork"
        - "Add magical enhancement"
        - "Discover rare material"
    
    major_milestone:
      options:
        - "Forge legendary item"
        - "Awaken item intelligence"
        - "Create artifact"
  
  signature_equipment:
    description: "Personal iconic gear"
    
    creation:
      when: "Moderate milestone"
      process: "Name and describe"
      benefit: "Grows with character"
    
    evolution:
      minor: "+1 enhancement"
      moderate: "Special property"
      major: "Legendary ability"

# ============================================
# ECONOMY
# ============================================

economy:
  currency:
    copper: 
      value: 1
      description: "Common transactions"
    
    silver:
      value: 10
      description: "Standard currency"
    
    gold:
      value: 100
      description: "Major purchases"
    
    platinum:
      value: 1000
      description: "Noble wealth"
  
  starting_wealth:
    by_archetype:
      fighter: "3d6 × 10 gold"
      ranger: "2d6 × 10 gold"
      paladin: "4d6 × 10 gold"
      rogue: "4d6 × 10 gold"
      wizard: "2d6 × 10 gold"
      cleric: "3d6 × 10 gold"
      bard: "3d6 × 10 gold"
  
  lifestyle_expenses:
    wretched:
      cost: "0/month"
      description: "Homeless"
    
    poor:
      cost: "20 gold/month"
      description: "Basic shelter"
    
    modest:
      cost: "100 gold/month"
      description: "Simple comfort"
    
    comfortable:
      cost: "200 gold/month"
      description: "Middle class"
    
    wealthy:
      cost: "500 gold/month"
      description: "Fine living"
    
    aristocratic:
      cost: "1000+ gold/month"
      description: "Luxury"
  
  services:
    healing:
      first_aid: "5 gold"
      cure_disease: "50 gold"
      remove_curse: "100 gold"
      resurrection: "5000 gold"
    
    transport:
      coach_ride: "3 copper/mile"
      ship_passage: "1 silver/mile"
      teleportation: "100 gold/person"
    
    information:
      common_knowledge: "1 silver"
      specific_fact: "10 gold"
      secret_information: "100+ gold"
    
    magical:
      identify_item: "20 gold"
      cast_spell: "10 gold × spell tier"
      enchant_item: "Days × 100 gold"

# ============================================
# ENCUMBRANCE
# ============================================

encumbrance:
  system: "Simplified slot-based"
  
  carrying_capacity:
    light_load:
      slots: "might + 5"
      effect: "No penalty"
    
    medium_load:
      slots: "might + 10"
      effect: "-1 to physical actions"
    
    heavy_load:
      slots: "might + 15"
      effect: "-2 to physical, -1 zone movement"
  
  item_slots:
    tiny: 0.1  # "Coins, gems, rings"
    small: 0.5  # "Daggers, potions, tools"
    medium: 1   # "Swords, armor pieces"
    large: 2    # "Two-handed weapons, full armor"
    bulky: 3    # "Awkward items"
  
  container_capacity:
    pouch: "2 slots of small items"
    backpack: "8 slots"
    saddlebags: "12 slots"
    bag_of_holding: "50 slots, weighs 1"
  
  quick_rules:
    ignore: "Items under 0.5 slots"
    weapons: "1 slot each"
    armor_worn: "Doesn't count"
    armor_carried: "Full slot value"

yaml/examples.yaml:
# Flow RPG Examples & Quick Start
# Version: 1.0-complete
# Pre-generated characters, play examples, and tutorials

quick_start:
  what_you_need:
    required:
      - "2-5 players (including GM)"
      - "Two six-sided dice per player"
      - "Character sheets"
      - "This reference"
    
    optional:
      - "Tokens for Flow tracking"
      - "Battle map and miniatures"
      - "Initiative tracker"

  fastest_start:
    step_1: "Choose pre-gen character"
    step_2: "GM reads scenario"
    step_3: "Start playing, learn as you go"
    step_4: "Reference rules as needed"

# ============================================
# PRE-GENERATED CHARACTERS
# ============================================

pregenerated_characters:
  
  # Level 0 (Starting Characters)
  
  marcus_ironforge:
    concept: "Dwarven Defender"
    level: "Starting (0 milestones)"
    
    identity:
      species: "Dwarf"
      archetype: "Fighter"
      calling: "Guardian"
    
    attributes:
      might: 3  # Base 2 + Dwarf 1
      grace: 0
      mind: -2
      awareness: -1
      will: 2
      presence: 0
    
    skills:
      professional: ["Combat +2"]
      novice: ["Athletics -1", "Command -1"]
      untrained: "All others at -2"
    
    derived_values:
      guard: 11  # 8 + 3(Might) + 0
      vitality: 12  # 10 + 2(Will)
      flow: 
        current: 0
        max: 6
      movement: 1
    
    equipment:
      armor: "Medium (DR 2, -1 Grace)"
      weapons: ["Longsword (2d6+1)", "Shield (+2 Guard)"]
      gear: ["Adventurer's kit", "50 gold"]
    
    special_abilities:
      species:
        stone_endurance: "Reduce first Vitality damage by 2"
        craftwise: "Ask one question about worked materials"
        steady_stance: "Free switch from Defensive"
      calling:
        protective_surge: "When ally takes damage, gain +1 Flow"
        helpers_intuition: "Know when someone needs help"
      edge:
        tough: "+2 Guard (included)"
    
    personality:
      trait: "Protective to a fault"
      ideal: "No one gets hurt on my watch"
      bond: "Shield-siblings with party"
      flaw: "Takes all blame for failures"
    
    tactics:
      preferred_stance: "Defensive"
      strategy: "Draw attacks, protect allies"
      flow_use: "Rally and defensive techniques"
  
  silvara_moonwhisper:
    concept: "Elven Scout"
    level: "Starting (0 milestones)"
    
    identity:
      species: "Elf"
      archetype: "Ranger"
      calling: "Seeker"
    
    attributes:
      might: 0
      grace: 3  # Base 2 + Elf 1
      mind: 0
      awareness: 1
      will: -1
      presence: 1
    
    skills:
      professional: ["Survival +2"]
      novice: ["Combat -1", "Investigate -1"]
      untrained: "All others at -2"
    
    derived_values:
      guard: 11  # 8 + 3(Grace) + 0
      vitality: 9   # 10 + (-1)(Will)
      flow:
        current: 0
        max: 6
      movement: 1
    
    equipment:
      armor: "Light (DR 1)"
      weapons: ["Longbow (2d6)", "Shortsword (2d6)"]
      gear: ["Tracking kit", "Climbing gear", "30 gold"]
    
    special_abilities:
      species:
        fey_grace: "+1 Flow on critical success"
        magical_affinity: "Sense magic in Near range"
        elven_focus: "Ignore first armor penalty to casting"
      calling:
        authentic_insight: "+3 Flow when trying new approach"
        soul_reading: "Ask one deep question per scene"
      edge:
        precise_strike: "Reroll one damage die"
    
    personality:
      trait: "Questions everything"
      ideal: "Truth matters more than comfort"
      bond: "Searching for lost sister"
      flaw: "Struggles with authority"
    
    tactics:
      preferred_stance: "Balanced"
      strategy: "Ranged support, scouting"
      flow_use: "Enhanced shots, perception"
  
  elena_lightbringer:
    concept: "Human Healer"
    level: "Starting (0 milestones)"
    
    identity:
      species: "Human"
      archetype: "Cleric"
      calling: "Mediator"
    
    attributes:
      might: 0
      grace: 0
      mind: 2  # Base 1 + Human 1
      awareness: 1
      will: 1
      presence: 0
    
    skills:
      professional: ["Medicine +2", "Empathy +2"]
      novice: ["Sorcery -1"]
      competent: ["Persuade 0"]  # Human versatile
      untrained: "All others at -2"
    
    derived_values:
      guard: 8   # 8 + 0 + 0
      vitality: 11  # 10 + 1(Will)
      flow:
        current: 0
        max: 6
      movement: 1
      spellcasting: "Yes (Mind 2 + Awareness 1 = 3)"
    
    equipment:
      armor: "Medium (DR 2, -1 Grace, -1 Sorcery)"
      weapons: ["Mace (2d6+1)", "Holy symbol"]
      gear: ["Healer's kit", "Prayer book", "35 gold"]
    
    special_abilities:
      species:
        versatile: "Extra Competent skill"
        determined: "+1 Flow when recovering from negative"
        adaptable: "Swap skills during rest"
      calling:
        harmony_restoration: "+1 Flow to all when resolving conflict"
        universal_understanding: "Understand any communication"
      spellcasting:
        tradition: "Divine"
        known_spells: ["Heal", "Shield", "Bolt", "Light"]
    
    personality:
      trait: "Sees all sides"
      ideal: "Peace is always possible"
      bond: "Sworn to protect the innocent"
      flaw: "Avoids necessary conflicts"
    
    tactics:
      preferred_stance: "Defensive"
      strategy: "Heal and support"
      flow_use: "Healing spells, protection"
  
  # After Minor Milestones (Session 3-4)
  
  finn_quickblade:
    concept: "Halfling Trickster"
    level: "3 Minor Milestones"
    
    identity:
      species: "Halfling"
      archetype: "Rogue"
      calling: "Enthusiast"
    
    attributes:
      might: -2
      grace: 3
      mind: 0
      awareness: 2
      will: 0  # Base -1 + Halfling 1
      presence: 0
    
    skills:
      professional: ["Stealth +2", "Finesse +2"]
      competent: ["Deceive 0"]  # Upgraded
      novice: ["Athletics -1"]  # New
      untrained: "All others at -2"
    
    derived_values:
      guard: 13  # 8 + 3(Grace) + 6(milestones)
      vitality: 10  # 10 + 0
      flow:
        current: 0
        max: 7  # Flow Harmony edge
      movement: 2  # Fast Movement edge
    
    equipment:
      armor: "Light (DR 1)"
      weapons: ["Daggers (2d6)", "Shortbow (2d6)"]
      gear: ["Masterwork thieves' tools", "Disguise kit", "100 gold"]
    
    special_abilities:
      species:
        lucky: "Flow stops at 0 once per scene"
        brave_heart: "+1 Flow when ally goes negative"
        small_but_mighty: "Move through enemies, +2 to hide"
      calling:
        joyful_flow: "Share Flow with adjacent allies"
        silver_lining: "Find benefit in any situation"
      edges:
        flow_harmony: "+1 max Flow"
        fast_movement: "+1 zone movement"
        riposte: "Counter after successful defense"
    
    personality:
      trait: "Eternally optimistic"
      ideal: "Life's too short not to enjoy"
      bond: "Party is chosen family"
      flaw: "Can't resist a good prank"
    
    tactics:
      preferred_stance: "Aggressive"
      strategy: "Flank, sneak attack, share Flow"
      flow_use: "Mobility and team support"
  
  # After Moderate Milestone (Session 6)
  
  aldric_stormcaller:
    concept: "Human Wizard"
    level: "1 Moderate, 2 Minor Milestones"
    
    identity:
      species: "Human"
      archetype: "Wizard"
      calling: "Scholar"
    
    attributes:
      might: -1
      grace: 1  # Base 0 + Human 1
      mind: 3  # Base 2 + Advancement 1
      awareness: 1
      will: 0
      presence: 1
    
    skills:
      expert: ["Sorcery +4"]  # Upgraded
      professional: ["Lore +2"]
      competent: ["Investigate 0"]  # Upgraded
      novice: ["Craft -1"]  # New
      untrained: "All others at -2"
    
    derived_values:
      guard: 12  # 8 + 1(Grace) + 6(milestones)
      vitality: 10  # 10 + 0
      flow:
        current: 1  # Scholar starts at +1
        max: 7  # Flow Harmony edge
      movement: 2  # No armor bonus
      spellcasting: "Yes (Mind 3 + Awareness 1 = 4)"
    
    equipment:
      armor: "None (DR 0, +1 Flow when hit, +1 Sorcery)"
      weapons: ["Staff (2d6)", "Wand focus"]
      gear: ["Spellbook", "Component pouch", "Research notes", "200 gold"]
    
    special_abilities:
      species:
        versatile: "Extra skill"
        determined: "+1 Flow recovery"
        adaptable: "Swap skills"
      calling:
        prepared_mind: "Start at +1 Flow"
        contingency_planning: "Declare preparation once/scene"
      signature_move:
        name: "Arcane Tempest"
        effect: "3d6 to all in zone"
        cost: "2 Flow (reduced from 3)"
      metamagic:
        quicken: "+1 Flow to cast as swift action"
        empower: "+2 Flow for +50% damage"
    
    known_spells:
      cantrips: ["Spark", "Mage Armor", "Light", "Prestidigitation"]
      tier_1: ["Bolt", "Shield", "Charm", "Detect Magic"]
      tier_2: ["Fireball", "Fly", "Invisibility"]
      tier_3: ["Lightning Storm"]
    
    personality:
      trait: "Constantly theorizing"
      ideal: "Knowledge should be preserved"
      bond: "Seeking lost magical library"
      flaw: "Overthinks simple problems"
    
    tactics:
      preferred_stance: "Balanced"
      strategy: "Control battlefield with spells"
      flow_use: "Big spells at key moments"

# ============================================
# PLAY EXAMPLES
# ============================================

play_examples:
  
  basic_skill_check:
    scenario: "Marcus tries to break down a door"
    
    step_1_approach:
      player: "I'll shoulder-charge the door with my full weight"
      gm: "That's using your Might with Athletics"
    
    step_2_roll:
      dice: [4, 3]
      modifiers:
        might: 3
        athletics: -1
      total: 9
    
    step_3_result:
      gm: "9 is a partial success. The door splinters and swings open, but you stumble through off-balance. You're in the room but you'll have -1 to your next action as you recover."
    
    step_4_flow:
      change: "No Flow change on partial success"
  
  combat_round:
    scenario: "Party fights goblin ambushers"
    
    setup:
      party:
        - "Marcus (Defensive)"
        - "Silvara (Balanced)"
        - "Elena (Defensive)"
      enemies:
        - "Goblin Chief (Aggressive)"
        - "2 Goblin Archers (Defensive)"
    
    turn_1_aggressive:
      goblin_chief:
        action: "Charges Marcus"
        roll: [5, 4]
        modifiers: "+2 Combat"
        total: 11
        result: "Hits for 7 damage, reduced to 5 by armor"
        marcus_guard: "11 → 6"
        flow: "Chief gains +1 (Aggressive hit)"
    
    turn_2_balanced:
      silvara:
        action: "Shoots Chief with bow"
        roll: [6, 5]
        modifiers: "+3 Grace, -1 Combat"
        total: 13
        result: "Critical! 2d6 damage: 9 to Chief"
        flow: "Silvara gains +1 (critical)"
    
    turn_3_defensive:
      marcus:
        action: "Defends and watches for opening"
        roll: [3, 5]
        modifiers: "+0 Grace, +2 Combat"
        total: 10
        result: "Success, +2 Guard until next turn"
        guard: "6 → 8 temporary"
        flow: "+1 (successful defense in Defensive)"
      
      elena:
        action: "Casts Heal on Marcus"
        roll: [4, 6]
        modifiers: "+2 Mind, -1 Sorcery"
        total: 11
        result: "Success, Marcus regains 2d6: 8 Guard"
        marcus_guard: "8 → 11 (full)"
        flow: "Elena at -1 (spell cost)"
      
      goblin_archers:
        action: "Fire at Silvara"
        result: "One hits for 5 damage"
        silvara_guard: "11 → 6"
        silvara_flow: "+1 (took damage)"
  
  social_encounter:
    scenario: "Elena negotiates with suspicious town guard"
    
    setup:
      elena_approach: "Mediator calling, seeking peaceful resolution"
      guard_attitude: "Suspicious (-2 to social rolls against)"
      stakes: "Party needs entrance to investigate"
    
    round_1:
      elena:
        stance: "Defensive (listening)"
        action: "I listen to his concerns first"
        roll: [5, 6]
        modifiers: "+1 Awareness, +2 Empathy"
        total: 14
        result: "Critical! Learn guard lost family to adventurers"
        flow: "+1 (Defensive in social)"
    
    round_2:
      elena:
        stance: "Balanced"
        action: "I acknowledge his loss and explain we're here to help"
        roll: [3, 4]
        modifiers: "+0 Presence, +0 Persuade, +1 Flow spent"
        total: 8
        result: "Partial success. He's listening but needs proof"
        composure: "Guard at 3/5"
    
    round_3:
      elena:
        action: "I show him our charter from the church"
        calling_benefit: "Universal Understanding - no roll needed"
        result: "Automatic success through calling"
        resolution: "Guard allows entry with escort"
        flow: "+1 to all (Mediator resolved conflict)"
  
  spellcasting_example:
    scenario: "Aldric uses magic in combat"
    
    turn_1_setup:
      aldric:
        flow: 1  # Scholar starts at +1
        stance: "Aggressive"
        action: "Cast Spark cantrip"
        roll: [4, 5]
        modifiers: "+3 Mind, +4 Sorcery"
        total: 16
        result: "Hit! 1d6: 4 damage"
        flow: "+2 total (cantrip +1, Aggressive +1)"
        new_flow: 3
    
    turn_2_buildup:
      aldric:
        flow: 3
        action: "Cast Bolt (Tier 1)"
        attribute_choice: "Mind for precision"
        effect: "3+d6 damage, ignores cover"
        roll: "Auto-hits behind cover"
        damage: "3+4 = 7"
        flow_cost: 0
        new_flow: 3
    
    turn_3_nova:
      aldric:
        flow: 3
        action: "Signature Move: Arcane Tempest"
        cost: 2  # Reduced from 3
        effect: "3d6 to all enemies in zone"
        damage: "14 to all"
        new_flow: 1
        narrative: "Lightning crackles through the battlefield"

# ============================================
# QUICK RULES REFERENCE
# ============================================

rules_reference:
  basic_roll: "2d6 + Attribute + Skill vs TN 8"
  
  success_levels:
    "6_or_less": "Failure"
    "7_to_9": "Partial Success"
    "10_to_12": "Full Success"
    "13_plus": "Critical Success (+1 Flow)"
  
  flow_quick:
    range: "-3 to +6"
    gain:
      - "Critical success: +1"
      - "Take damage: +1"
      - "Stance-specific triggers"
    spend:
      - "Boost roll: +1 per point"
      - "Techniques: varies"
      - "Spells: 0 to -3"
  
  stance_summary:
    aggressive:
      order: "First"
      bonus: "+1 damage, +1 Flow on hit"
      penalty: "-1 defense"
    balanced:
      order: "Second"
      bonus: "Flexible"
      special: "Free stance switch 1/combat"
    defensive:
      order: "Last"
      bonus: "+2 defense, +1 Flow when attacked"
      penalty: "-1 damage"
  
  combat_actions:
    attack: "Roll + Combat vs TN 8"
    defend: "+2 Guard on success"
    maneuver: "Create advantage"
    rally: "Recover 1d6 Guard (1/scene)"
    move: "1 zone"
  
  spell_costs:
    tier_0: "+1 Flow (generates)"
    tier_1: "0 Flow"
    tier_2: "-1 Flow"
    tier_3: "-2 Flow"
    tier_4: "-3 Flow"

# ============================================
# FIRST SESSION GUIDE
# ============================================

first_session:
  preparation:
    before_session:
      - "Read basic mechanics"
      - "Choose starting scenario"
      - "Print character sheets"
      - "Prepare tokens for Flow"
    
    session_zero_topics:
      - "Tone and content boundaries"
      - "Character connections"
      - "Campaign style preference"
      - "House rules if any"
  
  starting_scenario:
    title: "The Flowing Goblet"
    
    hook: "Goblins stole the town's magical cup that purifies water"
    
    scene_1_investigation:
      location: "Town square"
      challenge: "Gather information"
      skill_checks:
        - "Empathy to comfort victims"
        - "Investigate for clues"
        - "Persuade for witness info"
      discovery: "Goblins went to old mine"
    
    scene_2_journey:
      location: "Forest path"
      challenge: "Environmental hazard"
      options:
        stealth: "Sneak past wolf pack"
        survival: "Find safe path"
        combat: "Fight through"
      flow_opportunity: "Build Flow for mine"
    
    scene_3_mine_entrance:
      location: "Abandoned mine"
      challenge: "Goblin guards"
      encounter:
        enemies:
          - "2 Goblin scouts (Defensive)"
          - "1 Goblin warrior (Aggressive)"
        environment: "Can use mine carts"
        flow_use: "First combat techniques"
    
    scene_4_confrontation:
      location: "Mine depths"
      challenge: "Goblin shaman with cup"
      options:
        combat: "Defeat shaman"
        social: "Negotiate return"
        clever: "Trick or steal"
      twist: "Goblins also need clean water"
    
    resolution_options:
      violent: "Take cup by force"
      peaceful: "Share water source"
      clever: "Find second solution"
    
    rewards:
      success:
        - "Return water to town"
        - "100 gold reward"
        - "Minor milestone"
      extra:
        - "Peaceful: Goblin allies"
        - "Violent: Goblin enmity"
        - "Clever: Extra treasure"
  
  gm_tips:
    first_combat:
      - "Go slow, explain each step"
      - "Demonstrate stance benefits"
      - "Show Flow generation"
      - "Allow takebacks for learning"
    
    flow_management:
      - "Remind players when they gain Flow"
      - "Suggest Flow uses"
      - "Show GM Flow pool"
      - "Demonstrate complications"
    
    calling_integration:
      - "Point out calling triggers"
      - "Reward calling roleplay"
      - "Use narrative permissions"
      - "Connect to character goals"
  
  common_mistakes:
    players:
      - "Forgetting Flow gains"
      - "Not using stance benefits"
      - "Hoarding Flow too long"
      - "Ignoring calling benefits"
    
    gm:
      - "Forgetting Flow for damage"
      - "Not using GM Flow pool"
      - "Making single enemies too weak"
      - "Ignoring partial success"
  
  ending_session:
    wrap_up:
      - "Award minor milestone"
      - "Discuss advancement choices"
      - "Get feedback on system"
      - "Set next session expectations"
    
    between_sessions:
      - "Players choose advancement"
      - "GM prepares next adventure"
      - "Adjust based on feedback"
      - "Build on established fiction"

yaml/gm_tools.yaml:
# Flow RPG Game Master Tools
# Version: 1.0-complete
# GM guidance, encounter building, and campaign management

gm_system:
  philosophy:
    core_concept: "Enable dynamic storytelling through Flow"
    principles:
      - "Story first, rules second"
      - "Flow creates narrative momentum"
      - "Fail forward always"
      - "Player agency matters"

# ============================================
# FLOW ECONOMY MANAGEMENT
# ============================================

flow_management:
  gm_flow_pool:
    description: "GM's narrative currency"
    starting: "3 + number of players"
    maximum: 10
    reset: "Between sessions"
    
    generation:
      player_failure: "+1 when PC fails importantly"
      dramatic_moment: "+1 when tension peaks"
      villain_success: "+1 when antagonist succeeds"
      scene_change: "+2 at dramatic scene transitions"
    
    expenditure:
      introduce_complication:
        cost: 1
        effect: "Add unexpected obstacle"
      
      enhance_enemy:
        cost: 2
        effect: "Enemy gains advanced ability"
      
      environmental_hazard:
        cost: 1
        effect: "Activate environmental danger"
      
      reinforce:
        cost: 3
        effect: "Bring in reinforcements"
      
      escape_route:
        cost: 2
        effect: "Villain escapes dramatically"
      
      narrative_twist:
        cost: 4
        effect: "Major plot revelation"
  
  flow_transparency:
    visible_to_players: "Optional but recommended"
    benefits:
      - "Creates tension"
      - "Players understand stakes"
      - "Collaborative storytelling"
    
    communication:
      gaining: "I'm gaining Flow from that failure"
      spending: "Spending 2 Flow for complication"
      warning: "I have 8 Flow built up..."

# ============================================
# ENCOUNTER BUILDING
# ============================================

encounter_building:
  challenge_rating:
    formula: "Total Enemy Power / Party Average Power"
    
    difficulty_bands:
      trivial:
        ratio: "< 0.5"
        description: "No real threat"
        flow_generation: "Minimal"
      
      easy:
        ratio: "0.5 - 0.75"
        description: "Minor challenge"
        flow_generation: "Low"
      
      standard:
        ratio: "0.75 - 1.25"
        description: "Fair fight"
        flow_generation: "Moderate"
      
      hard:
        ratio: "1.25 - 1.75"
        description: "Serious challenge"
        flow_generation: "High"
      
      deadly:
        ratio: "> 1.75"
        description: "Potential TPK"
        flow_generation: "Extreme"
  
  enemy_templates:
    henchman:
      guard: "7 + party_milestones"
      vitality: "5 + party_milestones"
      damage: "1d6 + (party_milestones / 2)"
      skills: "One at Professional"
      flow: "Starts at 0"
      special: "Should survive 2 hits at each tier, dangerous in groups"
      description: "Numerous followers, individually weak but not tissue paper"
      design_note: "Playtest showed original formula (Guard 5, Vit 3 = 8 total) resulted in one-shot kills. New formula provides 12+ durability to require 2 hits."

    worthy_opponent:
      guard: "13 + (party_milestones × 3)"
      vitality: "21 + (party_milestones × 3)"
      damage: "2d6 + (party_milestones / 2)"
      skills: "Two at Professional"
      flow: "Starts at 0"
      special: "Equal match for individual heroes"
      description: "Capable adversary matching party members"
      design_note: "Lasts 2-3 rounds under focus fire, longer in mixed encounters"

    elite:
      guard: "40 + (party_milestones × 8)"
      vitality: "70 + (party_milestones × 14)"
      damage: "2d6+2 + party_milestones"
      damage_reduction: 2
      skills: "Two or three at Expert (+2)"
      flow: "Starts at +2"
      actions_per_round: 3
      legendary_resistances: "3 per scene"

      action_economy:
        philosophy: "Three actions prevent Elite from being overwhelmed, but prevent TPK alpha strikes"
        options:
          standard: "Attack twice + use technique (recommended)"
          full_offense: "Attack three times, but third attack has disadvantage (roll 3d6 keep lowest 2)"
          balanced: "Attack once + use two techniques"

        focus_fire_restriction:
          rule: "Second or third attack against same target in one round has disadvantage"
          mechanic: "Roll 3d6, keep lowest 2"
          rationale: "Prevents Elite from focus-firing single PC to death. Incentivizes spreading attacks."
          example: "Elite attacks Fighter twice: First attack normal (2d6+2+milestones), second attack with disadvantage (3d6 keep lowest 2, +2+milestones)"

        design_note: "Reduced damage from 3d6 to 2d6+2 (13.5→10.5 avg) and disadvantage on focus fire prevents instant kills while keeping Elite threatening. At milestone 3: First attack 13.5 avg, second on same target 10.5 avg = 24 total (down from 27). Spread across targets still deadly but not TPK-inducing."

      special: "Three actions per round with balanced economy, DR 2, legendary resistances"
      description: "Formidable threat requiring focused effort and party coordination"
      design_note: "Playtest-proven durability: 110 at milestone 0, 154 at milestone 3, 198 at milestone 6, 242 at milestone 9. Creates 4-6 round encounters against optimized parties with ~40 DPR. Sweet Spot Edition balanced for 0-12 milestone campaigns."
  
  encounter_composition:
    overwhelming_force:
      description: "Single powerful opponent with significant advantages"
      composition: "1 Elite"
      tactics: "Tests party coordination and resource management"
      guidance: "Elite acts multiple times per round OR has environmental advantages"
      notes: "Legendary resistance (3/scene) represents adaptability"

    coordinated_threat:
      description: "Elite leading organized group"
      composition: "1 Elite + 4-6 Henchmen"
      tactics: "Leader coordinates followers tactically"
      guidance: "Henchmen enable Elite's strategy through positioning and support"
      notes: "Elite adapts tactics when strategy fails"

    elite_squad:
      description: "Multiple skilled opponents"
      composition: "2-3 Elites"
      tactics: "Coordinated strikes and combination attacks"
      guidance: "Each Elite has distinct capability, they support each other"
      notes: "Focus fire and divide-and-conquer both valid approaches"

    overwhelming_numbers:
      description: "Numerous weak opponents"
      composition: "10+ Henchmen"
      tactics: "Swarm and surround tactics"
      guidance: "Use swarm rules for efficiency"
      notes: "Area effects and choke points become critical"

    asymmetric_conflict:
      description: "Mixed opposition with varied capabilities"
      composition: "1 Elite + 2 Worthy Opponents + 3 Henchmen"
      tactics: "Layered challenge with distinct roles"
      guidance: "Each opponent type complements the others tactically"
      notes: "Reinforcements may arrive based on narrative circumstances"
  
  environmental_factors:
    hazards:
      ongoing_damage:
        examples: ["Fire", "Acid", "Extreme cold"]
        effect: "1d6 per round in area"
        flow: "Generate when PCs affected"
      
      movement_restriction:
        examples: ["Mud", "Web", "Ice"]
        effect: "-1 zone movement"
        tactical: "Control positioning"
      
      visibility:
        examples: ["Darkness", "Fog", "Smoke"]
        effect: "-2 to ranged attacks"
        benefit: "Enables ambush"
    
    interactive_elements:
      destructible_cover:
        durability: "10-20 damage to destroy"
        effect: "Provides protection until destroyed"
      
      environmental_weapons:
        examples: ["Chandelier", "Boulder", "Explosive barrels"]
        damage: "3d6 area effect"
        activation: "1 action + skill check"
      
      terrain_advantage:
        high_ground: "+1 attack and damage"
        choke_point: "Limit enemy numbers"
        escape_route: "Alternative resolution"

# ============================================
# NPC GENERATION
# ============================================

npc_generation:
  quick_npc:
    name_and_role: "Define immediately"
    motivation: "What do they want?"
    memorable_trait: "One distinctive feature"
    
    mechanical_needs:
      social_npc:
        skills: "Two social at Professional"
        composure: "Will + Presence + 5"
        flow: "Starts at 0"
      
      combat_npc:
        template: "Use henchman/worthy_opponent/elite"
        modify: "Adjust for role"
      
      specialist_npc:
        expert_skill: "One at Expert (+2) - pinnacle of mortal achievement"
        other_skills: "Competent or less"
  
  memorable_traits:
    physical:
      - "Unusual height (very tall/short)"
      - "Distinctive scar or marking"
      - "Unusual hair/eye color"
      - "Missing limb or prosthetic"
      - "Distinctive clothing style"
    
    behavioral:
      - "Specific speech pattern"
      - "Nervous tic or habit"
      - "Catchphrase or saying"
      - "Unusual laugh"
      - "Specific fear or phobia"
    
    social:
      - "Overly formal/casual"
      - "Constantly suspicious"
      - "Inappropriately cheerful"
      - "Never makes eye contact"
      - "Whispers everything"
  
  npc_motivations:
    basic_drives:
      survival: "Stay alive and safe"
      wealth: "Acquire resources"
      power: "Gain influence/control"
      knowledge: "Learn secrets"
      revenge: "Settle old scores"
      love: "Protect/pursue relationships"
    
    calling_based:
      advocate: "Fix what's wrong"
      guardian: "Protect someone"
      exemplar: "Prove superiority"
      seeker: "Find identity"
      scholar: "Understand truth"
      sentinel: "Maintain security"
      enthusiast: "Experience excitement"
      champion: "Demonstrate strength"
      mediator: "Create harmony"

# ============================================
# CAMPAIGN MANAGEMENT
# ============================================

campaign_management:
  campaign_types:
    episodic:
      description: "Self-contained adventures"
      flow_reset: "Full reset each session"
      advancement: "Milestone per episode"
      benefits: "Easy to run, flexible"
    
    serial:
      description: "Ongoing connected story"
      flow_reset: "Carries between sessions"
      advancement: "Natural story beats"
      benefits: "Deep character development"
    
    sandbox:
      description: "Player-driven exploration"
      flow_reset: "By location"
      advancement: "Discovery-based"
      benefits: "Maximum agency"
    
    hybrid:
      description: "Serial with episodic elements"
      flow_reset: "Varies by arc"
      advancement: "Mixed approach"
      benefits: "Best of both worlds"
  
  session_structure:
    opening:
      recap: "What happened last time"
      intentions: "What are we doing today"
      flow_check: "Starting Flow states"
      scene_set: "Where we begin"
    
    rising_action:
      encounters: "2-3 challenges"
      flow_building: "Tension increases"
      complications: "Things go wrong"
    
    climax:
      major_challenge: "Climactic encounter"
      flow_maximum: "Peak resources"
      decisive_moment: "Victory or defeat"
    
    resolution:
      consequences: "What changed"
      rewards: "Treasure and growth"
      hooks: "Next session seeds"
      flow_reset: "Return to baseline"
  
  pacing_tools:
    tension_management:
      build_tension:
        - "Increase enemy Flow generation"
        - "Add time pressure"
        - "Reveal stakes gradually"
        - "Use environmental hazards"
      
      release_tension:
        - "Comic relief NPC"
        - "Safe haven location"
        - "Minor victory"
        - "Resource discovery"
    
    flow_pacing:
      slow_start: "Let players build Flow"
      midpoint_spike: "Big Flow expenditure opportunity"
      climax_management: "Both sides maximum Flow"
      denouement: "Gentle Flow reduction"
  
  milestone_timing:
    minor_milestone_triggers:
      - "End of satisfying session"
      - "Significant discovery"
      - "Overcome personal challenge"
      - "Creative problem solution"
    
    moderate_milestone_triggers:
      - "Complete story arc"
      - "Defeat recurring villain"
      - "Save community"
      - "Major character growth"
    
    major_milestone_triggers:
      - "Complete campaign chapter"
      - "World-changing event"
      - "Legendary achievement"
      - "Transform the setting"

# ============================================
# RULES ADJUDICATION
# ============================================

adjudication:
  core_principles:
    fiction_first:
      rule: "What makes sense in story?"
      application: "Rules support narrative"
    
    yes_and:
      rule: "Build on player ideas"
      application: "Add complications, not roadblocks"
    
    fail_forward:
      rule: "Failure creates opportunity"
      application: "Every roll changes situation"
  
  common_rulings:
    attribute_choice:
      principle: "Approach determines attribute"
      examples:
        intimidation:
          might: "Physical threats"
          mind: "Logical consequences"
          presence: "Force of personality"
          will: "Unbreakable stare"
    
    skill_overlap:
      principle: "Most specific skill applies"
      examples:
        climbing:
          athletics: "General climbing"
          survival: "Natural cliff faces"
          finesse: "Precise handholds"
    
    edge_cases:
      group_checks:
        rule: "Highest roller + assists"
        assist: "+1 per helper (max +3)"
      
      extended_challenges:
        rule: "Multiple successes needed"
        track: "Progress clock method"
      
      contested_rolls:
        rule: "Highest total wins"
        tie: "Defender/status quo wins"
  
  house_rule_guidelines:
    before_implementing:
      - "Discuss with players"
      - "Test for one session"
      - "Get feedback"
      - "Adjust or abandon"
    
    common_modifications:
      brutal_combat: "Injuries on Vitality damage"
      heroic_play: "Start with +1 Flow"
      gritty_realism: "Slower healing"
      high_magic: "Reduce spell costs by 1"

# ============================================
# SWEET SPOT EDITION CAMPAIGN GUIDANCE
# ============================================

sweet_spot_edition:
  philosophy: "Flow RPG Sweet Spot Edition - Bounded accuracy that actually works"

  campaign_parameters:
    ideal_length: "8-12 sessions"
    modifier_cap: "+5 total (attribute + skill + edges)"
    design_goal: "TN 8 stays relevant from session 1 through campaign conclusion"
    retirement: "Characters conclude at peak power around session 12"

  power_progression:
    session_1_2:
      typical_modifier: "+0 to +2"
      vs_tn_8: "42-58% success"
      description: "Challenging but achievable - heroes finding their footing"
      threats: "Local bandits, wild animals, minor mysteries"

    session_3_4:
      typical_modifier: "+2 to +3"
      vs_tn_8: "58-72% success"
      description: "Competent professionals - feel heroic without being automatic"
      threats: "Organized crime, cultists, dangerous beasts"

    session_5_6:
      typical_modifier: "+3 to +4"
      vs_tn_8: "72-83% success"
      description: "Regional heroes - reliable but not infallible"
      threats: "Noble houses, young dragons, demon cults"

    session_7_9:
      typical_modifier: "+4 to +5"
      vs_tn_8: "83-91% success"
      description: "Famous heroes - legendary skill with meaningful risk"
      threats: "Ancient guardians, powerful organizations, planar threats"

    session_10_12:
      typical_modifier: "+5 (at cap)"
      vs_tn_8: "97.2% success"
      description: "Legendary heroes - peak mortal capability, but rolls feel nearly automatic"
      threats: "Demon lords, ancient dragons, world-ending catastrophes"
      note: "Campaign concludes here - characters retire at peak power"
      design_warning: "At +5, TN 8 rolls are nearly automatic (35/36 outcomes succeed). Use TN 10+ for meaningful challenges. Bounded accuracy works but requires higher TNs at peak power."

  target_numbers:
    philosophy: "TN 8 remains the standard throughout - no scaling needed"

    standard_tns:
      trivial: 6
      easy: 7
      standard: 8
      hard: 10
      extreme: 12
      legendary: 14

    implementation:
      sessions_1_12: "Use these same TNs throughout the entire campaign"
      bounded_accuracy: "With +5 cap, even legendary challenges (TN 14) have 16.7% success rate"
      no_scaling_needed: "System naturally maintains challenge through capped modifiers"

  design_rationale:
    core_insight: "Bounded accuracy requires ACTUALLY bounding the modifiers"
    sweet_spot: "8-12 sessions is the natural lifespan for +0 to +5 progression"
    retirement: "Characters conclude at heroic peak rather than grinding toward diminishing returns"
    vs_unlimited_progression: "Avoids the 15+ session trap where +8 modifiers break TN 8 (97% success = not a meaningful roll)"

  gm_guidance:
    embrace_conclusion: "Plan for campaign arc to conclude around session 10-12"
    next_campaign: "Start fresh with new characters for new stories"
    legacy_benefits: "Retired characters can mentor new PCs or become world NPCs"
    sweet_spot_sweet: "This length provides complete character arcs without mechanical breakdown"

# ============================================
# TOOLS AND RESOURCES
# ============================================

gm_tools:
  random_tables:
    quick_npc_generator:
      d6_profession:
        1: "Merchant"
        2: "Guard"
        3: "Craftsperson"
        4: "Scholar"
        5: "Criminal"
        6: "Noble"
      
      d6_attitude:
        1: "Hostile"
        2: "Suspicious"
        3: "Neutral"
        4: "Friendly"
        5: "Helpful"
        6: "Fanatical"
    
    complication_generator:
      combat:
        1: "Reinforcements arrive"
        2: "Environment becomes hazardous"
        3: "Objective changes"
        4: "Innocent in danger"
        5: "Equipment failure"
        6: "Unexpected betrayal"
      
      social:
        1: "Authority arrives"
        2: "Secret revealed"
        3: "Mistaken identity"
        4: "Cultural misunderstanding"
        5: "Rival appears"
        6: "Time pressure added"
  
  tracking_sheets:
    combat_tracker:
      per_combatant:
        - "Name and stance"
        - "Current Guard/Vitality"
        - "Flow (current/max)"
        - "Conditions"
        - "Initiative order position"
    
    flow_tracker:
      player_flow:
        - "Character name"
        - "Current Flow"
        - "Flow triggers used"
        - "Signature moves available"
      
      gm_flow:
        - "Current pool"
        - "Complications available"
    
    campaign_tracker:
      milestone_progress:
        - "Sessions since last milestone"
        - "Significant achievements"
        - "Character growth moments"
        - "Pending rewards"
      
      story_threads:
        - "Active plots"
        - "Background events"
        - "Villain plans"
        - "Timer/countdown events"

# ============================================
# SAFETY TOOLS
# ============================================

safety_tools:
  session_zero:
    discuss:
      - "Content boundaries"
      - "Tone expectations"
      - "Safety mechanisms"
      - "Communication preferences"
    
    establish:
      - "Lines (never cross)"
      - "Veils (fade to black)"
      - "X-card availability"
      - "Check-in schedule"
  
  ongoing_safety:
    x_card:
      description: "Tap to skip content"
      no_questions: "No explanation needed"
    
    check_ins:
      timing: "Break points"
      method: "Thumbs up/down"
    
    aftercare:
      debrief: "Post-session discussion"
      support: "Available if needed"

# ============================================
# CAMPAIGN THEMES
# ============================================

campaign_themes:
  theme_as_mechanics:
    horror:
      flow_modification: "Negative Flow = fear"
      special_rules: "Sanity tracking"
      tone: "Diminishing resources"
    
    heroic:
      flow_modification: "Start at +1"
      special_rules: "Death saves easier"
      tone: "Larger than life"
    
    political:
      flow_modification: "Social Flow pools"
      special_rules: "Reputation tracking"
      tone: "Consequences matter"
    
    exploration:
      flow_modification: "Discovery generates Flow"
      special_rules: "Resource management"
      tone: "Wonder and danger"
  
  genre_modifications:
    modern:
      equipment: "Firearms and technology"
      magic: "Hidden or scientific"
      flow: "Adrenaline/confidence"
    
    sci_fi:
      equipment: "Energy weapons, spacecraft"
      magic: "Psionics or tech"
      flow: "Quantum probability"
    
    post_apocalyptic:
      equipment: "Scavenged and makeshift"
      magic: "Mutations or lost tech"
      flow: "Desperation/hope"

yaml/index.yaml:
# Flow RPG Complete System Index
# Version: 2.0-restructured
# Master file referencing all system components

flow_rpg_system:
  metadata:
    name: 'Flow RPG'
    version: '2.1-sweet-spot-edition'
    format: 'YAML structured rules'
    date: '2024'
    status: 'Sweet Spot Edition - Bounded accuracy that actually works'

  components:
    core_rules:
      file: 'core_rules.yaml'
      contains:
        - 'Basic mechanics and dice'
        - 'Resolution system'
        - 'Flow economy'
        - 'Attributes and skills with caps (+5 max total)'
        - 'Scene structure'
        - 'True bounded accuracy system'

    character:
      file: 'character.yaml'
      contains:
        - 'Character creation process'
        - 'Species (4 types)'
        - 'Archetypes (7 optional templates)'
        - 'Custom Build alternative'
        - 'Callings (9 types)'
        - 'Derived values (no auto-scaling)'
        - 'Magic access requirements'

    combat:
      file: 'combat.yaml'
      contains:
        - 'Stance system'
        - 'Zone-based movement'
        - 'Health (Guard/Vitality)'
        - 'Armor and weapons'
        - 'Combat techniques'
        - 'Death and dying'
        - 'Social combat'

    magic:
      file: 'magic.yaml'
      contains:
        - 'Spell tiers (0-4)'
        - 'Attribute-based casting'
        - 'Complete spell list'
        - 'Magical traditions'
        - 'Metamagic'
        - 'Ritual magic'
        - 'Magic items'

    advancement:
      file: 'advancement.yaml'
      contains:
        - 'Sweet Spot Edition milestone system'
        - 'Minor milestones (every session)'
        - 'Moderate milestones (sessions 3, 6, 9)'
        - 'Major milestones (sessions 5 and 10)'
        - 'Edges system'
        - 'Campaign designed for 8-12 sessions'
        - 'Retirement at peak power'

    techniques:
      file: 'techniques.yaml'
      contains:
        - 'Universal ability access'
        - 'Combat Techniques'
        - 'Metamagic options'
        - 'Divine abilities'
        - 'Roguish gambits'
        - 'Bardic inspiration'
        - 'Terrain mastery'
        - 'No archetype requirements'

    equipment:
      file: 'equipment.yaml'
      contains:
        - 'Weapon categories'
        - 'Armor types'
        - 'Adventuring gear'
        - 'Magic items'
        - 'Economy and costs'
        - 'Equipment progression'
        - 'Encumbrance'

    gm_tools:
      file: 'gm_tools.yaml'
      contains:
        - 'Flow management for GMs'
        - 'Encounter building'
        - 'NPC generation'
        - 'Campaign management'
        - 'Rules adjudication'
        - 'Safety tools'
        - 'Random tables'

    examples:
      file: 'examples.yaml'
      contains:
        - 'Pre-generated characters'
        - 'Play examples'
        - 'Quick rules reference'
        - 'First session guide'
        - 'Starting scenario'
        - 'Common mistakes'

  quick_reference:
    basic_mechanic: '2d6 + Attribute + Skill vs TN 8'

    flow_summary:
      range: [-3, 6]
      start: 0
      gain: ['Critical success', 'Taking damage', 'Stance triggers']
      spend: ['Boost rolls', 'Techniques', 'Spells']

    stances:
      aggressive: 'Act first, +1 damage, +1 Flow on hit'
      balanced: 'Act second, flexible, free switch'
      defensive: 'Act last, +2 defense, +1 Flow when attacked'

    health:
      guard: '12 + max(Might, Grace, Will)'
      vitality: '10 + Will'
      progression: 'Through milestone choices, not automatic'

    advancement:
      minor: 'Every session (horizontal growth)'
      moderate: 'Sessions 3, 6, 9 (capability expansion)'
      major: 'Sessions 5 and 10 (transformative power)'
      campaign_length: '8-12 sessions to peak power'

    spell_tiers:
      0: 'Cantrips (+1 Flow)'
      1: 'Basic (0 Flow)'
      2: 'Advanced (-1 Flow)'
      3: 'Expert (-2 Flow)'
      4: 'Master (-3 Flow)'

  design_notes:
    sweet_spot_edition:
      philosophy: 'Bounded accuracy that ACTUALLY works'
      core_insight: 'Unlimited progression breaks bounded accuracy - cap modifiers or TN 8 becomes meaningless'
      solution: 'Hard cap at +5 total modifier (attribute +3, skill +2, edges +1)'
      campaign_length: '8-12 sessions is the natural lifespan for +0 to +5 progression'
      retirement: 'Characters conclude at heroic peak rather than grinding through mechanical breakdown'
      math: 'At +5 cap: 97.2% success vs TN 8 (nearly automatic - only fail on 1,1)'
      reality_check: 'Even with +5 cap, TN 8 becomes trivial. GMs use TN 10-12 for peak power challenges.'
      vs_old_system: 'Old +8 cap resulted in 99.5% success (truly automatic)'
      sweet_spot: 'This length provides complete character arcs, but requires TN scaling in practice'

    version_2_restructuring:
      - 'Milestone pacing matches D&D dopamine schedule'
      - 'Custom Build option enables true character freedom'
      - 'Archetypes now optional starting templates'
      - 'Universal techniques accessible to all'
      - 'Major milestones arrive while still playing'
      - 'The "unicorn" - no multiclassing needed'

    rebalanced_from_original:
      - 'Flow range reduced to -3/+6'
      - 'Added Novice skill tier'
      - 'Cantrips are Flow-neutral (cost 0)'
      - 'Guard/Vitality no longer auto-scale'
      - 'Death saves use flat rolls'
      - 'Skills cap at Expert (+2), not Master (+3)'
      - 'Attributes cap at +3, not +5'

    mathematical_fixes:
      - '58% base success rate at +0 modifier'
      - '97.2% success at cap (+5 vs TN 8) - nearly automatic, requires TN scaling'
      - 'Guard ranges 10-19 (not 37+)'
      - 'Combat lasts 4-6 rounds at all tiers'
      - 'Progression meaningful AND bounded'
      - 'TN 8 relevant early game, TN 10-12 needed for late game challenges'

    structural_improvements:
      - 'Archetypes optional, not restrictive'
      - 'Any character can learn any ability'
      - 'Techniques.yaml unifies all subsystems'
      - 'Milestone rewards are choices not automatic'
      - 'True character customization achieved'

  usage_guide:
    character_creation_options:
      quick_start:
        - 'Choose an archetype for instant playability'
        - 'Everything pre-selected and balanced'
        - 'Can diverge later if desired'

      custom_build:
        - 'Start with blank slate'
        - 'Choose 3 skills and starting edge'
        - '100 coin equipment budget'
        - 'Build exactly what you envision'

      hybrid_approach:
        - 'Start with archetype'
        - 'Immediately begin customizing'
        - 'Keep what works, change what doesn't'

    for_players:
      start_with: ['character.yaml', 'techniques.yaml']
      reference: ['core_rules.yaml', 'combat.yaml', 'magic.yaml']
      advancement: ['advancement.yaml', 'techniques.yaml']

    for_gms:
      preparation: ['gm_tools.yaml']
      running: ['core_rules.yaml', 'combat.yaml']
      development: ['advancement.yaml']

    for_quick_start:
      1: 'Read examples.yaml first session guide'
      2: 'Use pregenerated characters'
      3: 'Run starting scenario'
      4: 'Reference rules as needed'

    for_conversion:
      from_original:
        - 'Apply rebalanced formulas'
        - 'Add Novice skill tier'
        - 'Adjust spell costs'
        - 'Recalculate Guard and Vitality'

      from_other_systems:
        - 'Use archetype equivalents'
        - 'Convert HP to Guard/Vitality'
        - 'Map abilities to Flow techniques'
        - 'Adapt monsters using templates'

  validation:
    completeness:
      rules: '100% - All mechanics defined'
      character_options: '100% - All combinations viable'
      gm_support: '100% - Full toolkit provided'
      examples: '100% - Multiple levels shown'

    balance:
      archetypes: 'All within 15% effectiveness'
      species: 'All mechanically viable'
      callings: 'All trigger regularly'
      advancement: 'Smooth progression curve'

    playability:
      complexity: 'Rules-moderate as intended'
      learning_curve: '2-3 sessions to master'
      reference_speed: 'Quick lookup via YAML structure'
      digital_tools: 'Ready for automation'

  implementation:
    physical_play:
      required: ['2d6 per player', 'Character sheets', 'Flow tokens']
      optional: ['Battle map', 'Miniatures', 'Initiative tracker']

    virtual_play:
      vtt_compatible: true
      dice_roller: 'Standard 2d6'
      character_sheets: 'YAML → form conversion'
      automation: 'Flow tracking priority'

    digital_tools:
      parser_ready: true
      database_structure: 'Hierarchical YAML'
      api_potential: 'Full rule automation'
      app_framework: 'Component-based design'

  license:
    notice: 'Complete game system in YAML format'
    usage: 'Full system implementation'
    modification: 'Encouraged with attribution'
    distribution: 'Share complete file set'
# End of Index File
# This completes the Flow RPG YAML implementation
# All rules, mechanics, and content are now structured data

yaml/magic.yaml:
# Flow RPG Magic System
# Version: 1.0-complete
# Spells, traditions, and magical mechanics

magic_system:
  philosophy:
    core_concept: "Same spell, different effects based on approach"
    design_principles:
      - "Elegance over complexity"
      - "Narrative-first with mechanical depth"
      - "Flow integration central"
      - "Player agency in casting approach"
  
  access_requirements:
    archetype_override:
      rule: "If archetype provides Sorcery skill, can cast regardless of attributes"
      affected: ["wizard", "cleric", "paladin", "bard"]
    
    attribute_requirements:
      arcane:
        formula: "mind + awareness >= 2"
        description: "Intellectual magical study"
      
      divine:
        formula: "will + presence >= 2"
        description: "Faith-based channeling"
      
      primal:
        formula: "awareness + will >= 2"
        description: "Natural world connection"
      
      performance:
        formula: "presence + grace >= 2"
        description: "Artistic magical expression"

# ============================================
# SPELL TIERS AND COSTS
# ============================================

spell_tiers:
  tier_0_cantrips:
    flow_cost: 0
    description: "Simple magics requiring no Flow investment"
    power_level: "Minor effects"
    examples: ["spark", "mage_armor", "light", "prestidigitation"]

    strategic_use:
      - "Free magical pressure without Flow cost"
      - "Maintain offense when Flow is neutral"
      - "Fill gaps between bigger spells"
  
  tier_1_basic:
    flow_cost: 0
    description: "Fundamental spells, Flow neutral"
    power_level: "Standard combat/utility effects"
    examples: ["bolt", "shield", "charm", "blur"]
    
    strategic_use:
      - "Reliable damage/protection"
      - "No Flow investment needed"
      - "Sustained casting possible"
  
  tier_2_advanced:
    flow_cost: -1
    description: "Powerful effects requiring momentum"
    power_level: "Significant impact"
    examples: ["fireball", "heal", "fly", "invisibility"]
    
    strategic_use:
      - "Turning point spells"
      - "Worth Flow investment"
      - "Combo with cantrips for Flow management"
  
  tier_3_expert:
    flow_cost: -2
    description: "Major magical effects"
    power_level: "Battle-changing"
    examples: ["lightning_storm", "teleport", "polymorph"]
    
    strategic_use:
      - "Decisive moments"
      - "Requires Flow buildup"
      - "Often combat-ending"
  
  tier_4_master:
    flow_cost: -3
    description: "Reality-altering magic"
    power_level: "Legendary effects"
    examples: ["time_stop", "dominate", "meteor_swarm"]
    
    strategic_use:
      - "Campaign climax moments"
      - "Requires perfect Flow management"
      - "Often scene-defining"

# ============================================
# SPELL POINTS (OPTIONAL RULE)
# ============================================

spell_points:
  description: "Alternative resource management for groups that prefer limited casting"
  optional: true
  philosophy: "Trade Flow integration for traditional resource tracking"

  pool_calculation:
    formula: "3 + Will modifier"
    minimum: 3
    maximum: 7
    recovery: "Full restoration between scenes"

    examples:
      low_will:
        will: 0
        points: 3
        note: "Can cast 3 Tier-1 spells or 1 Tier-3"

      moderate_will:
        will: 2
        points: 5
        note: "Can cast 5 Tier-1 or 2 Tier-2 + 1 Tier-1"

      high_will:
        will: 4
        points: 7
        note: "Can cast 7 Tier-1 or 2 Tier-3 + 1 Tier-1"

  spell_costs:
    tier_0_cantrips: 0
    tier_1_basic: 1
    tier_2_advanced: 2
    tier_3_expert: 3
    tier_4_master: 4

  interaction_with_flow:
    description: "Spell points replace Flow costs for spells"
    flow_generation: "Still generate Flow from critical successes and stances"
    flow_expenditure: "Can still spend Flow for techniques and narrative advantages"
    note: "This divorces spell resources from Flow while maintaining Flow mechanics"

  design_note: "For groups that prefer vancian-style resource management. Less elegant but more familiar to traditional players."

# ============================================
# ATTRIBUTE CASTING APPROACHES
# ============================================

casting_attributes:
  mind:
    name: "The Wizard's Way"
    strengths:
      - "Precision and control"
      - "Avoiding allies/collateral"
      - "Calculated effects"
      - "Perfect placement"
    
    mechanical_benefits:
      universal: "Ignore 1 point of cover/concealment"
      damage: "Can exclude X allies from area (X = Mind)"
      blessing: "Duration in hours instead of minutes"
      utility: "Perfect precision in effect"
    
    narrative_style: "Mathematical perfection, calculated angles"
  
  awareness:
    name: "The Sorcerer's Way"
    strengths:
      - "Maximum power"
      - "Instinctive casting"
      - "Sensing weaknesses"
      - "Raw magical force"
    
    mechanical_benefits:
      universal: "Spells seek weak points"
      damage: "+1 damage per die"
      detection: "Sense additional information"
      area: "Affects unseen targets"
    
    narrative_style: "Instinctive power, overwhelming force"
  
  will:
    name: "The Divine/Pact Way"
    strengths:
      - "Reliability under pressure"
      - "Persistence and duration"
      - "Unshakeable concentration"
      - "Unbreakable effects"

    mechanical_benefits:
      universal: "Advantage on concentration checks"
      concentration: "Maintains even if stunned (not unconscious)"
      duration: "Double duration"
      saves: "Targets get -1 to resist"
    
    narrative_style: "Determination, faith, inexorable force"
  
  presence:
    name: "The Bard's Way"
    strengths:
      - "Social and emotional effects"
      - "Fear and inspiration"
      - "Dramatic impact"
      - "Group influence"
    
    mechanical_benefits:
      universal: "Affects morale/emotions"
      social: "Double effect vs. composure"
      area: "Spectacular display causes awe"
      blessing: "Affects 2x normal targets"
    
    narrative_style: "Drama, performance, emotional impact"

# ============================================
# SPELL LIST BY TIER
# ============================================

spells:
  # ==========================================
  # TIER 0 - CANTRIPS
  # ==========================================
  
  tier_0:
    spark:
      name: "Spark"
      description: "Close combat magical attack"
      base_effect: "1d6 damage, touch range"
      flow: "0"
      
      attribute_variations:
        mind: 
          damage: "1d6"
          special: "Can ignite flammable objects precisely"
        awareness:
          damage: "1d6+1"
          special: "Automatically hits"
        will:
          damage: "1d6"
          special: "Unstoppable once cast"
        presence:
          damage: "1d6"
          special: "Frightens target for 1 round"
    
    mage_armor:
      name: "Mage Armor"
      description: "Protective barrier, self only"
      base_effect: "+2 Guard until hit"
      flow: "0"
      
      attribute_variations:
        mind:
          guard: 2
          special: "Absorbs first 3 damage"
        awareness:
          guard: 2
          special: "Warns of incoming attacks"
        will:
          guard: 2
          special: "Persists through unconsciousness"
        presence:
          guard: 2
          special: "Shimmers impressively, +1 social"
    
    light:
      name: "Light"
      description: "Create illumination"
      base_effect: "Bright light for scene"
      flow: "0"
      
      attribute_variations:
        mind:
          effect: "Precisely controlled beam"
          special: "Can focus like laser"
        awareness:
          effect: "Reveals hidden things"
          special: "Detects invisible"
        will:
          effect: "Cannot be dispelled"
          special: "Works in magical darkness"
        presence:
          effect: "Dazzling colors"
          special: "Provides +1 to Perform"
    
    prestidigitation:
      name: "Prestidigitation"
      description: "Minor magical effects"
      base_effect: "Small convenience magic"
      flow: "0"
      
      attribute_variations:
        mind:
          effect: "Precise manipulation"
          special: "Can pick locks at -2"
        awareness:
          effect: "Sense through creation"
          special: "Created items detect magic"
        will:
          effect: "Persistent creations"
          special: "Effects last hours"
        presence:
          effect: "Impressive displays"
          special: "+2 to entertainment"
  
  # ==========================================
  # TIER 1 - BASIC SPELLS
  # ==========================================
  
  tier_1:
    design_note: "Damage increased to 2d6 base for caster viability"

    bolt:
      name: "Bolt"
      description: "Ranged magical attack at Far range"
      base_effect: "Attribute + 2d6 damage"
      flow: "0"

      attribute_variations:
        mind:
          damage: "mind + 2d6"
          special: "Ignores cover completely"
          narrative: "Impossible angles, ricochets"
        awareness:
          damage: "awareness + 2d6 + 1"
          special: "Seeks weak points"
          narrative: "Unerring accuracy"
        will:
          damage: "will + 2d6"
          special: "Penetrates magical defenses"
          narrative: "Unstoppable force"
        presence:
          damage: "presence + 2d6"
          special: "Causes fear in nearby enemies"
          narrative: "Spectacular impact"
    
    shield:
      name: "Shield"
      description: "Protective ward for self or ally"
      base_effect: "+Attribute to Guard for scene"
      flow: "0"
      
      attribute_variations:
        mind:
          guard: "+mind"
          special: "Calculate optimal angles, no flanking"
        awareness:
          guard: "+awareness"
          special: "Warns of attacks, +1 defense"
        will:
          guard: "+will"
          special: "Persists if caster unconscious"
        presence:
          guard: "+presence"
          special: "Demoralizes attackers, -1 to hit"
    
    charm:
      name: "Charm"
      description: "Influence target's mind"
      base_effect: "Target becomes friendly"
      flow: "0"
      duration: "Scene or until betrayed"
      
      attribute_variations:
        mind:
          effect: "Actions must seem logical"
          special: "+mind to convince"
        awareness:
          effect: "Sense target's desires"
          special: "+awareness to social"
        will:
          effect: "Dominate if Will lower"
          special: "Direct control"
        presence:
          effect: "Irresistible charisma"
          special: "+presence to all social"
    
    blur:
      name: "Blur"
      description: "Defensive obscurement"
      base_effect: "+2 defense for scene"
      flow: "0"
      
      attribute_variations:
        mind:
          defense: 2
          special: "Calculated probability distortion"
        awareness:
          defense: 2
          special: "Instinctive dodging"
        will:
          defense: 2
          special: "Maintains when stunned"
        presence:
          defense: 2
          special: "Mesmerizing patterns"
    
    detect_magic:
      name: "Detect Magic"
      description: "Sense magical auras"
      base_effect: "Detect magic in Near range"
      flow: "0"
      
      attribute_variations:
        mind:
          range: "near"
          special: "Identify spell types"
        awareness:
          range: "far"
          special: "Sense through barriers"
        will:
          range: "near"
          special: "Detect alignment/intent"
        presence:
          range: "near"
          special: "Sense emotional resonance"
  
  # ==========================================
  # TIER 2 - ADVANCED SPELLS
  # ==========================================
  
  tier_2:
    design_note: "Damage increased to 3d6 base for meaningful Flow investment"

    fireball:
      name: "Fireball"
      description: "Explosive area damage"
      base_effect: "3d6 to all in zone"
      flow: "-1"

      attribute_variations:
        mind:
          damage: "3d6"
          special: "Exclude allies, precise placement"
        awareness:
          damage: "3d6+2"
          special: "Seeks most enemies"
        will:
          damage: "3d6"
          special: "Burns for 1d6/round"
        presence:
          damage: "3d6"
          special: "Causes panic, enemies flee"
    
    heal:
      name: "Heal"
      description: "Restore health"
      base_effect: "2d6 Vitality restored"
      flow: "-1"
      
      attribute_variations:
        mind:
          healing: "2d6"
          special: "Removes conditions"
        awareness:
          healing: "2d6+1"
          special: "Diagnoses problems"
        will:
          healing: "2d6"
          special: "Works at any range"
        presence:
          healing: "2d6"
          special: "Inspires, +1 Flow"
    
    fly:
      name: "Fly"
      description: "Grant flight"
      base_effect: "Fly for scene"
      flow: "-1"
      
      attribute_variations:
        mind:
          speed: "2 zones/turn"
          special: "Perfect control"
        awareness:
          speed: "3 zones/turn"
          special: "Instinctive navigation"
        will:
          speed: "2 zones/turn"
          special: "Maintains if unconscious"
        presence:
          speed: "2 zones/turn"
          special: "Dramatic swooping, +1 intimidate"
    
    invisibility:
      name: "Invisibility"
      description: "Become unseen"
      base_effect: "Invisible for scene or until attack"
      flow: "-1"
      
      attribute_variations:
        mind:
          duration: "scene"
          special: "Affects equipment perfectly"
        awareness:
          duration: "scene"
          special: "Muffles sound too"
        will:
          duration: "scene"
          special: "Can attack and stay invisible"
        presence:
          duration: "scene"
          special: "Dramatic reveal stuns enemies"
    
    web:
      name: "Web"
      description: "Create entangling area"
      base_effect: "Zone becomes difficult terrain"
      flow: "-1"
      
      attribute_variations:
        mind:
          effect: "Geometric patterns"
          special: "Can create bridges/walls"
        awareness:
          effect: "Living web"
          special: "Attacks those who enter"
        will:
          effect: "Unbreakable strands"
          special: "Cannot be destroyed"
        presence:
          effect: "Terrifying appearance"
          special: "Fear effect on trapped"
  
  # ==========================================
  # TIER 3 - EXPERT SPELLS
  # ==========================================
  
  tier_3:
    lightning_storm:
      name: "Lightning Storm"
      description: "Devastating area attack"
      base_effect: "3d6 to multiple zones"
      flow: "-2"
      
      attribute_variations:
        mind:
          damage: "3d6 to chosen targets"
          zones: 2
          special: "Precise targeting"
        awareness:
          damage: "3d6 to all enemies in sight"
          zones: "line of sight"
          special: "Cannot miss"
        will:
          damage: "3d6"
          zones: 3
          special: "Continues for 3 rounds"
        presence:
          damage: "3d6"
          zones: 2
          special: "Breaks morale, enemies flee"
    
    teleport:
      name: "Teleport"
      description: "Instant transportation"
      base_effect: "Move anywhere instantly"
      flow: "-2"
      
      attribute_variations:
        mind:
          range: "Anywhere with coordinates"
          passengers: "mind"
          special: "Perfect accuracy"
        awareness:
          range: "Anywhere you've sensed"
          passengers: "awareness"
          special: "Brings willing only"
        will:
          range: "Anywhere"
          passengers: "will"
          special: "Can bring unwilling (opposed Will)"
        presence:
          range: "Dramatic entrance"
          passengers: "presence"
          special: "+3 to next social action"
    
    polymorph:
      name: "Polymorph"
      description: "Transform creature"
      base_effect: "Change form for scene"
      flow: "-2"
      
      attribute_variations:
        mind:
          forms: "Studied creatures"
          special: "Perfect mimicry"
        awareness:
          forms: "Any observed creature"
          special: "Gain their abilities"
        will:
          forms: "Force transformation"
          special: "Works on unwilling"
        presence:
          forms: "Terrifying/beautiful forms"
          special: "Massive social impact"
    
    scrying:
      name: "Scrying"
      description: "View distant locations"
      base_effect: "See/hear remote location"
      flow: "-2"
      
      attribute_variations:
        mind:
          range: "Anywhere known"
          special: "Can analyze what's seen"
        awareness:
          range: "Find anyone"
          special: "Penetrates barriers"
        will:
          range: "Any plane"
          special: "Cannot be blocked"
        presence:
          range: "Anywhere dramatic"
          special: "Can project voice/image"
  
  # ==========================================
  # TIER 4 - MASTER SPELLS
  # ==========================================
  
  tier_4:
    time_stop:
      name: "Time Stop"
      description: "Pause time"
      base_effect: "Take extra turns"
      flow: "-3"
      
      attribute_variations:
        mind:
          turns: 3
          special: "Can set up complex plans"
        awareness:
          turns: 2
          special: "React to anything, interrupt"
        will:
          turns: 2
          special: "Extend through concentration"
        presence:
          turns: 2
          special: "Dramatic monologue, guaranteed impact"
    
    dominate:
      name: "Dominate"
      description: "Total mental control"
      base_effect: "Control target completely"
      flow: "-3"
      duration: "Scene or longer"
      
      attribute_variations:
        mind:
          effect: "Commands seem reasonable"
          special: "Undetectable control"
        awareness:
          effect: "Access all memories"
          special: "Use their skills"
        will:
          effect: "Absolute control"
          special: "Permanent if Will higher"
        presence:
          effect: "They want to serve"
          special: "Genuine devotion"
    
    meteor_swarm:
      name: "Meteor Swarm"
      description: "Ultimate destruction"
      base_effect: "4d6 to huge area"
      flow: "-3"
      
      attribute_variations:
        mind:
          damage: "4d6 precision strikes"
          special: "Hit only enemies"
        awareness:
          damage: "5d6 seeking meteors"
          special: "Cannot be dodged"
        will:
          damage: "4d6 + ongoing"
          special: "Area burns for scene"
        presence:
          damage: "4d6 + terror"
          special: "Witnesses flee in panic"
    
    wish:
      name: "Wish"
      description: "Alter reality"
      base_effect: "Limited reality change"
      flow: "-3"
      
      attribute_variations:
        mind:
          effect: "Logical changes"
          special: "No unintended consequences"
        awareness:
          effect: "Know perfect wish"
          special: "Optimal outcome"
        will:
          effect: "Force reality"
          special: "Override natural law"
        presence:
          effect: "Dramatic changes"
          special: "Legendary impact"

# ============================================
# RITUAL MAGIC
# ============================================

ritual_magic:
  description: "Extended casting for powerful effects"
  
  mechanics:
    time_required: "10+ minutes"
    flow_generation: "+3 on completion"
    interruption: "Ruins ritual, lose materials"
  
  ritual_types:
    divination:
      examples: ["Commune", "Legend Lore", "Contact Other Plane"]
      requirement: "mind or awareness"
    
    warding:
      examples: ["Magic Circle", "Forbiddance", "Hallow"]
      requirement: "will or mind"
    
    summoning:
      examples: ["Planar Ally", "Gate", "Conjure Elemental"]
      requirement: "will or presence"
    
    transformation:
      examples: ["Permanency", "Awaken", "Reincarnation"]
      requirement: "any attribute + materials"
  
  group_rituals:
    description: "Multiple casters contribute"
    mechanics:
      - "Each assistant grants +1 to roll"
      - "Can combine different traditions"
      - "Share Flow cost among participants"

# ============================================
# METAMAGIC
# ============================================

metamagic:
  description: "Modify spells with special techniques"
  acquisition: "Wizard archetype or feats"
  
  options:
    quicken:
      effect: "Cast as swift action"
      cost: "+1 Flow"
      requirement: "Mind-based casting"
    
    extend:
      effect: "Double duration"
      cost: "+1 Flow"
      requirement: "Will-based casting"
    
    empower:
      effect: "+50% damage"
      cost: "+2 Flow"
      requirement: "Awareness-based casting"
    
    silent:
      effect: "No verbal component"
      cost: "+1 Flow"
      requirement: "Mind-based casting"
    
    still:
      effect: "No somatic component"
      cost: "+1 Flow"
      requirement: "Will-based casting"
    
    widen:
      effect: "Double area"
      cost: "+2 Flow"
      requirement: "Presence-based casting"

# ============================================
# COUNTERSPELL
# ============================================

counterspell:
  description: "React to interrupt enemy spells"

  mechanics:
    trigger: "Enemy casts spell you can see"
    action: "Reaction"
    check: "Sorcery vs Sorcery (TN 8 + spell tier)"
    success: "Spell is negated"
    failure: "Spell takes effect normally"

  counterspell_consolation:
    rule: "When your spell is counterspelled, gain +2 Flow"
    reasoning: "Your magical energy rebounds, empowering your next attempt"
    effect: "Being countered becomes a setback, not a total loss"

    example:
      situation: "Cast Fireball (Tier 2, -1 Flow), enemy counterspells it"
      result: "Fireball negated, but you gain +2 Flow"
      net: "+1 Flow total (lost -1 from casting, gained +2 from being countered)"
      benefit: "Can immediately cast another Tier 2 spell at +1 Flow"

# ============================================
# MAGIC ITEMS
# ============================================

magic_items:
  creation:
    requirements:
      - "Appropriate spell known"
      - "Craft skill"
      - "Special materials"
      - "Time investment"
    
    flow_investment:
      minor: "5 Flow total over days"
      moderate: "10 Flow total over weeks"
      major: "20 Flow total over months"
  
  categories:
    consumables:
      potions:
        examples: ["Healing", "Invisibility", "Strength"]
        use: "Drink as action"
      
      scrolls:
        examples: ["Any spell"]
        use: "Read with Sorcery check"
      
      wands:
        examples: ["Specific spell, limited charges"]
        use: "Activate with Flow"
    
    permanent:
      weapons:
        enhancement_bonus: "+1 to +3"
        properties: ["Flaming", "Keen", "Vorpal"]
      
      armor:
        enhancement_bonus: "+1 to +3"
        properties: ["Fortification", "Glamered", "Ethereal"]
      
      accessories:
        examples: ["Rings", "Amulets", "Cloaks"]
        effects: ["Protection", "Enhancement", "Utility"]

# ============================================
# SPELL COMBINATIONS
# ============================================

spell_combinations:
  description: "Casting spells in sequence for synergy"
  
  examples:
    defensive_combo:
      sequence: ["mage_armor", "shield", "blur"]
      total_cost: "0, 0, 0 = 0 Flow cost"
      effect: "Layered defenses without Flow investment"

    offensive_combo:
      sequence: ["spark", "spark", "fireball"]
      total_cost: "0, 0, -1 = -1 Flow net"
      effect: "Soften targets before big spell"
    
    utility_combo:
      sequence: ["detect_magic", "dispel", "shield"]
      total_cost: "0, -1, 0 = -1 Flow"
      effect: "Counter enemy magic"
  
  advanced_combinations:
    time_stop_setup:
      sequence: ["time_stop", "blessing", "blessing", "position"]
      strategy: "Use frozen time for preparation"
    
    portal_assault:
      sequence: ["scrying", "teleport", "fireball"]
      strategy: "Scout, arrive, devastate"

# ============================================
# MAGICAL TRADITIONS
# ============================================

magical_traditions:
  arcane:
    source: "Study and knowledge"
    attribute: "mind"
    strengths: ["Versatility", "Precision", "Metamagic"]
    weaknesses: ["Requires study", "Component dependent"]
    signature_spells: ["Teleport", "Time Stop", "Wish"]
  
  divine:
    source: "Faith and devotion"
    attribute: "will"
    strengths: ["Reliability", "Healing", "Protection"]
    weaknesses: ["Deity restrictions", "Moral limitations"]
    signature_spells: ["Heal", "Resurrection", "Divine Storm"]
  
  primal:
    source: "Natural connection"
    attribute: "awareness"
    strengths: ["Elemental power", "Shapeshifting", "Territory"]
    weaknesses: ["Environment dependent", "Civilization penalty"]
    signature_spells: ["Lightning Storm", "Polymorph", "Earthquake"]
  
  performance:
    source: "Artistic expression"
    attribute: "presence"
    strengths: ["Group effects", "Emotion", "Inspiration"]
    weaknesses: ["Requires audience", "Obvious casting"]
    signature_spells: ["Charm", "Fear", "Mass Suggestion"]
  
  pact:
    source: "Bargained power"
    attribute: "will"
    strengths: ["Immediate power", "Unique abilities", "No study"]
    weaknesses: ["Patron demands", "Power can be revoked"]
    signature_spells: ["Dominate", "Summon", "Soul Cage"]

yaml/techniques.yaml:
# Flow RPG Universal Techniques
# Version: 2.0-restructured
# Abilities available to all characters through milestones

techniques_system:
  philosophy:
    core_concept: "Any character can learn any technique with proper training"
    design_principles:
      - "No archetype gates - abilities available to all"
      - "Narrative justification enhances acquisition"
      - "Flow cost balances powerful techniques"
      - "Milestone choices provide access"

  acquisition_methods:
    milestone_choice:
      description: "Select technique instead of other advancement"
      availability: "Any milestone level"

    training:
      description: "Learn from mentor or through practice"
      requirement: "Downtime and narrative justification"
      cost: "Time and possibly gold"

    discovery:
      description: "Find in ancient texts or through experimentation"
      requirement: "Research or exploration"

    archetype_package:
      description: "Archetypes provide starting techniques"
      benefit: "Immediate access without separate learning"

# ============================================
# COMBAT TECHNIQUES
# ============================================

combat_techniques:
  description: "Martial abilities for all warriors"
  source: "Originally Fighter archetype"

  basic_techniques:
    available_to: "All characters"
    no_prerequisites: true

    defensive_stance:
      effect: "+2 Guard until next turn"
      cost: "Action"
      flow_cost: 0

    power_attack:
      effect: "-2 to hit, +2 damage"
      cost: "Modifies attack"
      flow_cost: 0

    combat_expertise:
      effect: "+1 to combat rolls in chosen situation"
      examples: ["Dueling", "Mounted", "Defensive"]
      acquisition: "Minor milestone"

  flow_techniques:
    note: "No prerequisites - just milestone + Flow cost"

    riposte:
      trigger: "After successful defense"
      effect: "Immediate counterattack"
      flow_cost: 1
      acquisition: "Minor milestone"

    press_advantage:
      trigger: "While at Flow +2 or higher"
      effect: "+1d6 damage on all attacks"
      flow_cost: "Passive while condition met"
      acquisition: "Minor milestone"

    perfect_strike:
      effect: "Next attack ignores armor"
      flow_cost: 2
      acquisition: "Moderate milestone"

  advanced_techniques:
    note: "Flow cost is the only gate"

    whirlwind_strike:
      effect: "Attack all adjacent enemies"
      damage: "Normal weapon damage to each"
      flow_cost: 3
      acquisition: "Moderate milestone"

    devastating_blow:
      effect: "Double damage dice on next attack"
      flow_cost: 3
      limit: "Once per scene"
      acquisition: "Moderate milestone"

    battlefield_control:
      effect: "Reposition all combatants in zone"
      flow_cost: 3
      acquisition: "Major milestone"

# ============================================
# METAMAGIC TECHNIQUES
# ============================================

metamagic:
  description: "Spell modifications for all casters"
  source: "Originally Wizard archetype"
  note: "Available to anyone who can cast spells"

  basic_metamagic:
    note: "No prerequisites beyond spell access"

    subtle_spell:
      effect: "Cast without visible components"
      flow_cost: 1
      benefit: "Cannot be counterspelled"
      acquisition: "Minor milestone"

    extended_spell:
      effect: "Double spell duration"
      flow_cost: 1
      restriction: "Duration spells only"
      acquisition: "Minor milestone"

    careful_spell:
      effect: "Exclude allies from area effects"
      flow_cost: 1
      acquisition: "Minor milestone"

  advanced_metamagic:
    note: "Available through moderate milestones"

    empowered_spell:
      effect: "Add extra damage die"
      flow_cost: 2
      acquisition: "Moderate milestone"

    twinned_spell:
      effect: "Target two creatures"
      flow_cost: 2
      restriction: "Single-target spells only"
      acquisition: "Moderate milestone"

    quickened_spell:
      effect: "Cast as bonus action"
      flow_cost: 3
      limit: "Once per turn"
      acquisition: "Moderate milestone"

  master_metamagic:
    note: "Available through major milestones"

    heightened_spell:
      effect: "Increase save TN by 2"
      flow_cost: 3
      acquisition: "Major milestone"

    persistent_spell:
      effect: "Spell lasts entire scene"
      flow_cost: 4
      acquisition: "Major milestone"

# ============================================
# DIVINE TECHNIQUES
# ============================================

divine_techniques:
  description: "Faith-based abilities"
  source: "Originally Cleric/Paladin archetypes"
  note: "Can be reflavored as primal or arcane"

  healing_techniques:
    no_spell_requirement: true

    lay_on_hands:
      effect: "Heal 1d6 Vitality by touch"
      flow_cost: 1
      daily_uses: "Will modifier (minimum 1)"
      acquisition: "Minor milestone"

    healing_surge:
      effect: "All allies in zone recover 1d6 Guard"
      flow_cost: 2
      limit: "Once per scene"
      acquisition: "Moderate milestone"

  smite_techniques:
    requirement: "Narrative alignment with cause"

    divine_strike:
      effect: "+1d6 radiant damage vs opposed alignment"
      flow_cost: 1
      acquisition: "Minor milestone"

    banishing_smite:
      effect: "Send extraplanar creature home"
      flow_cost: 3
      save: "Will TN 10"
      acquisition: "Moderate milestone"

  aura_techniques:
    requirement: "Presence +1 or higher"

    protective_aura:
      effect: "Allies in zone get +1 to saves"
      flow_cost: 2
      duration: "Scene"
      acquisition: "Moderate milestone"

    inspiring_presence:
      effect: "Allies gain +1 Flow when you succeed"
      flow_cost: "Passive once activated"
      activation: 3
      acquisition: "Major milestone"

# ============================================
# ROGUISH GAMBITS
# ============================================

gambits:
  description: "High-risk, high-reward maneuvers"
  source: "Originally Rogue archetype"

  basic_gambits:
    available_to: "All characters"

    sneak_attack:
      trigger: "Attack with advantage or surprise"
      effect: "+1d6 damage"
      requirement: "Target unaware or flanked"
      acquisition: "Minor milestone"

      progression:
        basic: "+1d6 damage (Minor milestone)"
        improved: "+2d6 damage (Moderate milestone)"
        note: "Caps at 2d6 to prevent overshadowing Fighter damage output"

      critical_interaction:
        rule: "Sneak Attack dice are NOT multiplied on critical hits"
        reasoning: "Prevents damage spikes from turning crits into guaranteed kills"
        example:
          normal_hit: "2d6+3 (weapon) + 2d6 (sneak) = 4d6+3 avg 17"
          critical_hit: "2d6+3 (weapon) + 2d6 (sneak) = 4d6+3 avg 17 (same!)"
          without_this_rule: "Would be 6d6+3 avg 24 (too much)"

    dirty_trick:
      effect: "Blind, trip, or disarm opponent"
      contest: "Finesse vs defense"
      flow_generation: "+1 on success"
      acquisition: "Minor milestone"

  advanced_gambits:
    requirement: "Grace or Mind +2"

    impossible_dodge:
      trigger: "About to take damage"
      effect: "Negate all damage from source"
      flow_cost: 3
      limit: "Once per scene"
      acquisition: "Moderate milestone"

    shadow_step:
      effect: "Teleport behind enemy"
      range: "Within same zone"
      flow_cost: 2
      bonus: "Next attack has advantage"
      acquisition: "Moderate milestone"

  master_gambits:
    requirement: "Multiple successes with basic gambits"

    death_mark:
      effect: "Study target for vulnerability"
      duration: "One round studying"
      benefit: "Critical on 10+ vs that target"
      flow_cost: 3
      acquisition: "Major milestone"

# ============================================
# BARDIC INSPIRATION
# ============================================

inspiration_techniques:
  description: "Support and motivation abilities"
  source: "Originally Bard archetype"

  basic_inspiration:
    requirement: "Presence +1 or Perform skill"

    inspiring_word:
      effect: "Ally gains +1d6 to next roll"
      range: "Can hear you"
      flow_cost: 1
      uses: "Presence modifier per scene"
      acquisition: "Minor milestone"

    cutting_words:
      effect: "Enemy suffers -1d6 to next roll"
      range: "Can hear and understand you"
      flow_cost: 1
      acquisition: "Minor milestone"

  performance_magic:
    requirement: "Perform skill and spell access"

    song_of_rest:
      effect: "Double healing during short rest"
      duration: "10 minutes performance"
      acquisition: "Minor milestone"

    countercharm:
      effect: "Allies immune to charm/fear"
      duration: "While performing"
      flow_cost: 2
      acquisition: "Moderate milestone"

  legendary_performance:
    requirement: "Perform Expert (+2)"
    note: "Expert is the pinnacle of mortal skill"

    mass_suggestion:
      effect: "Influence crowd's emotions"
      save: "Will TN 10"
      flow_cost: 4
      acquisition: "Major milestone"

# ============================================
# TERRAIN MASTERY
# ============================================

terrain_mastery:
  description: "Environmental expertise"
  source: "Originally Ranger archetype"

  basic_terrain:
    selection: "Choose one terrain type"

    terrain_types:
      forest:
        benefits:
          - "Move through trees without slowing"
          - "Cannot be tracked"
          - "+2 to Survival"

      mountain:
        benefits:
          - "Climb at normal speed"
          - "Immune to altitude"
          - "+2 to Athletics"

      urban:
        benefits:
          - "Blend into crowds"
          - "Know all shortcuts"
          - "+2 to Stealth"

      desert:
        benefits:
          - "Half water requirements"
          - "Immune to heat exhaustion"
          - "+2 to Survival"

    acquisition: "Minor milestone per terrain"

  advanced_terrain:
    requirement: "Basic mastery in terrain"

    one_with_environment:
      effect: "Invisible while still in terrain"
      flow_cost: 2
      acquisition: "Moderate milestone"

    territorial_advantage:
      effect: "+1 to all rolls in chosen terrain"
      passive: true
      acquisition: "Moderate milestone"

  legendary_terrain:
    requirement: "Multiple terrain masteries"

    worldwalker:
      effect: "Benefits of all terrains"
      acquisition: "Major milestone"

# ============================================
# UNIVERSAL TECHNIQUES
# ============================================

universal_techniques:
  description: "Abilities not tied to any archetype"

  flow_mastery:
    flow_conservation:
      effect: "Reduce all Flow costs by 1 (minimum 0)"
      acquisition: "Major milestone"

    flow_battery:
      effect: "Maximum Flow increased to +8"
      acquisition: "Major milestone"

    flow_transfer:
      effect: "Give Flow to adjacent ally"
      rate: "2 for 1"
      acquisition: "Moderate milestone"

  legendary_abilities:
    requirement: "Two Major milestones"

    unstoppable:
      effect: "Immune to all conditions for scene"
      flow_cost: 6
      limit: "Once per day"

    perfect_action:
      effect: "Automatically succeed at any one roll"
      flow_cost: 6
      limit: "Once per session"

    legendary_resistance:
      effect: "Turn any failure into success"
      flow_cost: 3
      limit: "Three times per day"

# ============================================
# TECHNIQUE COMBINATIONS
# ============================================

technique_combinations:
  description: "Using multiple techniques together"

  examples:
    spell_blade:
      components:
        - "Quickened Spell (cast as bonus)"
        - "Perfect Strike (ignore armor)"
      total_cost: 5
      effect: "Cast spell and attack in same turn"

    perfect_ambush:
      components:
        - "Shadow Step (teleport)"
        - "Sneak Attack (bonus damage)"
        - "Death Mark (improved critical)"
      total_cost: 6
      effect: "Devastating surprise attack"

    divine_storm:
      components:
        - "Whirlwind Strike (hit all)"
        - "Divine Strike (radiant damage)"
        - "Inspiring Presence (allies gain Flow)"
      total_cost: 7
      effect: "Inspire allies while destroying enemies"

  design_note: "Combinations reward system mastery"

# ============================================
# LEARNING PATHS
# ============================================

suggested_paths:
  warrior_path:
    minor_milestones:
      - "Combat Expertise"
      - "Riposte"
      - "Weapon Focus"
    moderate_milestones:
      - "Whirlwind Strike"
      - "Perfect Strike"
    major_milestone:
      - "Battlefield Control"

  caster_path:
    minor_milestones:
      - "Subtle Spell"
      - "Careful Spell"
      - "Extended Spell"
    moderate_milestones:
      - "Empowered Spell"
      - "Quickened Spell"
    major_milestone:
      - "Persistent Spell"

  support_path:
    minor_milestones:
      - "Inspiring Word"
      - "Lay on Hands"
      - "Song of Rest"
    moderate_milestones:
      - "Healing Surge"
      - "Protective Aura"
    major_milestone:
      - "Inspiring Presence"

  custom_path:
    philosophy: "Mix and match as desired"
    example:
      - "Sneak Attack + Subtle Spell"
      - "Riposte + Inspiring Word"
      - "Terrain Mastery + Metamagic"

# End of Techniques File
