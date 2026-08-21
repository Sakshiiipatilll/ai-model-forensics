import torch


def get_weights(model):
    if isinstance(model, dict):
        return {
            k: v for k, v in model.items()
            if isinstance(v, torch.Tensor)
        }

    return model.state_dict()