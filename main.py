# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import hydra.experimental
#hydra.experimental.initialize(config_path="conf")
hydra.experimental.initialize_with_module(module="module", config_path="conf")
cfg=hydra.experimental.compose(config_name="config.yaml")


cfg=hydra.experimental.compose(config_name="config.yaml")

import module


