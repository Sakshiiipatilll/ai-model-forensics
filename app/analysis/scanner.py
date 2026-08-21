from .statistics import get_statistics
from .entropy import calculate_entropy
from .precision import precision_stats
from .bit_analysis import bit_pattern_score


def scan_model(weights):
    results = {}

    for name, tensor in weights.items():
        if tensor.is_floating_point():
            results[name] = get_statistics(tensor)
            results[name]["entropy"] = calculate_entropy(tensor)
            results[name].update(precision_stats(tensor))
            results[name]["bit_entropy"] = bit_pattern_score(tensor)

    return results