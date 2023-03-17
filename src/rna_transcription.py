def dna_transcription(dna: str) -> str:
    """
    Calcula a transcrição de um DNA (ácido desoxirribonucleico) para RNA (ácido ribonucleico).

    :param dna: Cadeia de nucleotídeos de um DNA.
    :return: A transcrição para uma cadeia de RNA.
    """
    rna_transcription = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''
    
    if not isinstance(dna, str):
        raise TypeError("O tipo da variável 'DNA' é restrito a strings.")

    try:
        for nucleotide in dna:
            rna += rna_transcription[nucleotide]
    except KeyError as k:
        raise KeyError(f"Durante a transcrição do DNA, a presença do nucleotídeo {k.args[0]} não é válida.")
    return rna