#!/usr/bin/python
# -*- coding: UTF-8 -*-


def nucl2aa_codon(nucl_seq, re_aa=True):
    nucl_seq = nucl_seq.upper().replace('U', 'T')
    aa_num, aa_list, codon_list = int(len(nucl_seq) / 3), [], []
    if len(nucl_seq[(aa_num - 1) * 3:]) != 3:
        print('\n\t!!! Warning: Your sequence is not a cds!!!  Please checked your sequence.')
        return None
    dict_u = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
              'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
              'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
              'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
              # --------------------------------------------#
              'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
              'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
              'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
              'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
              # --------------------------------------------#
              'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
              'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
              'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
              'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
              # --------------------------------------------#
              'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
              'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
              'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
              'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}
    for i in range(aa_num):
        codon_list.append(nucl_seq[0 + 3 * i: 3 + 3 * i])
        if dict_u.get(nucl_seq[0 + 3 * i: 3 + 3 * i]) is not None:
            aa_list.append(dict_u.get(nucl_seq[0 + 3 * i: 3 + 3 * i]))
        else:
            aa_list.append('X')
    if '*' in ''.join(aa_list[:-1]):
        print('\n\t!!! Warning: Stop codons in the body of sequence.')
    elif 'X' in ''.join(aa_list[:-1]):
        print('\n\t!!! Warning: Unknown amino acid (X) in the body of sequence.')
    if re_aa is True:
        return ''.join(aa_list)
    else:
        return codon_list


if __name__ == "__main__":
    nucl_seq_1 = 'ATGGTTTCCAAAGGAGAAGAAAATAATATGtaa'
    print("nucl_seq_1 to aa: ", nucl2aa_codon(nucl_seq_1))
    print("nucl_seq_1 to codon: ", nucl2aa_codon(nucl_seq_1, re_aa=False))

    nucl_seq_2 = 'ATGGTTTCCAAAGGAGAAGAAAATAATATGta'
    print("nucl_seq_2 to aa: ", nucl2aa_codon(nucl_seq_2))

    nucl_seq_3 = 'ATGGTTTCCAAAGGAGAAGAAAATAATtaaATG'
    print("nucl_seq_3 to aa: ", nucl2aa_codon(nucl_seq_3))

    nucl_seq_4 = 'ATGGTTTCCANNNGAGAAGAAAATAATATGtaa'
    print("nucl_seq_4 to aa: ", nucl2aa_codon(nucl_seq_4))

"""
nucl_seq_1 to aa:  MVSKGEENNM*
nucl_seq_1 to codon:  ['ATG', 'GTT', 'TCC', 'AAA', 'GGA', 'GAA', 'GAA', 'AAT', 'AAT', 'ATG', 'TAA']

	!!! Warning: Your sequence is not a cds!!!  Please checked your sequence.
nucl_seq_2 to aa:  None

	!!! Warning: Stop codons in the body of sequence.
nucl_seq_3 to aa:  MVSKGEENN*M

	!!! Warning: Unknown amino acid (X) in the body of sequence.
nucl_seq_4 to aa:  MVSXXEENNM*
"""
