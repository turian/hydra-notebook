import hydra.experimental
hydra.experimental.initialize(config_path="conf")
cfg=hydra.experimental.compose(config_name="config.yaml")
