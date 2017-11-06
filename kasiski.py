from math import sqrt


def _repeated_seq_pos(text, seq_len):
    seq_pos = {}  # entries of sequence : [positions]
    for i, char in enumerate(text):
        next_seq = text[i:i+seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
    repeated = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    rep_seq_pos = [(seq, seq_pos[seq]) for seq in repeated]
    return rep_seq_pos


def _get_spacings(positions):
    return [positions[i+1] - positions[i] for i in range(len(positions)-1)]


def _get_factors(number):
    factors = set()
    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)
    return sorted(factors)


def _candidate_key_lengths(factor_lists, max_key_len):
    all_factors = [factor_lists[lst][fac] for lst in range(len(factor_lists)) for fac in range(len(factor_lists[lst]))]
    # exclude factors larger than suspected max key length
    candidate_lengths = list(filter(lambda x:  x <= max_key_len, all_factors))
    # sort by probability (descending)
    sorted_candidates = sorted(set(candidate_lengths), key=lambda x: all_factors.count(x), reverse=True)
    return sorted_candidates


def find_key_length(cyphertext, seq_len, max_key_len):
    # find repeated sequences and their positions
    rsp = _repeated_seq_pos(text=cyphertext, seq_len=seq_len)
    seq_spc = {}
    for seq, positions in rsp:
        seq_spc[seq] = _get_spacings(positions)
    # calculate spacings between positions of each repeated
    # sequence and factor out spacings
    factor_lists = []
    for spacings in seq_spc.values():
        for space in spacings:
            factor_lists.append(_get_factors(number=space))
    # get common factors by descending frequency,
    # which constitute candidate key lengths
    ckl = _candidate_key_lengths(factor_lists=factor_lists, max_key_len=max_key_len)
    key_len = ckl[0]
    return key_len
