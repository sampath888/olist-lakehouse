# Phase 1 findings

Date: 2026-11-01

| Item | Result | Notes |
|---|---|---|
| Custom catalog `olist_lakehouse` | PASS | Created without a managed location |
| Schemas (bronze, silver, gold, ops, lab) and volumes (seed, landing, checkpoints) | PASS | Created by `notebooks/00_setup_catalog.py`, safe to re-run |
| Git folder clone from public repo | PASS | |
| Git folder push | PASS | The Databricks GitHub app link had no write access. A PAT with the GitHub username and Contents read/write fixed it |
| `.py` notebook round trip (Databricks, GitHub, Mac) | PASS | File keeps `# Databricks notebook source` and stays `.py` |
| Outbound access from serverless | PASS | github.com, pypi.org and raw.githubusercontent.com all returned 200 |
| `%pip install` on serverless | PASS (partial) | pytest was already installed, so a fresh download is untested. pypi.org itself is reachable |
| Dashboards in sidebar | Visible | Creating one is untested |
| Upload 9 Olist CSVs to `ops.seed` | PASS | |
| Hello bundle (CLI auth) | pending | Decides whether CI can deploy or we fall back to manual deploy |