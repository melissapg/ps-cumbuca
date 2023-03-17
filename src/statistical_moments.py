import statistics


def statistical_moments(samples: list[float], k: int, central: bool) -> float:
    """
    Calcula o momento amostral ou momento central de ordem k de uma lista de amostras.

    :param samples: Lista de amostras.
    :param k: K-ésimo momento a ser calculado.
    :param central: Indica se o momento central deve ser calculado e retornado (True) ou não (False).
    :return: O valor do momento amostral ou momento central de ordem k.
    """
    if not samples:
        raise ValueError("A lista de amostras não pode ser vazia.")

    moment, central_moment = 0.0, 0.0

    mean = statistics.mean(samples)  # primeiro momento amostral

    for sample in samples:
        moment += sample ** k
        central_moment += (sample - mean) ** k

    moment /= len(samples)
    central_moment /= len(samples)

    return central_moment if central else moment