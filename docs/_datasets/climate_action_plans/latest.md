---
name: climate_action_plans
title: Climate Action Plans
description: "Crowdsourced dataset of location of climate actions plans\n"
version: latest
licenses:
- name: CC-BY-4.0
  path: https://creativecommons.org/licenses/by/4.0/
  title: Creative Commons Attribution 4.0 International License
contributors:
- title: mySociety
  path: https://mysociety.org
  role: author
- title: Climate Emergency UK
  path: https://www.climateemergency.uk/
  role: author
custom:
  build: climate_action_plans_dataset.build:build
  tests:
  - test_climate_action_plans
  dataset_order: 0
  download_options:
    gate: default
    survey: default
    header_text: default
  composite:
    xlsx:
      include: all
      exclude: none
      render: true
    sqlite:
      include: all
      exclude: none
      render: true
    json:
      include: all
      exclude: none
      render: true
  change_log:
    0.1.0: initial version
    0.1.1: Added CEUK as contributor
resources:
- title: Council Action Plans
  description: Crowdsourced collection of URLs for local council climate action plans
  custom:
    row_count: 1466
  path: councils_plans.csv
  name: councils_plans
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local_authority_code
      type: string
      description: Three/four letter code for the local authority
      constraints:
        unique: false
      example: ABE
    - name: council
      type: string
      description: Name for local authority (not necessarily official name)
      constraints:
        unique: false
      example: Aberdeen City Council
    - name: search_link
      type: string
      description: Link used to search for the council
      constraints:
        unique: false
      example: https://www.google.com/search?q=Aberdeen+City+Council+climate+action+plan
    - name: unfound
      type: string
      description: Looked and nothing found
      constraints:
        unique: false
      example: X
    - name: credit
      type: string
      description: Person who collected the info
      constraints:
        unique: false
      example: '@RewilderBeast'
    - name: url
      type: string
      description: URL to the plan
      constraints:
        unique: false
      example: https://committees.aberdeencity.gov.uk/documents/s109158/CouncilEnergyAndClimateRoutemap%20-%20Appendix.pdf
    - name: date_retrieved
      type: string
      description: Data the plan was found
      constraints:
        unique: false
      example: 15/02/2021
    - name: time_period
      type: string
      description: Time period the plan covers
      constraints:
        unique: false
      example: 2021-2025
    - name: type
      type: string
      description: Type of plan
      constraints:
        unique: false
      example: Pre-plan
    - name: scope
      type: string
      description: Council only or Whole Area
      constraints:
        unique: false
      example: Council only
    - name: status
      type: string
      description: Current status of the plan. draft / interim / proposal / approved
        / etc
      constraints:
        unique: false
      example: Draft
    - name: homepage_mention
      type: string
      description: Council mentions environment/climate action/sustainability on homepage
      constraints:
        unique: false
      example: No
    - name: dedicated_page
      type: string
      description: Is there a page decidated to this with a link to their plan thats
        easy to find?
      constraints:
        unique: false
      example: No
    - name: well_presented
      type: string
      description: "Is this well-presented for public understanding?\ne.g. Is it a\
        \ set of appendices to a council meeting minutes document, or a standalone\
        \ document with some introduction to the context\n"
      constraints:
        unique: false
      example: Well presented visual aids and clear intro
    - name: baseline_analysis
      type: string
      description: Is there a baseline analysis of the CO2 emissions int he area?
      constraints:
        unique: false
      example: Yes
    - name: notes
      type: string
      description: Additional notes
      constraints:
        unique: false
      example: "Council voted not to declare a climate emergency. \n"
    - name: plan_due
      type: string
      description: When is the full action plan due if there isn't one yet?
      constraints:
        unique: false
      example: '2022'
    - name: title
      type: string
      description: Title of the plan
      constraints:
        unique: false
      example: Energy and Climate Plan ???Routemap???
    - name: title_checked
      type: string
      description: Has the automated title generated been checked
      constraints:
        unique: false
      example: y
  hash: 90c4a6dabf2a85ed3b78b5c30dd6431f
  download_id: climate-action-plans-councils-plans
full_version: 0.1.1
permalink: /datasets/climate_action_plans/latest
---
