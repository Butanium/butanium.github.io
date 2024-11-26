---
title: "Tiny-Dashboard: A Lightweight Feature Activation Analysis Tool"
collection: projects
permalink: /projects/tiny-dashboard
excerpt: 'A minimal, hackable package for building feature activation dashboards in transformer models'
date: 2024-11-26
venue: "Open Source Project"
codeurl: https://github.com/Butanium/tiny-activation-dashboard/
---

Tiny-Dashboard is a lightweight Python package designed to make feature activation analysis in neural language models more accessible and customizable. While other tools like `SAEDashboard` and `sae_vis` offer comprehensive features, Tiny-Dashboard prioritizes simplicity and hackability.

## Key Features

The package supports both offline and online analysis modes:

### Offline Analysis
- Explore pre-computed feature activations
- Visualize max activation examples
- Generate shareable HTML reports
- Support for both in-memory and database-backed storage

### Online Analysis
- Real-time feature activation analysis
- Support for chat template formatting
- Custom prompt testing
- Interactive visualization

## Implementation

The tool is built with flexibility in mind, offering both class-based and function-based approaches for customization. It includes specialized implementations like the CrosscoderOnlineFeatureDashboard, which was developed during the CrossCoders project to analyze combined base and instruct model activations.

The package is available on PyPI: 
```bash
pip install tiny-dashboard
```	

For detailed usage examples and documentation, visit the [GitHub repository](https://github.com/Butanium/tiny-activation-dashboard/).