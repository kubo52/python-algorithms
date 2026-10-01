def calculate_gc(sequence: str) -> float:
    """Return the GC-content ratio of a DNA sequence."""
    clean_seq = sequence.upper().strip()
    if not clean_seq:
        return 0.0
    gc_count = clean_seq.count("G") + clean_seq.count("C")
    return gc_count / len(clean_seq)


if __name__ == "__main__":
    test_dna = "AGCTATAGCGATCGCG"
    print(f"Sequence: {test_dna}")
    print(f"GC Ratio: {calculate_gc(test_dna):.2%}")
